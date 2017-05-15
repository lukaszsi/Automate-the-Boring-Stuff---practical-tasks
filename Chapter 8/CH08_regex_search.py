#! python3
'''Program that opens all .txt files in a folder and searches
for any line that matches a user-supplied regular expression.
The results are printed to the screen.'''

import re
import os

# User gives the path to the folder.
directory = input('Give full path to folder: ')
# User provides regular expression.
expr_search = input('What do you want to search for in files: ')
# For files in folder open .txt file and search for regular expression.
def regex_search(folder_path, expression):
    for file in os.listdir(folder_path):
        if file.endswith('txt'):
            check_file = open(os.path.join(folder_path, file))
            file_content = check_file.read()
# prints result to the screen for each file
            mo = re.compile(r''+expression).search(file_content)
            if mo != None:
                print('Found in '+file+': '+mo.group())

regex_search(directory, expr_search)
