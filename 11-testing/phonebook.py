# Phonebook.py
class Phonebook:
    """ A simple phone book class with basic operation. """

    def __init__(self):
        """ Initialize an empty phonebook. """
        self.contacts = {}

    def add_contact(self, name, phone):
        """ Add a new contact or update existing one. """
        if not name or not phone:
            raise ValueError("Name and phone number cannot be empty")
        self.contacts[name] = phone
        return True
    
    def get_contact(self, name):
        """ Get phone number for a contact. Return None if not found. """
        return self.contacts.get(name)
    
    def delete_contact(self, name):
        """ Delete a contact. Return True if deleted, False if not found. """
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False
    
    def count_contacts(self):
        """ Return total number of contacts. """
        return len(self.contacts)