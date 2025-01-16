def find_duplicates(numbers):
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

# Example
numbers = [1, 2, 3, 2, 4, 5, 6, 4, 7]
print("Duplicates:", find_duplicates(numbers))
