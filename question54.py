import random

def shuffle_list(numbers):
    random.shuffle(numbers)
    return numbers

# Example
numbers = [1, 2, 3, 4, 5]
print("Shuffled list:", shuffle_list(numbers))
