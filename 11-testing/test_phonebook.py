import unittest
from phonebook import Phonebook

class TestPhonebook(unittest.TestCase):
    """ Test cases for Phonebook class. """

    def setUp(self):
        """ Set up a fresh phonebook before each test. """
        self.pb = Phonebook()
        self.pb.add_contact("Alice", "123-4567")
        self.pb.add_contact("Bob", "234-5678")
        
    def test_add_contact(self):
        """ Test adding a new contact. """
        result = self.pb.add_contact("Charlie", "345-6789")
        self.assertTrue(result)
        self.assertEqual(self.pb.get_contact("Charlie"), "345-6789")
        self.assertEqual(self.pb.count_contacts(), 3)
        
    def test_add_contact_with_empty_name(self):
        """ Test adding contact with empty name raises ValueError. """
        with self.assertRaises(ValueError):
            self.pb.add_contact("", "123-4567")
        
    def test_add_contact_with_empty_phone(self):
        """ Test adding contact with empty phone raises ValueError. """
        with self.assertRaises(ValueError):
            self.pb.add_contact("Charlie", "")
            
    def test_get_contact(self):
        """ Test getting a contact by name. """
        self.assertEqual(self.pb.get_contact("Alice"), "123-4567")
        self.assertEqual(self.pb.get_contact("Bob"), "234-5678")
        self.assertIsNone(self.pb.get_contact("Unknown"))
        
    def test_delete_contact(self):
        """ Test deleting a contact. """
        self.assertTrue(self.pb.delete_contact("Alice"))
        self.assertIsNone(self.pb.get_contact("Alice"))
        self.assertEqual(self.pb.count_contacts(), 1)
        
    def test_delete_nonexistent_contact(self):
        """ Test deleting a contact that doesn't exist. """
        self.assertFalse(self.pb.delete_contact("Unknown"))
        self.assertEqual(self.pb.count_contacts(), 2)
        
    def test_count_contacts(self):
        """ Test counting contacts. """
        self.assertEqual(self.pb.count_contacts(), 2)
        self.pb.add_contact("Charlie", "345-6789")
        self.assertEqual(self.pb.count_contacts(), 3)
    
if __name__ == "__main__":
    unittest.main()