def get_number(prompt):
    """Get a valid float number from user with error handling."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number (e.g., 5 or 3.14).")
        
def divide(a, b):
    """Divide a by b, handling division by zero!"""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    
def main():
    print("--- Robust Calculator ---")
    print("Supported operations: +, -, *, /")
    
    # Get first number (always valid)
    num1 = get_number("Enter first number: ")

    # Get operator with validation
    operators = ['+', '-', '*', '/']
    while True:
        operator = input("Enter operation (+, -, *, /): ").strip()
        if operator in operators:
            break
        print("Invalid operator! Please choose one of: +, -, *, /")
        
    # Get second number (always valid)
    num2 = get_number("Enter second number: ")

    # Perform calculation with error handling
    try:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = divide(num1, num2) # This function handles division by zero
            
        # Check if result is an error message (string)
        if isinstance(result, str):
            print(f"{result}")
        else:
            print(f"Result: {num1} {operator} {num2} = {result}")
        
    except Exception as e:
        # Catch any unexpected error (safety net)
        print(f"An unexpected error occured: {e}")
        
    finally:
        print("Calculation complete. Thank you for using the calculator!")

if __name__ == "__main__":
    main()