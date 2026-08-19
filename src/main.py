from src.static_site_setup import static_runner, generate_pages_recursive


origin = "/home/akinremd/Workspace/Static_site_generator/content"
template = "/home/akinremd/Workspace/Static_site_generator/template.html"
destination = "/home/akinremd/Workspace/Static_site_generator/public"



def main():
    print("Starting static site generator")
    static_runner()
    generate_pages_recursive(origin, template, destination)
    print("Initialized")


if __name__ == "__main__":
    main()









