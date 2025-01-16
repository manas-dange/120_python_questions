while True:
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        print(f"Valid number entered: {number}")
        break
    except ValueError:
        print("Invalid input, please enter a valid number.")
