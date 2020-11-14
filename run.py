#!/usr/bin/env python3.6
from user import User
from credential import Credential
from art import *
import random
import sys
from simple_colors import *

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
    tprint("The Vault")
    # print(green('The Vault','bold'))
    print('\n')
    # print("\u001b[34m"+"Hello Welcome to your password locker.\n What is your name?"+"\u001b[34m")
    print(blue('Hello Welcome to')+ green(' The Vault','bold')+ blue(' your password locker.'))
    print(blue('What is your name?'))
    user_name=input()
    print('\n')
    print(blue(f"Hello {user_name}, Fill in your information to create a password locker account."))
    print('\n')

    print(blue('New Password'))
    print(blue("-"*15))

    print(blue("First Name"))
    f_name=input()
    print(blue("Last Name"))
    l_name=input()
    print(blue("Enter password"))
    passWord=input()
    print(blue("Confirm password"))
    cPassword=input()

    save_users(create_user(f_name,l_name,passWord,cPassword))
    print("\n")
    print(green(f"{f_name}","bright")+ blue(" Your new password locker was created succesfully!Your new password is ")+green(f'{passWord}','bold'))
    print('-'*85)
    print("\n")

    print(blue("Please login with your password "))
    login=input()
    print('\n')
    if login== passWord:


        while True:
            print(blue("Use these short codes :","underlined"))
            print(blue(" cp -----create a password \n dp -----display password \n fp -----find password \n dlt ----- delete password  \n ex ----- exit the account list"))
            print('\n')
            short_code= input().lower()
            print('\n')

            if short_code == 'cp':
                print(blue('New Credential','underlined'))
                # print('-'*15)

                print(blue('Account name '))
                accountName=input()
                print(blue('Username '))
                userName=input()
                print('\n')
                
                print(blue("Use these short codes:","underlined"))
                print(blue(" gp ---- generate your own password \n rp ---- generate random password "))

                short_codes= input().lower()
                print('\n')
                if short_codes == 'gp':

                    print(blue('Password','underlined'))

                    password=input()

                    save_accounts(create_account(accountName,userName,password))
                    print('\n')
                    print(blue(f"{accountName}",["bold","underlined"]))

                    print(blue("Username is ")+ green(f'{userName}','bright'))
                    print(blue("Your password is ")+ green(f'{password}','bright'))
                    print('\n')
                
                elif short_codes == 'rp':
                    password=generate_random_pswd()
                    save_accounts(create_account(accountName,userName,password))
                    print('\n')
                    print(blue(f"{accountName}",['bold','underlined']))
                    print(blue("Username is ")+ green(f'{userName}','bright'))
                    print(blue("Your password is ")+ green(f'{password}','bright'))
                    print('\n')

                else:
                    print(blue("I didn't get that. Please choose the right code!"))

            elif short_code == "dp":

                if display_accounts():
                    print("\n")
                    print (blue('Here is a list of all passwords:','underlined'))
                    

                    for accounts in display_accounts():
                        print(green(f"{accounts.acc_name}","bold")+"----"+ green(f"{accounts.username}","italic")+"----"+green(f"{accounts.acc_pswd}","bright"))

                    print('\n')

                else:
                    print('\n')
                    print(blue("You don't seem to have any password saved"))
                    print('\n')
        
            elif short_code == "fp":
                print('\n')
                print(blue("Enter the account name you want to search for","blink"))

                search_account= input()

                if check_existing_account(search_account):
                    search_account= find_account(search_account)
                    print('\n')
                    print(blue(f"{search_account.acc_name}","underlined"))
                    print(blue("Username is ")+ green(f"{search_account.username}","bright"))
                    print(blue("Password is ")+ green(f"{search_account.acc_pswd}","bright"))
                    print('\n')
                else:
                    print(blue("The password for this account doesn't exist in your vault"))
                    print('\n')
            
            elif short_code == "dlt":
                print('\n')
                print(blue('Please enter account name you wish to delete'))
                print('\n')

                dlt_account=input()

                if find_account(dlt_account):
                    search_account= find_account(dlt_account)
                    print("-"*20)

                    search_account.delete_account()
                    print('\n')
                    print(blue("Your password for :")+green(f'{search_account.acc_name}','bold')+blue(" was successfully deleted!"))
                    print('\n')
            
                else:
                    print(blue('This password does not exist in your Vault'))
        
        
                
        
            elif short_code =='ex':
                print('\n')
                print(blue('Thank You for using The Vault','bold'))
                print('\n')
                print(blue('Bye .....','bold'))
                break
            else:
                print(blue("I really didn't get that. Try again"))
                print('\n')

    else:
        print(blue("Your password doesn't match"))   



if __name__ == '__main__':

    main()