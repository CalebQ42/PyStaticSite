import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "HELLO", props={"href": "https://www.boot.dev"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.boot.dev\"")
    
    def test_repr(self):
        node = HTMLNode("a", "HELLO", props={"href": "https://www.boot.dev"})
        node2 = HTMLNode("a", "HELLO", props={"href": "https://www.boot.dev"})
        self.assertEqual(str(node), str(node2))

    def test_leaf(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("a", "Click me!", {"href": "https://www.google.com"})

                    ]
                ),
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), '<p><p><a href="https://www.google.com">Click me!</a></p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

if __name__ == "__main__":
    unittest.main()