def flatten_list(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

# Example
nested_list = [1, [2, [3, 4], 5], 6]
print("Flattened list:", flatten_list(nested_list))
