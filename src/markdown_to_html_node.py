from src.text_to_textnodes import text_to_textnodes
from src.textnode import text_node_to_html_node, TextNode, TextType
from src.markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from src.htmlnode import LeafNode, ParentNode, HTMLNode

# Need to make function for each block type to convert to HTMLNode, and then combine them in the main function.

def markdown_to_html_node(markdown_text: str) -> LeafNode: 
    final_htmlnode = ParentNode("div", [], None)
    blocks = markdown_to_blocks(markdown_text)


    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            htmlnode = heading_to_html_node(block)
            final_htmlnode.children.append(htmlnode)

        elif block_type == BlockType.QUOTE:
            htmlnode = quote_to_html_node(block)
            final_htmlnode.children.append(htmlnode)

        elif block_type == BlockType.UNORDERED_LIST:
            htmlnode = unordered_list_to_html_node(block)
            final_htmlnode.children.append(htmlnode)

        elif block_type == BlockType.ORDERED_LIST:
            htmlnode = ordered_list_to_html_node(block)
            final_htmlnode.children.append(htmlnode)

        elif block_type == BlockType.CODE:
            htmlnode = code_to_html_node(block)
            final_htmlnode.children.append(htmlnode)

        else:
            htmlnode = paragraph_to_html_node(block)
            final_htmlnode.children.append(htmlnode)

    return final_htmlnode




    
#---------------------
def heading_to_html_node(block: str) -> HTMLNode:
    hashtags = block[0:7].count("#")
    tag = "h" + str(hashtags)
    htmlnode = ParentNode(tag, [], None)

    clean_block = block[hashtags:].strip()
    children = text_to_children(clean_block)
    htmlnode.children = children
    return htmlnode

#---------------------
def quote_to_html_node(block: str) -> HTMLNode:
    tag = "blockquote"
    htmlnode = ParentNode(tag, [], None)

    clean_block = quote_cleaner(block)
    children = text_to_children(clean_block)
    htmlnode.children = children
    return htmlnode

def quote_cleaner(block: str) -> str:
    lines = block.split("\n")
    cleaned_lines = []
    for line in lines:
        stripped = line.lstrip(">").strip()
        cleaned_lines.append(stripped)
    return " ".join(cleaned_lines)

#---------------------
def unordered_list_to_html_node(block: str) -> HTMLNode:
    tag = "ul"
    htmlnode = ParentNode(tag, [], None)

    clean_block_lines = unordered_list_cleaner(block)
    for line in clean_block_lines:
        inner_html_tag = "li"
        inner_html_children = text_to_children(line)
        inner_html = ParentNode(inner_html_tag, inner_html_children, None) 
        htmlnode.children.append(inner_html) 
    return htmlnode


def unordered_list_cleaner(block: str) -> list[str]:
    lines = block.split("\n")
    cleaned_lines = []
    for line in lines:
        stripped = line.lstrip("-").strip()
        cleaned_lines.append(stripped)
    return cleaned_lines

#---------------------
def ordered_list_to_html_node(block: str) -> HTMLNode:
    tag = "ol"
    htmlnode = ParentNode(tag, [], None)

    clean_block_lines = ordered_list_cleaner(block)
    for line in clean_block_lines:
        inner_html_tag = "li"
        inner_html_children = text_to_children(line)
        inner_html = ParentNode(inner_html_tag, inner_html_children, None) 
        htmlnode.children.append(inner_html) 
    return htmlnode


def ordered_list_cleaner(block: str) -> list[str]:
    lines = block.split("\n")
    cleaned_lines = []
    for line in lines:
        stripped = line.lstrip("0123456789.").strip()
        cleaned_lines.append(stripped)
    return cleaned_lines

#---------------------
def code_to_html_node(block: str) -> HTMLNode:
    tag = "pre"
    htmlnode = ParentNode(tag, [], None)

    clean_block = block[3:-3].lstrip()
    text_child = TextNode(clean_block, TextType.CODE)
    html_child = text_node_to_html_node(text_child)
    htmlnode.children.append(html_child)
    return htmlnode

#---------------------
def paragraph_to_html_node(block: str) -> HTMLNode:
    tag = "p"
    htmlnode = ParentNode(tag, [], None)

    clean_block = block.replace("\n", " ")
    children = text_to_children(clean_block)
    htmlnode.children = children
    return htmlnode

#---------------------
def text_to_children(text ) -> list[LeafNode]:
    textnodes = text_to_textnodes(text) 
    children = []
    for textnode in textnodes:
        new_htmlnode = text_node_to_html_node(textnode)
        children.append(new_htmlnode)
    return children




 
 