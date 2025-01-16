def search_in_file(filename, substring):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
            if substring in line:
                print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Example
search_in_file("example.txt", "search_term")
