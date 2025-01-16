def key_exists(d, key):
    return key in d

# Example
d = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
print(f"Key '{key}' exists:", key_exists(d, key))
