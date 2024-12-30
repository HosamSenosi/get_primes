import numpy as np
import math
import time
from functools import wraps

# Timing decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {(end_time - start_time):.6f} seconds")
        return result
    return wrapper

# previous implementation
@timer
def get_primes_previous(n_min, n_max):
    result = []
    for x in range(max(n_min, 2), n_max):
        has_factor = False
        for p in range(2, int(np.sqrt(x)) + 1):
            if x % p == 0:
                has_factor = True
                break
        if not has_factor:
            result.append(x)
    return result

# New implementation
@timer
def get_primes_sieve(n_min: int, n_max: int) -> list[int]:
    if n_max < 2:
        return []
    
    # Initialize the sieve
    sieve = [True] * (n_max + 1)
    sieve[0] = sieve[1] = False
    
    # Mark non-prime numbers in the sieve
    for i in range(2, int(n_max ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i:n_max + 1:i] = [False] * len(sieve[i * i:n_max + 1:i])
    
    # Generate result list based on n_min
    return [num for num in range(max(2, n_min), n_max + 1) if sieve[num]]

# Let's test with different ranges
def compare_implementations(ranges):
    print("\nPerformance Comparison:")
    print("-" * 50)
    
    for n_min, n_max in ranges:
        print(f"\nTesting range: {n_min} to {n_max}")
        
        # Run both implementations
        result1 = get_primes_previous(n_min, n_max)
        result2 = get_primes_sieve(n_min, n_max)
        
        # Verify results match -- Unnecessary
        print(f"Results match: {result1 == result2}")

        print(f"Number of primes found: {len(result1)}")



if __name__ == "__main__":
    n_min = input("Enter the lower bound of the range: ")
    n_max = input("Enter the upper bound of the range: ")
    if n_min.isnumeric() and n_max.isnumeric() and int(n_min)<int(n_max):
        print("Invalid range. The lower bound must be less than or equal to the upper bound.")
    else:
        compare_implementations([(n_min, n_max)])


# # Test with different ranges
# test_ranges = [
#     (1000000,10000000)
# ]
# compare_implementations(test_ranges)