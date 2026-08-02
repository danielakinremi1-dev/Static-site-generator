from src.textnode import TextNode, TextType


def main():
    type = TextType.PLAIN
    new = TextNode("Hello, World!", type, None)
    print(new)


main()