import os
import shutil
from src.markdown_to_html_node import markdown_to_html_node

def static_runner(sourcedir = "/home/akinremd/Workspace/Static_site_generator/static", targetdir = "/home/akinremd/Workspace/Static_site_generator/public") -> None:
    if not os.path.isdir(sourcedir) or not os.path.isdir(targetdir):
        return ValueError("Must use valid directories")

    shutil.rmtree(targetdir)
    os.mkdir(targetdir)
    sourcedir_items = os.listdir(sourcedir)
      
    for item in sourcedir_items:
        item_path = os.path.join(sourcedir, item)
        if os.path.isfile(item_path):
            with open("/home/akinremd/Workspace/Static_site_generator/static_files_log.txt", "a", encoding="utf-8") as file:
                file.write(f"Copied file {item}\n")
            item_path = os.path.join(sourcedir, item)
            shutil.copy(item_path, targetdir)

        elif os.path.isdir(item_path):
            with open("/home/akinremd/Workspace/Static_site_generator/static_files_log.txt", "a", encoding="utf-8") as file:
                file.write(f"Copied directory {item}\n")
            copied_dir = os.path.join(targetdir, item)
            os.mkdir(copied_dir)
            static_runner(item_path, copied_dir)

def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[1:].strip()
    raise Exception("Must have h1 header")


def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, mode="r", encoding="utf-8") as file:
        from_contents = file.read()
    with open(template_path, mode="r", encoding="utf-8") as file:
            tem_contents = file.read()

    from_htmlstring = markdown_to_html_node(from_contents).to_html()
    from_title = extract_title(from_contents)
    tem_contents = tem_contents.replace("{{ Title }}", from_title)
    tem_contents = tem_contents.replace("{{ Content }}", from_htmlstring)

    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(tem_contents)

