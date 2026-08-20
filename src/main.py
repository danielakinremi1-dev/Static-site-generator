from src.static_site_setup import static_runner, generate_pages_recursive
import sys


origin = "content"
template = "template.html"
destination = "docs"

sourcedir = "static"
targetdir = "docs"

if len(sys.argv) < 2:
    basepath = "/"
else:
    basepath = sys.argv[1]


def main():
    print("Starting static site generator")
    static_runner(sourcedir, targetdir)
    generate_pages_recursive(origin, template, destination, basepath)
    print("Initialized")


if __name__ == "__main__":
    main()









