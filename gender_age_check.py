# Get age and gender from user
age = int(input("Enter your age: "))
# Convert gender input to uppercase to handle 'm' or 'f'
gender = input("Enter your gender (M/F): ").upper()

# Check special retirement eligibility
if age >= 60 and gender == "F":
    # Female aged 60 or older
    status = "Eligible for special retirement (women)"
elif age >= 65 and gender == "M":
    # Male aged 65 or older
    status = "Eligible for regular retirement (men)"
else:
    # Any other case
    status = "Not yet eligible for retirement"

print(f"Status: {status}")