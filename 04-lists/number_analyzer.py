# Create an empty list to store numbers
numbers = []

# Get 5 numbers from user
for i in range(1, 6): # Loop 5 items
    num = float(input(f"Enter number {i}: "))
    numbers.append(num) # Add to list

# Calculate results using list functions
total = sum(numbers) # Sum of all numbers
maximum = max(numbers) # Maximum value
minimum = min(numbers) # Minimum value
average = total / len(numbers) # Average

# Display results
print("\n--- Results ---")
print(f"Numbers entered: {numbers}")
print(f"Sum: {total}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")