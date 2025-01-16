def remove_even_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

# Example
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("List without even numbers:", remove_even_numbers(numbers))
