from textnode import TextType , TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError(f"Invalid markdown: unbalanced delimiter {delimiter}")

        for i, section in enumerate(sections):
            if section == "":
                continue
            if i % 2 == 0:  
                new_nodes.append(TextNode(section, TextType.TEXT))
            else:  
                new_nodes.append(TextNode(section, text_type))
        
    return new_nodes


def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return links


def split_nodes_image(old_nodes):
    new_nodes = [] 
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        temp_text = node.text
        for image in images:
            image_alt = image[0]
            image_link = image[1]
            sections = temp_text.split(f"![{image_alt}]({image_link})", 1)
            if sections[0] != "":
                text_node = TextNode(sections[0],TextType.TEXT)
                new_nodes.append(text_node)
            image_node = TextNode(image[0],TextType.IMAGE,image[1])
            new_nodes.append(image_node)

            temp_text = sections[1]
        if temp_text != "":
            new_nodes.append(TextNode(temp_text,TextType.TEXT))
    return new_nodes
            
   

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text,)
        if not links:
            new_nodes.append(node)
            continue
        temp_text = node.text
        for link in links:
            link_alt = link[0]
            link_link = link[1]
            sections = temp_text.split(f"[{link_alt}]({link_link})", 1)
            if sections[0] != "":
                text_node = TextNode(sections[0],TextType.TEXT)
                new_nodes.append(text_node)
            link_node = TextNode(link[0],TextType.LINK,link[1])
            new_nodes.append(link_node)
            temp_text = sections[1]
        if temp_text != "":
            new_nodes.append(TextNode(temp_text,TextType.TEXT))
    return new_nodes
    

def text_to_textnodes(text):
    if not text:
        return [TextNode("", TextType.TEXT)]

    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)


    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    nodes = split_nodes_image(nodes)

    nodes = split_nodes_link(nodes)

    return nodes
