import pyperclip
import random


class Credential:
    """
    class that generates new instances of accounts
    """
    account_list = []

    def __init__(self, acc_name, username, acc_pswd):
        """
        Args:
            acc_name:first name on your account
            user_name:user name on your account
            password: new password generated for that account
        """
        self.acc_name = acc_name
        self.username = username
        self.acc_pswd = acc_pswd

    def save_account(self):
        """
        save account method saves oblects in account_list
        """
        Credential.account_list.append(self)

    def delete_account(self):
        """
        delete_account method deletes a saves account from the account_list
        """
        Credential.account_list.remove(self)

    @classmethod
    def find_by_account(cls, accounts):
        """
        Method that takes in account name and returns the username and password of that account

        Args:
            account: account name to search for
        Returns:
            Account of user that matches the account
        """

        for name in cls.account_list:
            if name.acc_name == accounts:
                return name

    @classmethod
    def account_exist(cls, account):
        """
        Method that checks if an account exists from the account list.
        Args:
            account:account name to search if exists
        Return:
            Boolean: True or false depending if the account exists
        """
        for name in cls.account_list:
            if name.acc_name == account:
                return True

        return False

    @classmethod
    def display_accounts(cls):
        """
        Method that returns the account list
        """
        return cls.account_list

    def generate_random():
        """
        Methods that returns a random password 
        """
        characters = 'abcdefghijklmnopqrstuvwxz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*'
        length=int(input('Enter the length of your password '))
        password_characters=[random.choice(characters) for x in range (length)]
        password= "".join(password_characters)
        
        return password

    @classmethod
    def copy_password(cls,account):
        account_found= Credential.find_by_account(account)
        pyperclip.copy(account_found.password)
