from block_splitter import markdown_to_blocks
from blockNode import block_to_block_type,BlockType,BlockTags
from htmlnode import HTMLNODE , ParentNode , LeafNode
from text_splitter import text_to_textnodes
from textnode import text_node_to_html_node
import re

def markdown_to_html_node(markdown):
    
    blocks = markdown_to_blocks(markdown)
    tags , types = type_to_tag(blocks)
    html_nodes = list(map(lambda pair:HTMLNODE(tag=pair[0],value=pair[1]),zip(tags,blocks)))
    converted_nodes = process_parents_nodes(html_nodes , types)
    page_node = ParentNode(tag="div",children=converted_nodes)
    return page_node


def process_nodes_to_page(nodes):
    html = "<div>"
    for node in nodes:
        html += node.to_html()
    html += "</div>"
    return html


def process_parents_nodes(html_nodes , types):
    result_nodes = []
    for node , type in zip(html_nodes,types):
        if type == BlockType.CODE:
            if not node.value.startswith("```") or not node.value.endswith("```"):
                raise ValueError("invalid code block")
            lines = node.value.strip().splitlines()
            if lines and lines[0].startswith("```") and lines[-1].startswith("```"):
                code_lines = lines[1:-1] 
            else:
                code_lines = lines
            code_text = "\n".join(code_lines) + "\n"

            # Create nested <pre><code> structure
            code_node = LeafNode(tag="code", value=code_text)
            pre_node = LeafNode(tag="pre", value=code_node.to_html())
            result_nodes.append(pre_node)
        if type == BlockType.HEADING:
            updated_value = node.value.lstrip("#").strip()
            heading_node = LeafNode(tag=node.tag,value=updated_value)
            result_nodes.append(heading_node)
        if type == BlockType.QUOTE:
            val = " ".join(line.lstrip("> ").strip() for line in node.value.splitlines())
            node.value = val
            result_nodes.append(LeafNode("blockquote", val))
        if type == BlockType.UNORDERED_LIST:
            child_nodes = list_childs(node.value)
            new_node = ParentNode(tag=node.tag,children=child_nodes)
            result_nodes.append(new_node)
        if type == BlockType.ORDERED_LIST:
            child_nodes = ol_list_childs(node.value)
            new_node = ParentNode(tag=node.tag,children=child_nodes)
            result_nodes.append(new_node)
        if type == BlockType.PARAGRAPH:
            val =  " ".join(node.value.strip().splitlines())
            child_nodes = list(map(text_node_to_html_node,text_to_textnodes(val)))
            new_node = ParentNode(tag=node.tag,children=child_nodes)
            result_nodes.append(new_node)
    
    return result_nodes 
          

def ol_list_childs(text):
    lines = text.split("\n")
    child_nodes = []
    for line in lines:
        line = line[3:]
        child = text_to_children(line)
        child = ParentNode(tag="li",children=child) 
        child_nodes.append(child)
    return child_nodes
        
def list_childs(text):
    lines = text.split("\n")
    child_nodes = []
    for line in lines:
        line = line.strip("- ")
        child = ParentNode(tag="li",children=text_to_children(line))
        child_nodes.append(child)
    return child_nodes
    
def type_to_tag(blocks):    
    blocks_with_types = list(map(block_to_block_type, blocks))
    tags = []

    for block, block_type in zip(blocks, blocks_with_types):
        if block_type == BlockType.HEADING:
            # Count the number of leading '#' (up to 6)
            match = re.match(r'^(#{1,6})\s', block)
            if match:
                level = len(match.group(1))
                tags.append(f"h{level}")
            else:
                tags.append("h1")
        else:
            tags.append(BlockTags[block_type.name].value)
    
    return tags , blocks_with_types

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    child_nodes = list(map(text_node_to_html_node,text_nodes))
    return child_nodes
    
def test_markdown_to_html():
    md = """
# Header

## Header 2

Paragraph

- list item
- list item

1. Ordered List item
2. Ordered List item

[Link](www.something.com)

I am trying to understand **what is happening** here. As _italic_ is miss understood everywhere

![image](image.com)

_italic Text_

**Bold Text**'

``` Some code you _don't need to wary about_ It *should be as it is* ```

>I am the best man alive
>That's a lie


"""
    htmls = markdown_to_html_node(md)
    print(htmls)
    
    
# test_markdown_to_html()