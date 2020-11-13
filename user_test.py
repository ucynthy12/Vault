import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps creating test cases
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
    
    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved in the user list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)



if __name__ == '__main__':
    unittest.main()
