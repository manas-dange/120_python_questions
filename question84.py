def append_to_file(filename):
    try:
        text = input("Enter a line of text to append to the file: ")
        with open(filename, 'a') as file:
            file.write(text + '\n')
        print(f"Text appended to '{filename}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example
append_to_file("example.txt")
