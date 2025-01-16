def write_to_file(filename):
    try:
        text = input("Enter a line of text to write to the file: ")
        with open(filename, 'w') as file:
            file.write(text)
        print(f"Text written to '{filename}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example
filename = "output.txt"
write_to_file(filename)
