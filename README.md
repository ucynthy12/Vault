# The Vault


## Author  
Cynthia Umutoniwabo
## Description 
This is an amazing application that will help us manage our passwords and even generate new passwords for us.

## Technology Used  
1.Python3.6  
2.Pyperclip  
3.Pip

## BDD
| Behaviour            | Input                            | Output                                 |
|----------------------|----------------------------------|----------------------------------------|
|Open Terminal          | Run $./run.py   | Hello Welcome to the Vault your password locker. What is your name?           |
| welcome message           | Enter name  | Hello Name, Fill in your information to create a password locker account.     |
| Enter information    | Enter  first name,last name, password and confirm password       | <NAME> your password locker account was created succesfully. your password is  <password> |
| logging in your vault account| use your password  | enter your account. Use these short codes |
| logging in your vault account| wrong password |exit application|
| choose cp to create a password|Enter Credential  | use the short codes to generate your code or random code |
| generate password|choose gp  and enter your own password | Password succefully generated with account name,username and password |
| generate password |choose rp | Password succefully generated with account name, username and random password |
| Display passwords|choose dp  | all the account with their respective information display |
| Display passwords|choose dp with no password in the vault |you seem to not have any password saved |
|Find password|choose fp and enter an account you wish to search | account you searched display with all the information |
|Find password|choose fp and enter an wrong account | The password for this account doesn't exist in your vault |
| Delete password|choose dlt and enter an account you wish to delete  | The account with the password is deleted succesfully|
| Delete password|choose dlt and enter wrong account to delete  | This password does not exist in your Vault|
| Exit the application|choose  ex | Thank you for using the vault. Bye .. |
| Mistake on short code| wrong short code entered  |I really didn't get that. Try again|


### Known Bugs
There are no known bugs currently 

### Support and Contact details
For more contribution on my application, please fork and send some request.

1.Email: ucynthy12@gmail.com  
2.Github   
  .username: ucynthy12  
  .name: Cynthia Umutoniwabo  

### License
Copyright (c) [2020] [Cynthia Umutoniwabo]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



