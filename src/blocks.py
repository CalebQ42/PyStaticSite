
valid_blocks = [
    "paragraph",
    "heading",
    "code",
    "quote",
    "unordered_list",
    "ordered_list"
]

def block_to_block_type(block: str):
    if block.startswith("# "):
        return valid_blocks[1]
    if block.startswith("```") and block.endswith("```"):
        return valid_blocks[2]
    if block.startswith(">"):
        return valid_blocks[3]
    if block.startswith("*") or block.startswith("-"):
        newlines = block.count("\n")
        bullets = block.count("\n*") + block.count("\n-")
        if newlines == bullets:
            return valid_blocks[4]
    if block.startswith("1."):
        num = 1
        valid = True
        for l in block.split("\n"):
            if not l.startswith(str(num)+"."):
                valid = False
                break
        if valid:
            return valid_blocks[5]
    return valid_blocks[0] 

def markdown_to_blocks(text):
    code_block_spl = text.split("```")
    if len(code_block_spl) == 1:
        return text.split("\n\n")
    if len(code_block_spl)%2 == 0:
        raise Exception("uneven code blocks (```). Invalid markdown")
    middle = False
    out = []
    for s in code_block_spl:
        if not middle:
            middle = True
            if s == "":
                out += s.split("\n\n")
            continue
        middle = False
        out.append("```"+s+"```")
    return out