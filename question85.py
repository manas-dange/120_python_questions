import csv

def read_csv_file(filename):
    try:
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Example
read_csv_file("example.csv")
