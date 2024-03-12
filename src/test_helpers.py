import unittest

from split_nodes import valid_types
from helpers import text_to_textnodes
from textnode import TextNode

class Tests(unittest.TestCase):
    def test_text_to_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This is ", valid_types[0]),
                TextNode("text", valid_types[1]),
                TextNode(" with an ", valid_types[0]),
                TextNode("italic", valid_types[2]),
                TextNode(" word and a ", valid_types[0]),
                TextNode("code block", valid_types[3]),
                TextNode(" and an ", valid_types[0]),
                TextNode("image", valid_types[5], "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", valid_types[0]),
                TextNode("link", valid_types[4], "https://boot.dev"),
            ]
        )

if __name__ == "__main__":
    unittest.main()