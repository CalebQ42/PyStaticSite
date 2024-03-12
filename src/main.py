import os
import shutil

from blocks import block_to_block_type, markdown_to_blocks, valid_blocks
from helpers import mk_to_html_node

def main():
    shutil.rmtree("public")
    setup_dirs("static", "public")
    generate_pages_recursive("content", "template.html", "public")

def setup_dirs(frm, to):
    if os.path.exists(to):
        shutil.rmtree(to)
    os.mkdir(to)
    fils = os.listdir(frm)
    for f in fils:
        pth = os.path.join(frm, f)
        if os.path.isfile(pth):
            shutil.copy(pth, to)
        elif os.path.isdir(pth):
            setup_dirs(pth, os.path.join(to, f))

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for b in blocks:
        typ = block_to_block_type(b)
        if typ == valid_blocks[1]:
            spl = b.split(" ", 1)
            if len(spl[0]) == 1:
                return spl[1]
    raise Exception("main header (#) not present.")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    mkd = ""
    tmpl = ""
    with open(from_path) as f:
        mkd = f.read()
    with open(template_path) as f:
        tmpl = f.read()
    tmpl = tmpl.replace("{{ Title }}", extract_title(mkd)).replace("{{ Content }}", mk_to_html_node(mkd).to_html())
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w") as f:
        f.write(tmpl)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
    fils = os.listdir(dir_path_content)
    for f in fils:
        print(f)
        pth = os.path.join(dir_path_content, f)
        if os.path.isfile(pth):
            generate_page(pth, template_path, os.path.join(dest_dir_path, f.replace(".md", ".html")))
        elif os.path.isdir(pth):
            if not os.path.exists(os.path.join(dest_dir_path, f)):
                os.makedirs(os.path.join(dest_dir_path, f))
            generate_pages_recursive(pth, template_path, os.path.join(dest_dir_path, f))

main()