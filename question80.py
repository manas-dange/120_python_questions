def line_count_in_file(filename):
    try:
        with open(filename, 'r') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0

# Example
print("Line count:", line_count_in_file("example.txt"))
