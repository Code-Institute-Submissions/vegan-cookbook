import unittest, json
from types import IntType

class UsernameTests(unittest.TestCase):

    def test_username_empty(self):
        """
        Asserts if a username is empty
        """
        result = check_username(, "")
        self.assertFalse(result, "Empty username was not marked as empty")
        
    
    def test_username_taken(self):
        """
        Asserts that a known taken username is checked as invalid
        """
        result = check_username(, "Annie")
        self.assertFalse(result, "Taken username was not marked as taken")


if __name__ == '__main__':
    unittest.main()