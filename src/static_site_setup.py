import os
import shutil
from src.markdown_to_html_node import markdown_to_html_node

def static_runner(sourcedir: str, targetdir: str) -> None:
    if not os.path.isdir(sourcedir):
        raise ValueError("Must use valid directory for source")

    if os.path.isdir(targetdir):
        shutil.rmtree(targetdir)

    os.makedirs(targetdir, exist_ok=True)
    sourcedir_items = os.listdir(sourcedir)
      
    for item in sourcedir_items:
        item_path = os.path.join(sourcedir, item)
        if os.path.isfile(item_path):  
            shutil.copy(item_path, targetdir)

        elif os.path.isdir(item_path): 
            copied_dir = os.path.join(targetdir, item)
            os.mkdir(copied_dir)
            static_runner(item_path, copied_dir)

def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[1:].strip()
    raise Exception("Must have h1 header")


def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, mode="r", encoding="utf-8") as file:
        from_contents = file.read()
    with open(template_path, mode="r", encoding="utf-8") as file:
            tem_contents = file.read()

    from_htmlstring = markdown_to_html_node(from_contents).to_html()
    from_title = extract_title(from_contents)
    tem_contents = tem_contents.replace("{{ Title }}", from_title)
    tem_contents = tem_contents.replace("{{ Content }}", from_htmlstring)
    tem_contents = tem_contents.replace(f'href="/', f'href="{basepath}')
    tem_contents = tem_contents.replace(f'src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(tem_contents)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str) -> None:
    dir_contents = os.listdir(dir_path_content)

    for item in dir_contents:
        item_path = os.path.join(dir_path_content, item)
        if os.path.isfile(item_path) and item_path.endswith(".md"): 
            destination_path = os.path.join(dest_dir_path, item)
            destination_path = destination_path[:-3] + ".html"
            generate_page(item_path, template_path, destination_path, basepath)
        elif os.path.isdir(item_path):
            new_dest_dir = os.path.join(dest_dir_path, item)
            generate_pages_recursive(item_path, template_path, new_dest_dir, basepath)