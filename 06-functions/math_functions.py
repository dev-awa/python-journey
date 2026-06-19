def factorial(n):
    """Calculate factorial of a non-negative integer using recursion."""
    if n == 0 or n == 1: # Base case
        return 1
    else:
        return n * factorial(n - 1) # Recursive call

    
def fibonacci(n):
    """Generate Fibonacci sequence up to n terms using a loop."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n): # Start from 3rd term (index 2)
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence


def main():
    # Get user choice
    print("--- Math functions ---")
    print("1. Calculate factorial")
    print("2. Generate Fibonacci sequence")
    choice = input("Choose (1/2): ")
    
    if choice == "1":
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial(num)
            print(f"Factorial of {num} is: {result}")
        
    elif choice == "2":
        n = int(input("How many Fibonacci numbers to generate? "))
        result = fibonacci(n)
        if result:
            print(f"Fibonacci sequence ({n} terms): {result}")
        else:
            print("Please enter a positive number.")
    else:
        print("Invalid choice.")


# This ensures main() runs only when script is exeuted directly (not imported)
if __name__ == "__main__":
    main()