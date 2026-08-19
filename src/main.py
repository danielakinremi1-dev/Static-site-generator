from src.static_site_setup import static_runner, generate_pages_recursive
import sys


origin = "/home/akinremd/Workspace/Static_site_generator/content"
template = "/home/akinremd/Workspace/Static_site_generator/template.html"
destination = "/home/akinremd/Workspace/Static_site_generator/docs"

sourcedir = "/home/akinremd/Workspace/Static_site_generator/static"
targetdir = "/home/akinremd/Workspace/Static_site_generator/docs"

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









