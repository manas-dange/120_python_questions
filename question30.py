#30
# Check if a number is a perfect number
num = int(input("Enter a number: "))
divisors = [i for i in range(1, num) if num % i == 0]
if sum(divisors) == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")