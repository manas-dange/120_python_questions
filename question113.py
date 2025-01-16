from functools import reduce

# Use filter to get odd numbers and reduce to sum them
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Use reduce to sum the odd numbers
sum_of_odds = reduce(lambda x, y: x + y, odd_numbers)
print("Sum of odd numbers:", sum_of_odds)
