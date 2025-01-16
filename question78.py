def copy_file(source, destination):
    try:
        with open(source, 'r') as src_file, open(destination, 'w') as dest_file:
            dest_file.write(src_file.read())
        print(f"Contents copied from {source} to {destination}.")
    except FileNotFoundError:
        print(f"File '{source}' not found.")

# Example
copy_file("source.txt", "destination.txt")
