def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

# Example
base = 2
exp = 3
print(f"{base}^{exp}:", power(base, exp))
