from src.textnode import TextNode, TextType
import re

def extract_markdown_images(text: str) -> list[(str, str)]:
    img_matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return img_matches

def extract_markdown_links(text: str) -> list[(str, str)]:
    link_matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_matches


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = [] 
    delimiter_type = text_type

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            blocks = node.text.split(delimiter)
            if len(blocks) % 2 != 1:
                raise Exception("Invalid markdown syntax, check delimiters")
            for block in range(len(blocks)):
                if block % 2 == 1:
                    next_node = TextNode(blocks[block], delimiter_type)
                    new_nodes.append(next_node)
                else:
                    next_node = TextNode(blocks[block], TextType.TEXT)
                    new_nodes.append(next_node)
    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = [] 
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            string = node.text
            for image in images:

                string = string.split(f"![{image[0]}]({image[1]})")
                new_txt_node = TextNode(string[0], TextType.TEXT)
                new_nodes.append(new_txt_node)
                new_img_node = TextNode(image[0], TextType.IMAGE, image[1])
                new_nodes.append(new_img_node)
                string = string[1]
            if len(string) > 0:
                new_nodes.append(TextNode(string, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = [] 
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            string = node.text
            for link in links:

                string = string.split(f"[{link[0]}]({link[1]})")
                new_txt_node = TextNode(string[0], TextType.TEXT)
                new_nodes.append(new_txt_node)
                new_link_node = TextNode(link[0], TextType.LINK, link[1])
                new_nodes.append(new_link_node)
                string = string[1]
            if len(string) > 0:
                new_nodes.append(TextNode(string, TextType.TEXT))

    return new_nodes

