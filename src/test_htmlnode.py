
import unittest

from htmlnode import HTMLNODE , LeafNode , ParentNode

class TestHTMLNODE(unittest.TestCase):
    
    def test_eq(self):
        
        node = HTMLNODE("<table>","I am a table","<tr><td>Row 1</td></tr>",{"border":"1"})
        node2 = HTMLNODE("<table>","I am a table","<tr><td>Row 1</td></tr>",{"border":"1"})
        self.assertEqual(node, node2)

    def test_not_equal(self):
        
        node = HTMLNODE("<table>","I am a table","<tr><td>Row 1</td></tr>",{"border":"1"})
        node2 = HTMLNODE("<table>","I am a different table","<tr><td>Row 1</td></tr>",{"border":"1"})
        self.assertNotEqual(node, node2)

        node3 = HTMLNODE("<table>","I am a table","<tr><td>Row 1</td></tr>",{"border":"2"})
        self.assertNotEqual(node, node3)
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!") 
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
if __name__ == "__main__":
    unittest.main()