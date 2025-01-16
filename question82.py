def find_longest_word_in_file(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
        return max(words, key=len)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

# Example
print("Longest word:", find_longest_word_in_file("example.txt"))
