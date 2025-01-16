def frequency_count(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    return frequency

# Example
numbers = [1, 2, 3, 2, 4, 5, 2, 3, 4]
print("Frequency count:", frequency_count(numbers))
