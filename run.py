#!/usr/bin/env python3.6
from user import User
from credential import Credential
from art import *

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
    user.save_users()

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
    account.save_accounts()

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
