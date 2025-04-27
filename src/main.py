from textnode import TextNode, TextType
from htmlnode import LeafNode , HTMLNODE , ParentNode

def main():
    text_node = TextNode("Hello, World!", TextType.TEXT, "http://example.com")
    print(text_node)
    


if __name__ == "__main__":
    main()