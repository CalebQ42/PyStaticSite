import unittest
from htmlnode import LeafNode, ParentNode

from split_nodes import valid_types
from helpers import mk_to_html_node, text_to_textnodes
from textnode import TextNode

class TestHelpers(unittest.TestCase):
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
    
    def test_mk_to_html_nodes(self):
        text = """
# Heading *with italics*

### Code

```
let's also do some **code**



with a bunch of enters to confuse things*
```

## Lists

* How about an **unorder**
* List [with a link](https://darkstorm.tech)

1. Or even an ordered list
2. With an _image_
3. ![image](https://darkstorm.tech/favicon.png)

> And don't forget the **quotes** with `inline code`
"""
        self.assertEqual(
            mk_to_html_node(text).to_html(),
            ParentNode("div",[
                ParentNode("h1", [
                    LeafNode(value="Heading "),
                    LeafNode("i", "with italics")
                ]),
                ParentNode("h3", [
                    LeafNode(value="Code")
                ]),
                ParentNode("pre",[
                    LeafNode("code", "let's also do some **code**\n\n\n\nwith a bunch of enters to confuse things*")
                ]),
                ParentNode("h2", [
                    LeafNode(value="Lists")
                ]),
                ParentNode("ul",[
                    ParentNode("li",[
                        LeafNode(value="How about an "),
                        LeafNode("b", "unorder")
                    ]),
                    ParentNode("li", [
                        LeafNode(value="List "),
                        LeafNode("a", "with a link", {"href": "https://darkstorm.tech"})
                    ])
                ]),
                ParentNode("ol", [
                    ParentNode("li", [
                        LeafNode(value="Or even an ordered list")
                    ]),
                    ParentNode("li", [
                        LeafNode(value="With an "),
                        LeafNode("i", "image")
                    ]),
                    ParentNode("li", [
                        LeafNode("img", "", props={"alt": "image", "src": "https://darkstorm.tech/favicon.png"})
                    ])
                ]),
                ParentNode("blockquote", [
                    LeafNode(value="And don't forget the "),
                    LeafNode("b", "quotes"),
                    LeafNode(value=" with "),
                    LeafNode("code", "inline code")
                ])
            ]).to_html()
        )

if __name__ == "__main__":
    unittest.main()