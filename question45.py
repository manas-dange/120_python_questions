def linear_search(numbers, target):
    for i, num in enumerate(numbers):
        if num == target:
            return i
    return -1

# Example
numbers = [10, 20, 30, 40, 50]
target = 30
print(f"Index of {target}:", linear_search(numbers, target))
