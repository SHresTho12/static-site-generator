from textnode import TextNode, TextType
from htmlnode import LeafNode , HTMLNODE , ParentNode
from staticContentPuller import source_to_destination
from webPageServer import generate_page , generate_pages_recursive
import os
import shutil
import sys

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    if len(sys.argv) < 2:
        basepath = "/"
        print("Defaulting to static and content directories")
    else:
        basepath = sys.argv[1]
        print(f"The base path is {basepath}")
        
    # source_to_destination("/home/maloti12/shreshtho/self/projects/boots/static-site-generator/static","/home/maloti12/shreshtho/self/projects/boots/static-site-generator/public")
    # generate_pages_recursive("/home/maloti12/shreshtho/self/projects/boots/static-site-generator/content","/home/maloti12/shreshtho/self/projects/boots/static-site-generator/template.html","/home/maloti12/shreshtho/self/projects/boots/static-site-generator/public")
    source_to_destination(dir_path_static, dir_path_public)
    generate_pages_recursive(dir_path_content, template_path, dir_path_public,basepath)
    
    
    


if __name__ == "__main__":
    main()