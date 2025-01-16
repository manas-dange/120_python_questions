def reverse_list(numbers):
    for i in range(len(numbers) // 2):
        numbers[i], numbers[-i - 1] = numbers[-i - 1], numbers[i]
    return numbers

# Example
numbers = [1, 2, 3, 4, 5]
print("Reversed list:", reverse_list(numbers))
