from src.textnode import TextNode, TextType
from pathlib import Path


def main():
    type = TextType.PLAIN
    new = TextNode("Hello, World!", type, None)
    print(new)


if __name__ == __main__:
    main()


def static_runner(sourcedir: Path, targetdir: Path) -> None:
    