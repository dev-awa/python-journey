def say_hello(name: str) -> str:
    """Returns a personalized greeting."""
    return f"Hello, {name}! Welcome to Python."

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(say_hello(user))