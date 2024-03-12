import re

from textnode import TextNode

valid_types = [
    "text",   #0
    "bold",   #1
    "italic", #2
    "code",   #3
    "link",   #4
    "image",  #5
]

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    out = []
    for n in old_nodes:
        if type(n) != TextNode or n.text_type == valid_types[3]:
            out.append(n)
            continue
        spl = n.text.split(delimiter)
        if len(spl) % 2 == 0:
            raise Exception(f"uneven {delimiter}'s. invalid markdown") 
        middle = False
        for i in range(0, len(spl)):
            if not middle:
                middle = True
                if spl[i] == "":
                    continue
                out.append(TextNode(spl[i], n.text_type, n.url))
                continue
            middle = False
            if spl[i] == "":
                continue
            out.append(TextNode(spl[i], text_type))
    return out

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    out = []
    for n in old_nodes:
        if type(n) != TextNode or n.text_type == valid_types[3]:
            out.append(n)
            continue
        imgs = extract_markdown_images(n.text)
        if not imgs:
            out.append(n)
            continue
        to_process = n.text
        for i in imgs:
            spl = to_process.split(f"![{i[0]}]({i[1]})", 1)
            if spl[0] != "":
                out.append(TextNode(spl[0], n.text_type))
            out.append(TextNode(i[0], valid_types[5], i[1]))
            to_process = spl[1]
        if to_process != "":
            out.append(TextNode(to_process, n.text_type))
    return out

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_link(old_nodes):
    out = []
    for n in old_nodes:
        if type(n) != TextNode or n.text_type == valid_types[3]:
            out.append(n)
            continue
        lnks = extract_markdown_links(n.text)
        if not lnks:
            out.append(n)
            continue
        to_process = n.text
        for i in lnks:
            spl = to_process.split(f"[{i[0]}]({i[1]})", 1)
            if spl[0] != "":
                out.append(TextNode(spl[0], n.text_type))
            out.append(TextNode(i[0], valid_types[4], i[1]))
            to_process = spl[1]
        if to_process != "":
            out.append(TextNode(to_process, n.text_type))
    return out