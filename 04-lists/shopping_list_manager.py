# Initialize empty shopping list
shopping_list = []

# Show menu until user chooses to exit
while True:
    print("\n--- Shopping List Manager ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        # Add item
        item = input("Enter item name: ")
        shopping_list.append(item) # Add  to end of list
        print(f"'{item}' added to list.")
        
    elif choice == "2":
        # Remove item
        item = input("Enter item name to remove: ")
        if item in shopping_list: # Check if item exists
            shopping_list.remove(item) # Remove the item
            print(f"'{item}' removed from list.")
        else:
            print(f"'{item}' not found in list.")

    elif choice == "3":
        # View list
        if len(shopping_list) == 0: # Check if list is empty
            print("Your shopping list is empty.")
        else:
            print("Your shopping list: ")
            for idx, item in enumerate(shopping_list, start=1): # Show with numbers
                print(f"{idx}. {item}")
    
    elif choice == "4":
        # Exit loop
        print("Goodbye!")
        break # Exit the while loop
    
    else:
        print("Invalid choice. Please enter 1-4.")