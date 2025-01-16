import random

def pick_random_element(lst):
    return random.choice(lst)

# Example
my_list = [1, 2, 3, 4, 5]
print("Random choice:", pick_random_element(my_list))
