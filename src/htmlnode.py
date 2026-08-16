

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError("to_html method must be implemented in subclasses")

    def props_to_html(self):
        if self.props is None:
            return ""
        return " " + " ".join(f'{key.replace('"', '')}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return (
                self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props
            )
        return False


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value 
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        
        if self.tag is None:
            raise ValueError("Tag cannot be None for ParentNode")
        if self.children is None:
            raise ValueError("Children cannot be None for ParentNode")

        children = ""
        for child in self.children:
            children += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"

    