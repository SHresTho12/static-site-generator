import os
import shutil
def source_to_destination(source,destination):
    source = os.path.abspath(source)
    destination = os.path.abspath(destination)
    
    if not os.path.exists(source):
        raise Exception("Invalid Source Destination")
    
    if not os.path.exists(destination):
        os.makedirs(destination)
    else:
        for item in os.listdir(destination):
            item_path = os.path.join(destination,item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
    
    for item in os.listdir(source):
        src_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)

        if os.path.isfile(src_path):
            print("Copying file: ", item, "from", src_path, "to", dest_path)
            shutil.copy2(src_path, dest_path)
        elif os.path.isdir(src_path):
            print("Copying directory: ", item, "from", src_path, "to", dest_path)
            os.makedirs(dest_path, exist_ok=True)
            source_to_destination(src_path, dest_path)  
            