import os
import shutil

def main():
    shutil.rmtree("public")
    os.mkdir("public")
    setup_dirs("static", "public")

def setup_dirs(frm, to):
    if not os.path.exists(to):
        os.mkdir(to)
    fils = os.listdir(frm)
    for f in fils:
        pth = os.path.join(frm, f)
        if os.path.isfile(pth):
            shutil.copy(pth, to)
        elif os.path.isdir(pth):
            setup_dirs(pth, os.path.join(to, f))

main()