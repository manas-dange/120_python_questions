#17
num = int(input("enter number"))
factorial = 1
if num>=0:
    for i in range(1, num+1):
        factorial = factorial * i
    print(factorial)
else:
    print("factorial cannot be calculated for negative numbers")