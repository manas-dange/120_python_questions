#22
# Print the first n numbers of the Fibonacci sequence
n = int(input("Enter the number of Fibonacci numbers to print: "))
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b