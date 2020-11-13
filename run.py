#!/usr/bin/env python3.6
from user import User
from credential import Credential
from art import *

def create_user(fname,lname,pswd,c_pswd):
    """
    Function to creat a new user 
    """
    new_user= User(fname,lname,pswd,c_pswd)
    return new_user

def save_users(user):
    """
    Function to save user
    """
    user.save_users()