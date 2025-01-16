def sum_of_list(lst):
    if not lst:  # Base case: empty list
        return 0
    return lst[0] + sum_of_list(lst[1:])

# Example
lst = [1, 2, 3, 4, 5]
print("Sum of list:", sum_of_list(lst))
