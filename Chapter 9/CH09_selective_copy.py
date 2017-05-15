#! python3
''' Script that walks through a folder tree and searches
for files with a certain file extension and copies these
files to a new folder in cwd. '''
import os
import shutil

def walk_and_copy(extension, search_path, copy_path):
    os.makedirs(copy_path)
# program walks through a folder tree that was given and searches for .jpg file
    for folder_name, subfolders, filenames in os.walk(search_path):
        for filename in filenames:
            if filename.endswith(extension):
                # program copies these files to a new folder in cwd
                print(os.path.join(folder_name,filename)+' was copied to '+copy_path)
                shutil.copy(os.path.join(folder_name,filename), copy_path)                

# Program asks about certain file extension to look for (for example '.jpg'),
#  path to search and to copy files to.
extension = input("What file extention to look for? (example: '.jpg'. Hit enter to use example): ")
if extension == '':
    extension = '.jpg'
# program asks about path to walk through
search_path = input("What is the path to look in? (example: 'F:\\bacon'. Hit enter to use example): ")
if search_path == '':
    search_path = 'F:\\bacon'
# program asks about path to copy files
copy_path = input("What is the path to copy files to? (example: 'F:\\copy'. Hit enter to use example): ")
if copy_path == '':
    copy_path = 'F:\\copy'

walk_and_copy(extension, search_path, copy_path)

