import unittest
from credential import Credential
import pyperclip
class TestAccount(unittest.TestCase):
    """
    Test class that defines test cases for credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps creating test cases
    """
    def setUp(self):
        """
        Set up method to run before each test cases 
        """
        self.new_account= Credential("Twitter","ucynthy12","zion")
    
    def test_init(self):
        """
        test_init test case to test if the object is initializes properly
        """
        self.assertEqual(self.new_account.acc_name,"Twitter")
        self.assertEqual(self.new_account.username,"ucynthy12")
        self.assertEqual(self.new_account.acc_pswd,"zion")
   
    def test_save_account(self):
        """
        test_save_account test case to test if the account object is saved in the account list
        """
        self.new_account.save_account()
        self.assertEqual(len(Credential.account_list),1)
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.account_list = []

    def test_save_multiple_account(self):
        """
        test_save_multiple_account test case to test if you can save multiple accounts in account list
        """
        self.new_account.save_account()
        test_account= Credential("Github","ucynthy12","iliza")
        test_account.save_account()
        self.assertEqual(len(Credential.account_list),2)
    
    def test_delete_accounr(self):
        """
        test_delete_account to test if we can remove an account from our account_list
        """
        self.new_account.save_account()
        test_account= Credential("Github","ucynthy12","iliza")
        test_account.save_account()

        self.new_account.delete_account()
        self.assertEqual(len(Credential.account_list),1)
    
    def test_find_account_by_name(self):
        """
        test to check if we can find an account and display the username and password of that account
        """

        self.new_account.save_account()
        test_account= Credential("Github","ucynthy12","iliza")
        test_account.save_account()

        found_account= Credential.find_by_account("Github")

        self.assertEqual(found_account.username,test_account.username)

    def test_account_exists(self):
        """
        test to check if we can return a Boolean if we cannot find the account.
        """

        self.new_account.save_account()
        test_account= Credential("Instagram","ucynthy12","irebe")
        test_account.save_account()
        account_exists=Credential.account_exist("Instagram")
        self.assertTrue(account_exists)
    
    def test_display_all_accounts(self):
        """
        Method that returns a list of all accounts saved
        """
        self.assertEqual(Credential.display_accounts(),Credential.account_list)

    def test_copy_password(self):
        """
        Method that test if password was copied on clipboard
        """
        self.new_account.save_account() 
        Credential.copy_password('Twitter')
        self.assertEqual(self.new_account.acc_pswd,pyperclip.paste())

    def test_random_password(self):
        """
        Method that returns random password
        """
        random=Credential.generate_random()
        self.assertTrue(random)

        
if __name__ == '__main__':
    unittest.main()