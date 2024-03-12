from blocks import block_to_block_type, markdown_to_blocks, valid_blocks
from htmlnode import LeafNode, ParentNode
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

def mk_to_html_node(text: str):
    text = text.strip()
    if text == "":
        return ParentNode("div", [])
    block_nodes = []
    blocks = markdown_to_blocks(text)
    if not blocks:
        raise Exception("no markdown blocks found")
    for b in blocks:
        b = b.strip()
        if b == "":
            continue
        typ = block_to_block_type(b)
        par_node = None
        if typ == valid_blocks[1]:
            spl = b.split(" ", 1)
            h_num = len(spl[0])
            if h_num > 6:
                h_num = 6
            par_node = ParentNode(f"h{h_num}")
            b = spl[1]
        elif typ == valid_blocks[2]:
            b = b.removeprefix("```").removesuffix("```").strip("\n")
            par_node = ParentNode("pre", [LeafNode("code", b)])
            b = ""
        elif typ == valid_blocks[3]:
            par_node = ParentNode("blockquote")
            b = b.removeprefix(">").strip()
        elif typ == valid_blocks[4]:
            subs = []
            list_items = b.split("\n")
            for i in list_items:
                item = []
                nodes = text_to_textnodes(i[1:].strip())
                for n in nodes:
                    item.append(text_node_to_html_node(n))
                subs.append(ParentNode("li", item))
            par_node = ParentNode("ul", subs)
            b = ""
        elif typ == valid_blocks[5]:
            subs = []
            list_items = b.split("\n")
            for i in list_items:
                item = []
                nodes = text_to_textnodes(i[2:].strip())
                for n in nodes:
                    item.append(text_node_to_html_node(n))
                subs.append(ParentNode("li", item))
            par_node = ParentNode("ol", subs)
            b = ""
        else:
            par_node = ParentNode("p")
        if b != "":
            subs = []
            nodes = text_to_textnodes(b)
            for n in nodes:
                subs.append(text_node_to_html_node(n))
            par_node.children = subs
        block_nodes.append(par_node)
    return ParentNode("div", block_nodes)