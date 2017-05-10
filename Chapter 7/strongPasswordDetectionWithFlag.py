import re

def is_strong(password):
    is_strong = True
    if re.compile(r'.{8,}').search(password) == None:
        is_strong = False
    elif re.compile(r'[a-z]+').search(password) == None:
        is_strong = False
    elif re.compile(r'[A-Z]+').search(password) == None:
        is_strong = False
    elif re.compile(r'\d+').search(password) == None:
        is_strong = False
    return is_strong

print(is_strong('ThisIsStr0ngPassword'))
print(is_strong('weakone'))