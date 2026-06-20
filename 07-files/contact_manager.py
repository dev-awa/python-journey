import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from JSON file. Return empty dict if file doesn't exist."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file) # Convert JSON to Python dict
    return {} # Return empty dict if file doesn't exist.

def save_contacts(contacts):
    """Save contacts dictionary to JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4) # Pretty print with 4 spaces
    
def main():
    # Load existing contacts at start
    phonebook = load_contacts()
    print("Phonebook loaded successfully!")
    
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add contact")
        print("2. Find contact")
        print("3. Delete contact")
        print("4. Show all contacts")
        print("5. Exit")
    
        choice = input("Choose (1-5): ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            phonebook[name] = phone
            save_contacts(phonebook) # Save after each change
            print(f"Contact '{name}' saved.")
        
        elif choice == "2":
            name = input("Enter name to search: ")
            if name in phonebook:
                print(f"{name}: {phonebook[name]}")
            else:
                print(f"'{name}' not found.")
            
        elif choice == "3":
            name = input("Enter name to delete: ")
            if name in phonebook:
                del phonebook[name] # Remove from dictionary
                save_contacts(phonebook)
                print(f"Contact '{name}' deleted.")
            else:
                print(f"'{name}' not found.")
        
        elif choice == "4":
            if not phonebook:
                print("Phonebook is empty.")
            else:
                print("\n--- All Contacts ---")
                for name, phone in phonebook.items():
                    print(f"{name}: {phone}")
                    
        elif choice == "5":
            print("Goodbye! Your contacts are saved.")
            break
        else:
            print("Invalid choice. Please enter 1-5.")
    
if __name__ == "__main__":
    main()