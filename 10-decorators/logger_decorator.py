import datetime

def logger(filename="log.txt"):
    """
    Decorator factory that logs function calls to a file.
    Args:
        filename: Name of the log file (default: log.txt)
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Get current timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Format arguments for logging
            args_str = ", ".join(str(arg) for arg in args)
            kwargs_str = ", ".join(f"{key}={value}" for key, value in kwargs.items())
            
            # Combine arguments
            all_args = args_str
            if kwargs_str:
                all_args += f" (kwargs: {kwargs_str})"
                
            # Log the call
            log_entry = f"[{timestamp}] Function {func.__name__}' called with args: {all_args}\n"
            with open(filename, 'a') as log_file: # 'a' for append
                log_file.write(log_entry)
                
            # Call the original function and get result
            result = func(*args, **kwargs)
            
            # Log the result
            result_entry = f"[{timestamp}] '{func.__name__}' returned: {result}\n"
            with open(filename, 'a') as log_file:
                log_file.write(result_entry)
            
            return result
        return wrapper
    return decorator

# Create a logger with a specific file
@logger("Calculator_log.txt")
def add(a, b):
    """ Add two numbers. """
    return a + b

@logger("Calculator_log.txt")
def multiply(a, b):
    """ Multiply two numbers. """
    return a * b

@logger("Calculator_log.txt")
def divide(a, b):
    """ Divide a by b. Handle division by zero. """
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    print("--- Logger Decorator Demo ---")
    print("All function calls will be logged to 'calculator_log.txt'")
    
    # Call functions
    add(5, 3)
    multiply(4, 7)
    divide(10, 2)
    divide(8, 0) # This will log the error message
    
    print("Logging complete. Check 'calculator_log.txt'")
    
    # Display log content
    try:
        with open("calculator_log.txt", 'r') as f:
            print("\n Log content: ")
            print("=" * 50)
            print(f.read())
    except FileExistsError:
        print("No log file found.")

if __name__ == "__main__":
    main()