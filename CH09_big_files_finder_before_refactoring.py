#! python3
''' Program that walks through a folder tree that was given and searches
for files over 100 MB and then prints these files with their absolute
path to the screen'''
import os

# program asks about path to walk through
def walk_and_print():
    search_path = input("What is the path to look in? (example: 'F:\\bacon'. Hit enter to use example): ")
    if search_path == '':
        search_path = 'F:\\bacon'
# program walks through a folder tree that was given and searches for files over 100 MB
    for folder_name, subfolders, filenames in os.walk(search_path):
        for filename in filenames:
            if os.path.getsize(os.path.join(folder_name,filename)) > 104857600:
# program prints these files with their absolute path to the screen
                print(os.path.join(folder_name,filename))
walk_and_print()
