import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps creatin test cases
    """

    def setUp(self):
        """
        Set up method to run before each test cases 
        """
        self.new_user= User("Cynthia","Umutoniwabo","1989","1989")

    def test_init(self):
        """
        test_init test case to test if the object is initializes properly
        """
        self.assertEqual(self.new_user.first_name,"Cynthia")
        self.assertEqual(self.new_user.last_name,"Umutoniwabo")
        self.assertEqual(self.new_user.password,"1989")
        self.assertEqual(self.new_user.conf_password,"1989")

if __name__ == '__main__':
    unittest.main()
