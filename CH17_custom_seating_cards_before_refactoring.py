#! python3
# customSeatingCards.py - creates custom cards for list of guests.

import os
from PIL import Image, ImageDraw

# Loads flower image and changes its size.
flowerImage = Image.open('flower.jpg')
width, height = flowerImage.size
smallFlowerIm = flowerImage.resize((int(width/5), int(height/5)))
# TODO: do i have to save it?

# Creates list of guests.
os.chdir('C:\\User\\Desktop\\Cards')
guestsFile = open('guests.txt')
text = guestsFile.read()
guestsList = text.split('\n')

for guest in guestsList:
    # Creates image.
    image = Image.new('RGBA', (288, 360), 'yellow')

    # Adds guest's name.
    draw = ImageDraw.Draw(image)
    draw.text((110, 60), guest, fill='blue')
    image.save(guest + '.jpg')
    
    # Adds flower.
    image = Image.open(guest + '.jpg')
    image.paste(smallFlowerIm, (120, 100))

    # Adds rectangles.
    blackImage = Image.new('RGBA', (292, 364), 'black')
    blackImage.paste(image, (2, 2))

    blackImage.save(guest + '.jpg')
