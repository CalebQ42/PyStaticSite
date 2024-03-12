import unittest

from helpers import text_to_textnodes
from split_nodes import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image, split_nodes_link, valid_types
from textnode import TextNode

# valid_types = [
#     "text",       #0
#     "bold",       #1
#     "italic",     #2
#     "code",       #3
#     "link",       #4
#     "image",      #5
# ]

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_type(self):
        node = TextNode("This is a text node", "italics")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_split_nodes(self):
        node = TextNode("This is text with a `code block` word", valid_types[0])
        new_nodes = split_nodes_delimiter([node], "`", valid_types[3])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", valid_types[0]),
                TextNode("code block", valid_types[3]),
                TextNode(" word", valid_types[0]),
            ]
        )
        node = TextNode("Hello **WORLD**", valid_types[0])
        node2 = TextNode("This should not be **split up** or **cause an exception", valid_types[3])
        node3 = TextNode("This is bold and this is *italics*", valid_types[1])
        new_nodes = split_nodes_delimiter([node, node2, node3], "**", valid_types[1])
        new_nodes = split_nodes_delimiter(new_nodes, "*", valid_types[2])
        self.assertEqual(
            new_nodes,
            [
                TextNode("Hello ", valid_types[0]),
                TextNode("WORLD", valid_types[1]),
                TextNode("This should not be **split up** or **cause an exception", valid_types[3]),
                TextNode("This is bold and this is ", valid_types[1]),
                TextNode("italics", valid_types[2])
            ]
        )
    
    def test_mk_link_img(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        self.assertEqual(
            extract_markdown_images(text),
            [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")]
        )
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(
            extract_markdown_links(text),
            [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        )

    def test_img_link(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            valid_types[0],
        )
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("This is text with an ", valid_types[0]),
                TextNode("image", valid_types[5], "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", valid_types[0]),
                TextNode(
                    "second image", valid_types[5], "https://i.imgur.com/3elNhQu.png"
                ),
            ]
        )
        node = TextNode(
            "Hello [world](https://darkstorm.tech) and also to everyone at [boot.dev](https://boot.dev)",
            valid_types[0]
        )
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("Hello ", valid_types[0]),
                TextNode("world", valid_types[4], "https://darkstorm.tech"),
                TextNode(" and also to everyone at ", valid_types[0]),
                TextNode("boot.dev", valid_types[4], "https://boot.dev")
            ]
        )

if __name__ == "__main__":
    unittest.main()
