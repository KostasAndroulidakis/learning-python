# OpenEDG Python Institute
# Python Essentials 2
# 4.4.1.8 LAB: The os module

import os

def find(path, dir):
    """
    Find directories with the specified name within the given path.
    """
    # Check if the provided path is a directory
    if not os.path.isdir(path):
        print(f"The path '{path}' is not a valid directory.")
        return

    # Get the absolute path of the starting directory
    abs_starting_path = os.path.abspath(path)
    
    # Iterate through the directory structure
    for root, dirs, files in os.walk(path):
        # Check if the target directory is in the current directory
        if dir in dirs:
            # Construct the absolute path to the found directory
            found_path = os.path.join(root, dir)
            abs_found_path = os.path.abspath(found_path)
            
            # Create the formatted path - always starts with .../ 
            # and shows the path relative to the current directory
            formatted_path = "..." + abs_found_path[len(os.getcwd()):]
            
            # Replace backslashes with forward slashes for consistent output
            # regardless of operating system
            formatted_path = formatted_path.replace("\\", "/")
            
            print(formatted_path)

# Test the function with the example input
if __name__ == "__main__":
    # Example from the lab requirements
    path = "./tree"
    dir = "python"
    print(f"Finding '{dir}' in '{path}':")
    find(path, dir)