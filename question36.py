# Generate all prime numbers in a range
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
primes = [i for i in range(start, end + 1) if is_prime(i)]
print(f"Prime numbers in the range [{start}, {end}]: {primes}")
