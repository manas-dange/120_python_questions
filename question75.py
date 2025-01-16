def gcd(a, b):
    if b == 0:  # Base case
        return a
    return gcd(b, a % b)

# Example
a, b = 48, 18
print(f"GCD of {a} and {b}:", gcd(a, b))
