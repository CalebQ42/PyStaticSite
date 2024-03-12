class TextNode:
    def __init__(self, text: str, text_type:str, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        if type(node) != TextNode:
            return False
        if node.text != self.text or node.text_type != self.text_type or node.url != self.url:
            return False
        return True

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"