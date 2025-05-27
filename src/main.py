from textnode import TextNode, TextType
from htmlnode import LeafNode , HTMLNODE , ParentNode
from staticContentPuller import source_to_destination
from webPageServer import generate_page , generate_pages_recursive



def main():
    source_to_destination("/home/maloti12/shreshtho/self/projects/boots/static-site-generator/static","/home/maloti12/shreshtho/self/projects/boots/static-site-generator/public")
    generate_pages_recursive("/home/maloti12/shreshtho/self/projects/boots/static-site-generator/content","/home/maloti12/shreshtho/self/projects/boots/static-site-generator/template.html","/home/maloti12/shreshtho/self/projects/boots/static-site-generator/public")
    
    


if __name__ == "__main__":
    main()