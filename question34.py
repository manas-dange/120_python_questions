# Check if a 3-digit number is an Armstrong number
def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    return num == sum(d ** 3 for d in digits)

number = int(input("Enter a 3-digit number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
