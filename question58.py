def invert_dictionary(d):
    return {value: key for key, value in d.items()}

# Example
d = {'a': 1, 'b': 2, 'c': 3}
print("Inverted dictionary:", invert_dictionary(d))
