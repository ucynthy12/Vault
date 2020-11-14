#!/usr/bin/env python3.6
from user import User
from credential import Credential
# from art import *
import random
import sys
# from simple_colors import *

def create_user(fname,lname,pswd,c_pswd):
    """
    Function to create a new user 
    """
    new_user= User(fname,lname,pswd,c_pswd)
    return new_user

def save_users(user):
    """
    Function to save user
    """
    user.save_user()

def create_account(ac_name,us_name,ac_pswd):
    """
    Function to create a new account
    """
    new_account= Credential(ac_name,us_name,ac_pswd)
    return new_account

def save_accounts(account):
    """
    Function to save account
    """
    account.save_account()

def delete_account(account):
    """
    Function to delete account
    """
    account.delete_account()

def find_account(account):
    """
    Function that finds an account name and returns the account
    """
    return Credential.find_by_account(account)

def check_existing_account(account):
    """
    Function that check if an account exists with that account name and return a Boolean
    """
    return Credential.account_exist(account)

def display_accounts():
    """
    Function that returns all the saved accounts
    """
    return Credential.display_accounts()

def generate_random_pswd():
    """
    Function to generate a random password
    """
    
    random= Credential.generate_random()
    return random
    



def main():
    # tprint("The Vault")
    # print(green('The Vault','bold'))
    print('\n')
    print("\u001b[34m"+"Hello Welcome to your password locker. What is your name?"+"\u001b[34m")
    print('\n')
    user_name=input()
    print('\n')
    print(f"Hello {user_name}. Fill in your information to create a password locker account.")
    print('\n')

    print('New Password')
    print("-"*15)

    print("First Name")
    f_name=input()
    print("Last Name")
    l_name=input()
    print("Enter password")
    passWord=input()
    print("Confirm password")
    cPassword=input()

    save_users(create_user(f_name,l_name,passWord,cPassword))
    print("\n")
    print(f"{f_name} Your new password locker was created")
    print("\n")
    print(f"Your new password -------- {passWord} ")

    print("\n")

    print("Please login with your first name ")
    login=input()
    print('\n')
    if login== f_name:


        while True:
            print("Use these short codes :")
            print('-'*25)
            print(" cp -----create a password \n dp -----display password \n fp -----find password \n dlt ----- delete password  \n ex ----- exit the account list")
            print('\n')
            short_code= input().lower()
            print('\n')

            if short_code == 'cp':
                print('New Credential')
                print('-'*15)

                print('Account name ')
                accountName=input()
                print('Username ')
                userName=input()
                print('\n')
                
                print("Use these short codes:")
                print('-'*30)
                print(" gp ---- generate your own password \n rp ---- generate random password ")

                short_codes= input().lower()
                print('\n')
                if short_codes == 'gp':

                    print('Password')
                    print('-'*10)
                    password=input()

                    save_accounts(create_account(accountName,userName,password))
                    print('\n')
                    print(f"{accountName}")
                    print("-"*15)
                    print(f"Username.... {userName}")
                    print(f"Your password.... {password}")
                    print('\n')
                
                elif short_codes == 'rp':
                    password=generate_random_pswd()
                    save_accounts(create_account(accountName,userName,password))
                    print('\n')
                    print(f"{accountName}")
                    print("-"*15)
                    print(f"Username.... {userName}")
                    print(f"Your password.... {password}")
                    print('\n')

                else:
                    print("I didn't get that. Please choose the right code!")

            elif short_code == "dp":

                if display_accounts():
                    print("\n")
                    print ('Here is a list of all passwords:')
                    print('-'*40)

                    for accounts in display_accounts():
                        print(f"{accounts.acc_name}----{accounts.username}----{accounts.acc_pswd}")

                    print('\n')

                else:
                    print('\n')
                    print("You don't seem to have any password saved")
                    print('\n')
        
            elif short_code == "fp":
                print('\n')
                print("Enter the account name you want to search for")

                search_account= input()

                if check_existing_account(search_account):
                    search_account= find_account(search_account)
                    print('\n')
                    print(f"{search_account.acc_name}")
                    print("-"*10)
                    print(f"Username.....{search_account.username}")
                    print(f"Password.....{search_account.acc_pswd}")
                    print('\n')
                else:
                    print("That password doesn't exist")
                    print('\n')
            
            elif short_code == "dlt":
                print('\n')
                print('Please enter account name you wish to delete')
                print('\n')

                dlt_account=input()

                if find_account(dlt_account):
                    search_account= find_account(dlt_account)
                    print("-"*20)

                    search_account.delete_account()
                    print('\n')
                    print(f"Your password for : {search_account.acc_name} was successfully deleted!")
                    print('\n')
            
                else:
                    print('this password does not exist in your Vault')
        
        
                
        
            elif short_code =='ex':
                print('\n')
                print('Thank You for using The Vault')
                print('\n')
                print('Bye .....')
                break
            else:
                print("I really didn't get that. Try again")
                print('\n')

    else:
        print("Your first name doesn't match")   



if __name__ == '__main__':

    main()