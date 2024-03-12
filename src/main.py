from htmlnode import LeafNode
from split_nodes import extract_markdown_images
from textnode import TextNode
import re

def main():
    text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
    print(extract_markdown_images(text))

main()