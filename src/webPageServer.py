import re
from block_to_html import markdown_to_html_node
import os
def extract_title(markdown):
    lines = markdown.strip().split('\n')
    found = False
    for line in lines:
        line = line.strip()
        if re.match(r"^# ",line):
            found = True
            return line[2:]
    if not found:
        raise Exception("No title found")
    
    
def generate_page(from_path,template_path,dest_path):
    print(f"Generating HTML file from ${from_path} to ${dest_path} using ${template_path}")
    with open(from_path,"r") as f:
        markdown = f.read()
    with open(template_path,"r") as f:
        template = f.read()
    
    html = markdown_to_html_node(markdown=markdown)
    title = extract_title(markdown)
    page = re.sub(r"{{ Title }}",title,template)
    page = re.sub(r"{{ Content }}",html.to_html(), page)
    
    with open(dest_path,"w") as f:
        f.write(page)
    
    
def generate_pages_recursive(dir_path_content,template_path,dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise Exception("Invalid Directory Path")
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content,item)
        if os.path.isfile(item_path):
            if item.endswith(".md"):
                dest_path = os.path.join(dest_dir_path, item.replace(".md", ".html"))
                generate_page(item_path, template_path, dest_path)
        elif os.path.isdir(item_path):
            sub_dest_dir_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(item_path, template_path, sub_dest_dir_path)
            


    
    
def test():
    # Test case 1: Valid title
    markdown = "# Hello"
    title = extract_title(markdown)
    assert title == "Hello", "Test case 1 failed"

    # Test case 2: Valid title with extra space
    markdown = "#    World"
    title = extract_title(markdown)
    assert title == "   World", "Test case 2 failed"

    # Test case 3: No title (should raise Exception)
    markdown = "Just some text\n## Subtitle"
    try:
        extract_title(markdown)
        assert False, "Test case 3 failed: Exception not raised"
    except Exception as e:
        assert str(e) == "No title found", "Test case 3 failed: Wrong exception message"

    # Test case 4: Title not at the top
    markdown = "Text\n# Heading\nMore text"
    title = extract_title(markdown)
    assert title == "Heading", "Test case 4 failed"

    print("All test cases passed.")

test()
