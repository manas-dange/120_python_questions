import multiprocessing

def square_number(n):
    return n * n

# Use multiprocessing to calculate squares in parallel
if __name__ == "__main__":
    with multiprocessing.Pool(4) as pool:
        results = pool.map(square_number, [1, 2, 3, 4, 5])
    
    print("Squared numbers:", results)
