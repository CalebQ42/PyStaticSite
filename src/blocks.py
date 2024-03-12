
valid_blocks = [
    "paragraph",
    "heading",
    "code",
    "quote",
    "unordered_list",
    "ordered_list"
]

def markdown_to_blocks(text):
    return text.split("\n\n")

