#! python3
# photoFolderSearch.py - program goes through every folder on hard drive
# and finds potential photo folders.

import os
from PIL import Image

for folder_name, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not (filename.lower().endswith('.jpg') or filename.lower().endswith('.png')):
            numNonPhotoFiles += 1
            continue    # skip to next filename

        # Open image file using Pillow.
        try:
            fileImage = Image.open(os.path.join(folder_name,filename))
            width, height = fileImage.size
            
            # Check if width & height are larger than 500.
            if width > 500 and height > 500:
                # Image is large enough to be considered a photo.
                numPhotoFiles += 1
            else:
                # Image is too small to be a photo.
                numNonPhotoFiles += 1
        except:
            print('Can not open file, skipping ' + os.path.join(folder_name,filename))

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if numPhotoFiles > numNonPhotoFiles:
        print(os.path.abspath(folder_name))
