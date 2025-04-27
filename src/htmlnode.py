class HTMLNODE():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        html =""
        for key,value in self.props.items():
            tag = f"{key}=\"{value}\""
            html = html + " " + tag
        return html
    def __eq__(self, other):
        if not isinstance(other, HTMLNODE):
            return False
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)

    def __repr__(self):
        return f"Tag : {self.tag} \n Value: {self.value} \n Children: {self.children} \n Props:: {self.props}"

class LeafNode(HTMLNODE):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"LeafNode({self.tag} , {self.value} , {self.props})"

class ParentNode(HTMLNODE):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children=children,props=props) # Corrected super() call
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent Node Must have a Valid HTML tag")
        if self.children is None:
            raise ValueError("Without children how you are a parent?")
        
        child_html = ""
        for child in self.children:
            child_html += child.to_html()
        if self.props:
            html = f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"
        else:
            html =f"<{self.tag}>{child_html}</{self.tag}>"
        return html
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"