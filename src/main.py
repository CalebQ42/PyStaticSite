from htmlnode import LeafNode
from textnode import TextNode

def main():
    tn = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(tn)

def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == "text":
        return LeafNode(value=text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == "code":
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == "link":
        return LeafNode(tag="a", value=text_node.text, props={'href': text_node.url})
    elif text_node.text_type == "image":
        return LeafNode("img", "", {"alt": text_node.text, "src": text_node.url})
    raise Exception("Invalid text_type")

main()