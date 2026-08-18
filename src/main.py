from src.static_site_setup import static_runner, generate_page


origin = "/home/akinremd/Workspace/Static_site_generator/content/index.md"
template = "/home/akinremd/Workspace/Static_site_generator/template.html"
destination = "/home/akinremd/Workspace/Static_site_generator/public/index.html"



def main():
    print("Starting static site generator")
    static_runner()
    generate_page(origin, template, destination)


if __name__ == "__main__":
    main()









