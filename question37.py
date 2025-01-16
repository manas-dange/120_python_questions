# Display the Collatz sequence
def collatz_sequence(num):
    while num != 1:
        print(num, end=" -> ")
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
    print(1)

number = int(input("Enter a positive integer: "))
collatz_sequence(number)
