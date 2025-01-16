#23
# Reverse the digits of a number
num = int(input("Enter an integer: "))
reversed_num = int(str((num))[::-1]) * (-1 if num < 0 else 1)
print(f"The reversed number is: {reversed_num}")