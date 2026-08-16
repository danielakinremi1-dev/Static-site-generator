from src.markdown_to_html_node import markdown_to_html_node
import unittest


class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_multi_block(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

1. This is an ordered list
2. With some items

- Here's an unordered list block
- With an inline **bold** item

> A quote blocks been entered here
> With a second _line_ and italics

### Heading to finish off

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><ol><li>This is an ordered list</li><li>With some items</li></ol><ul><li>Here's an unordered list block</li><li>With an inline <b>bold</b> item</li></ul><blockquote>A quote blocks been entered here With a second <i>line</i> and italics</blockquote><h3>Heading to finish off</h3><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    