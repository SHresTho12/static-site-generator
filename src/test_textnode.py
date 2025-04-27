import unittest

from textnode import TextNode, TextType , text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        self.assertEqual(node, node2)
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, http://example.com)")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node2), "TextNode(This is a text node, bold, None)")
    def test_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

        node3 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node3)

        node4 = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        self.assertNotEqual(node, node4)
        node5 = TextNode("This is a text node", TextType.BOLD, "http://example.org")
        self.assertNotEqual(node, node5)
        node6 = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        node7 = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        self.assertEqual(node6, node7)
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
if __name__ == "__main__":
    unittest.main()