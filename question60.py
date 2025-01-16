def merge_dictionaries(d1, d2):
    merged = d1.copy()
    for key, value in d2.items():
        merged[key] = merged.get(key, 0) + value
    return merged

# Example
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
print("Merged dictionary:", merge_dictionaries(d1, d2))
