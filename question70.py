def binary_search(lst, target, low, high):
    if low > high:  # Base case: target not found
        return -1
    mid = (low + high) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        return binary_search(lst, target, mid + 1, high)
    else:
        return binary_search(lst, target, low, mid - 1)

# Example
lst = [1, 3, 5, 7, 9, 11]
target = 5
print(f"Index of {target}:", binary_search(lst, target, 0, len(lst) - 1))
