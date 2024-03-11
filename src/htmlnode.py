class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if not self.props:
            return ""
        out = ""
        for k in self.props:
            out += f" {k}=\"{self.props[k]}\""
        return out

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("value must be specified")
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("value must be specified")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if not children:
            raise ValueError("children must be specified")
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if not self.children:
            raise ValueError("children must be specified")
        out = ""
        if self.tag:
            out += f"<{self.tag}{self.props_to_html()}>"
        for c in self.children:
            out += c.to_html()
        if self.tag:
            out += f"</{self.tag}>"
        return out