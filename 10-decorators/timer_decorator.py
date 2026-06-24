import time

def timer(func):
    """
    Decorator that measures the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time() # Start timer
        result = func(*args, **kwargs) # Call the original function
        end_time = time.time() # End timer
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds")
        return result
    return wrapper

# Apply the decorator using @ syntax
@timer
def slow_function():
    """ A function that simulates a slow operation. """
    print("Running slow operation...")
    time.sleep(2) # Simulate a slow operation (2 seconds)
    print("Operation complete.")
    return "Result of slow function."

@timer
def fast_function(n):
    """ A function that calculates sum of numbers quickly. """
    total = sum(range(n))
    print(f"Sum of numbers up to {n}: {total}")
    return total

def main():
    print("--- Timer Decorator Demo ---")
    
    # Call the decorated functions
    slow_function()

    print("\n" + "-" * 40)

    fast_function(1000000) # Sum of 1 to 1,000,000
    
if __name__ == "__main__":
    main()