# Get user's age and convert to integer
age = int(input("Please enter your age: "))

# Classify age group using if/elif/else
if age < 18:
    # Under 18
    category = "Teenager"
elif 18 <= age < 65:
    # Between 18 and 64 (inclusive 18)
    category = "Adult"
else:
    # 65 or older
    category = "Senior"

# Print result using f-string
print(f"You are categorized as: {category}")