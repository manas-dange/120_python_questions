#26
# Calculate the sum of digits of a number
num = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) for digit in str((num)))
print(f"The sum of digits of {num} is: {sum_of_digits}")