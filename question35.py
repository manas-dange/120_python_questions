# Calculate the sum of the series 1 + 1/2 + ... + 1/n
n = int(input("Enter a positive integer n: "))
series_sum = sum(1 / i for i in range(1, n + 1))
print(f"The sum of the series is: {series_sum}")
