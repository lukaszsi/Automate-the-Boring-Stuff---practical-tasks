#! python3
import re

def password_check(password):
    hasError = False
    if re.compile(r'.{8,}').search(password) == None:
        print('Password is not long enough!')
        hasError = True
    if re.compile(r'[a-z]+').search(password) == None:
        print('Password has no lowercase characters!')
        hasError = True
    if re.compile(r'[A-Z]+').search(password) == None:
        print('Password has no uppercase characters!')
        hasError = True
    if re.compile(r'\d+').search(password) == None:
        print('Password has no digits!')
        hasError = True
    if hasError == False:
        print('Password is strong enough!')
