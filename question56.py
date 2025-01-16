def dict_from_two_lists(keys, values):
    return dict(zip(keys, values))

# Example
keys = ['a', 'b', 'c']
values = [1, 2, 3]
print("Dictionary:", dict_from_two_lists(keys, values))
