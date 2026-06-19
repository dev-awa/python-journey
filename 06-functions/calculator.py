def add(a, b):
    """Return sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return difference of two  numbers (a - b)."""
    return a - b


def multiply(a, b):
    """Return product of two numbers."""
    return a * b


def divide(a, b):
    """Return quotient of a divided by b. Handle division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b


def get_number(prompt):
    """Helper function to get a float number from user with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            

def main():
    print("--- Simple Calculator ---")
    print("Avilable operations: +, -, *, /")
    
    # Get inputs
    num1 = get_number("Enter first number: ")
    operator = input("Enter operation (+, -, *, /): ")
    num2 = get_number("Enter second number: ")
    
    # Perform calculation based on operator
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    else:
        result = "Invalid operator"
        
    # Display result
    print(f"Result: {num1} {operator} {num2} = {result}")
    
    
if __name__ == "__main__":
    main()