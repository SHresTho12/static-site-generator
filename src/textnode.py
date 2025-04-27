from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"



class TextNode():
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, value):
        if self.text != value.text:
            return False
        if self.text_type != value.text_type:
            return False
        if self.url != value.url:
            return False
        return True
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):  
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None,value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b",text_node.text,None)
    elif text_node.text_type is TextType.ITALIC:
        return LeafNode("i",text_node.text,None)
    elif text_node.text_type is TextType.CODE:
        return LeafNode("code",text_node.text,None)
    elif text_node.text_type is TextType.LINK:
        return LeafNode("a",text_node.text,{"href":text_node.url})
    elif text_node.text_type is TextType.IMAGE:
        return LeafNode("img","",{"src":text_node.url,"alt":text_node.text})
