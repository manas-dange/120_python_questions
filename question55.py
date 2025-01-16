def is_sorted(numbers):
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))

# Example
numbers = [1, 2, 3, 4, 5]
print("Is the list sorted?", is_sorted(numbers))
