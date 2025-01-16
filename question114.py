import time

# List comprehension
start_time = time.time()
list_comprehension = [x * 2 for x in range(1000000)]
list_time = time.time() - start_time

# Generator expression
start_time = time.time()
generator_expression = (x * 2 for x in range(1000000))
generator_time = time.time() - start_time

print(f"List comprehension time: {list_time:.6f} seconds")
print(f"Generator expression time: {generator_time:.6f} seconds")
