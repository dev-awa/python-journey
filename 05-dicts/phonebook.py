# Initialize empty phonebook dictionary
phonebook = {}

while True:
    print("\n--- Phonebook Menu ---")
    print("1. Add contact")
    print("2. Find contact")
    print("3. Delete contact")
    print("4. Show all contacts")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        # Add or update a contact
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        phonebook[name] = phone # Add or update the key
        print(f"Contact '{name}' saved successfully.")

    elif choice == "2":
        # Find a contact by name
        name = input("Enter name to search: ")
        if name in phonebook: # Check if key exists
            print(f"{name}'s number: {phonebook[name]}")
        else:
            print(f"Contact '{name}' not found.")

    elif choice == "3":
        # Delete a contact
        name = input("Enter name to delete: ")
        if name in phonebook:
            removed_phone = phonebook.pop(name) # Remove and get the value
            print(f"Contact '{name}' (number {removed_phone}) deleted.")
        else:
            print(f"Contact '{name}' not found.")
            
    elif choice == "4":
        # Show all contacts
        if len(phonebook) == 0:
            print("Phonebook is empty.")
        else:
            print("\n--- All Contacts ---")
            for name, phone in phonebook.items(): # Iterate over key-value pairs
                print(f"{name}: {phone}")
        
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-5.")