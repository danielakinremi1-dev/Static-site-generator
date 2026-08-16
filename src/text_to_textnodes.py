from src.textnode import TextNode, TextType
from src.markdown_conversions import split_nodes_delimiter, split_nodes_image, split_nodes_link
def text_to_textnodes(text: str) -> list[TextNode]:
    initial_node = [TextNode(text, TextType.TEXT)]
    text_nodes = split_nodes_delimiter(initial_node, "`", TextType.CODE)
    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    return text_nodes
