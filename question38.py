# Print a diamond-shaped pattern of stars
n = int(input("Enter the width (odd number): "))
for i in range(1, n + 1, 2):
    print(" " * ((n - i) // 2) + "*" * i)
for i in range(n - 2, 0, -2):
    print(" " * ((n - i) // 2) + "*" * i)
