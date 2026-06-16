import random # Import random module to generate random numbers

# Generate a random number between  1 and 10
secret_number = random.randint(1, 10)
max_attempts = 3
attempts = 0

print("I'm thinking of a number between 1 and 10. You have 3 tries.")

# Loop runs as long as attempts are less than max_attempts
while attempts < max_attempts:
    # Get user's guess and convert to integer
    guess = int(input("Enter your guess: "))
    attempts += 1 # Increase attempt counter
    
    # Check if the guess is correct
    if guess == secret_number:
        print(f"Correct! The number was {secret_number}. You won in {attempts} tries.")
        break # Exit the loop if guessed correctly
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    
# This runs if the loop ends without a break (i.e., attempts exhausted)
else:
    print(f"Sorry, you lost. The number was {secret_number}.")