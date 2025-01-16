def generate_square_dict(n):
    return {x: x**2 for x in range(1, n + 1)}

# Example
n = 5
print("Generated dictionary:", generate_square_dict(n))
