def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# Example
n = 7
print(f"{n}th Fibonacci number:", fib(n))
