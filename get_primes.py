import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{'-'*15} \n {func.__name__} took {(end_time - start_time):.6f} seconds \n {'-'*15}")
        return result
    return wrapper


@timer
def get_primes(n_min: int, n_max: int, show_progress: bool = True) -> list[int]:
    """
    Generate prime numbers between n_min and n_max using the Sieve of Eratosthenes algorithm.
    
    Args:
        n_min (int): Lower bound of the range (inclusive)
        n_max (int): Upper bound of the range (inclusive)
        show_progress (bool): Whether to show the loading progress
    
    Returns:
        list[int]: List of prime numbers in the specified range
    """    
    if n_max < 2:
        return []
    
    # Initialize the sieve
    sieve = [True] * (n_max + 1)
    sieve[0] = sieve[1] = False
    
    # Calculate total iterations for progress tracking
    total_steps = int(n_max ** 0.5) - 1
    current_step = 0
    
    # Mark non-prime numbers in the sieve
    for i in range(2, int(n_max ** 0.5) + 1):
        if sieve[i]:
            # Mark multiples of i as non-prime
            sieve[i * i:n_max + 1:i] = [False] * len(sieve[i * i:n_max + 1:i])
        
        # Update progress
        if show_progress:
            current_step += 1
            progress = (current_step / total_steps) * 100
            print(f"\rGenerating primes... {progress:.1f}%", end="", flush=True)
    
    # Clear the loading message
    if show_progress:
        print("\rGenerating primes... Done!")
    
    # Generate result list based on n_min
    return [num for num in range(max(2, n_min), n_max + 1) if sieve[num]]


if __name__ == "__main__":
    n_min=input("Enter the lower bound of the range: ")
    n_max=input("Enter the upper bound of the range: ")
    if n_min.isnumeric() and n_max.isnumeric() and int(n_min)<int(n_max):
        primes = get_primes(int(n_min),int(n_max))
        len_primes=len(primes)
        print(f"There are {len_primes} primes between {n_min} and {n_max} \n ")
        if len_primes > 100:
            with open(f'primes_from_{n_min}_to_{n_max}.txt', 'w') as f:
                f.write(f"There are {len_primes} primes between {n_min} and {n_max} \n Primes:\n")
                for prime in primes:
                    f.write(str(prime) + "\n")
            print(f"Results saved to primes_from_{n_min}_to_{n_max}.txt file")
        else:
            print("Primes:\n",primes)
    else:
        print("Invalid input. Please enter valid integers.")