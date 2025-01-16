import os

def list_files_and_directories():
    items = os.listdir()
    for item in items:
        print(item)

# Example
list_files_and_directories()
