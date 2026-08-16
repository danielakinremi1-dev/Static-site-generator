import unittest

from src.markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        text = """# Heading 1

## Heading 2

This is a paragraph."""
        blocks = markdown_to_blocks(text)
        block_types = [block_to_block_type(block) for block in blocks]
        expected = [BlockType.HEADING, BlockType.HEADING, BlockType.PARAGRAPH]
        self.assertEqual(block_types, expected)