def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Example
lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]
print("Common elements:", common_elements(lst1, lst2))
