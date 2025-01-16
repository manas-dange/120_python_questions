def second_largest(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    if len(unique_numbers) < 2:
        return None  # Not enough elements for second largest
    unique_numbers.sort()
    return unique_numbers[-2]

# Example
numbers = [10, 20, 4, 45, 99, 45]
print("Second largest:", second_largest(numbers))
