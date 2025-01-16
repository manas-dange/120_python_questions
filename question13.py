#13
# Convert Celsius to Fahrenheit and vice versa
choice = input("Enter 'C' to convert to Celsius or 'F' to convert to Fahrenheit: ").strip().upper()

if choice == 'F':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F.")
elif choice == 'C':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C.")
else:
    print("Invalid choice!")
