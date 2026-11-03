# Static Site Generator

A static site generator written from scratch in Python with no third-party libraries. It turns a folder of Markdown files into a full HTML website, rendered through a shared template.

**Live demo:** https://danielakinremi1-dev.github.io/Static-site-generator/

## How it works

1. **Copy static assets:** the contents of `static/` (CSS, images) are copied recursively into `docs/`. Any previous build is removed first.
2. **Parse Markdown into blocks:** each page is split into blocks and classified as a heading, paragraph, quote, code block, ordered list or unordered list.
3. **Parse inline Markdown:** text inside each block is split into typed nodes for bold, italic, inline code, links and images.
4. **Build an HTML tree:** nodes become `LeafNode` and `ParentNode` objects that render themselves recursively with `to_html()`.
5. **Render pages:** the HTML and the page's `# h1` title are injected into `template.html`. Each `content/**/index.md` is written to the same path under `docs/` as `.html`.
6. **Rewrite paths:** root-relative `href`/`src` links are rewritten with a configurable base path, so the site works when it's served from a GitHub Pages subdirectory.

## Project structure

```
.
├── src/
│   ├── main.py                  # Entry point
│   ├── textnode.py              # Inline text node types
│   ├── htmlnode.py              # HTMLNode / LeafNode / ParentNode
│   ├── markdown_conversions.py  # Inline parsing (delimiters, links, images)
│   ├── text_to_textnodes.py     # Inline parsing pipeline
│   ├── markdown_blocks.py       # Block splitting and classification
│   ├── markdown_to_html_node.py # Block → HTML node conversion
│   ├── static_site_setup.py     # Asset copying and page generation
│   └── tests/                   # Unit tests
├── content/                     # Markdown source pages
├── static/                      # CSS and images
├── template.html                # Page template
└── docs/                        # Generated site (served by GitHub Pages)
```

## Usage

Requires Python 3.12+.

Build the site and serve it locally at http://localhost:8888:

```bash
./main.sh
```

Build for GitHub Pages (uses the `/Static-site-generator/` base path):

```bash
./build.sh
```

Run the tests:

```bash
./test.sh
```

## Adding content

Create a Markdown file at `content/<path>/index.md` that starts with a `# Title` heading, then rebuild. The page is generated at `docs/<path>/index.html`.
 
