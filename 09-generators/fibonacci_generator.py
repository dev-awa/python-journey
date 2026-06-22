def fibonacci_generator():
    """
    Generator that produces Fibonacci numbers infinitely.
    Yields: next Fibonacci number
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b # Update values for next iteration
        
def main():
    print("--- Fibonacci Generator ---")

    try:
        n = int(input("How many Fibonacci numbers to generate? "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return
    
    if n <= 0:
        print("Please enter a positive number.")
        return
    
    print(f"\n First {n} Fibonacci numbers: ")
    print("=" * 40)
    
    # Create generator object
    fib = fibonacci_generator()

    # Generate and display n numbers
    for i in range(n):
        number = next(fib) # Get next value from generator
        print(f"{i+1}: {number}")
        
    print("=" * 40)
    
    # Demonstrate that generator can continue
    if n > 0:
        print(f"\n The generator can continue. Next number would be: {next(fib)}")

if __name__ == "__main__":
    main()