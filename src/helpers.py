import re

from htmlnode import LeafNode
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link, valid_types
from textnode import TextNode


def text_to_textnodes(text):
    nodes = split_nodes_delimiter([TextNode(text, valid_types[0])], "`", valid_types[3])
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", valid_types[1])
    nodes = split_nodes_delimiter(nodes, "__", valid_types[1])
    nodes = split_nodes_delimiter(nodes, "*", valid_types[2])
    nodes = split_nodes_delimiter(nodes, "_", valid_types[2])
    return nodes

def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == valid_types[0]: #text
        return LeafNode(value=text_node.text)
    elif text_node.text_type == valid_types[1]: #bold
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == valid_types[2]: #italics
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == valid_types[3]: #code
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == valid_types[4]: #link
        return LeafNode(tag="a", value=text_node.text, props={'href': text_node.url})
    elif text_node.text_type == valid_types[5]: #image
        return LeafNode("img", "", {"alt": text_node.text, "src": text_node.url})
    raise Exception("Invalid text_type")