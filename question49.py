def rotate_list(numbers, k):
    k %= len(numbers)  # Handle rotations greater than the list size
    return numbers[-k:] + numbers[:-k]

# Example
numbers = [1, 2, 3, 4, 5]
k = 2
print("Rotated list:", rotate_list(numbers, k))
