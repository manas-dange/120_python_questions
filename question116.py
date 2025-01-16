# Context manager to open, write, and close a file
class FileWriter:
    def __enter__(self):
        self.file = open("output.txt", "w")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Using the context manager
with FileWriter() as f:
    f.write("Hello, this is a test message.")

print("Message written to output.txt")
