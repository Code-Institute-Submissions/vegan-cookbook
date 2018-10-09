import unittest, json
from utils import check_recipename


class RecipenameTests(unittest.TestCase):
    '''
    Asserts the Recipe Name field was left empty
    '''
    def test_is_empty_recipename(self):
        self.assertFalse(
            check_recipename(""), 
            "Invalid Recipe Name was incorrectly marked as valid")

    '''
    Asserts the Recipe Name field was left empty
    '''
    def test_is_valid_recipename(self):
        self.assertTrue(
            check_recipename("banana"), 
            "Valid Recipe Name was incorrectly marked as invalid")

    
if __name__ == '__main__':
    unittest.main()