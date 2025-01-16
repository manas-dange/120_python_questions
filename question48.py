def count_occurrences(numbers, target):
    return numbers.count(target)

# Example
numbers = [1, 2, 3, 2, 4, 2, 5]
target = 2
print(f"The number {target} appears {count_occurrences(numbers, target)} times.")
