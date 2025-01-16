def word_count_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
        words = text.split()
        return len(words)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0

# Example
print("Word count:", word_count_in_file("example.txt"))
