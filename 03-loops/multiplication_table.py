# Get a number from the user
number = int(input("Enter a number to see its multiplication table: "))

print(f"Multiplication table of {number}:")

# Use a for loop to iterate from 1 to 10
for i in range(1, 11): # range(1, 11) produces 1, 2, ..., 10
    result = number * i
    print(f"{number} x {i} = {result}")