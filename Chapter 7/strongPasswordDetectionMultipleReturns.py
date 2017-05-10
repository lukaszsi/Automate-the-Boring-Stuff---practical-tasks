import re

def is_strong(password):
    if re.compile(r'.{8,}').search(password) == None:
        return False
    elif re.compile(r'[a-z]+').search(password) == None:
        return False
    elif re.compile(r'[A-Z]+').search(password) == None:
        return False
    elif re.compile(r'\d+').search(password) == None:
        return False
    else:
        return True

print(is_strong('ThisIsStr0ngPassword'))
print(is_strong('weakone'))