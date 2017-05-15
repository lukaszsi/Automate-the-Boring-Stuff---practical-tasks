#! Python3
'''Script that finds words like ADJECTIVE, NOUN, ADVERB, VERB
 in a given text and enables to override them. '''
import re

# opens .txt file
textFile = open(input('Name of the file? '))
newTextFile = textFile.read()
textFile.close()
# regexes and changing of the text
words = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
while True:
    checkFile = newTextFile
    for i in words:
        if re.compile(i).search(newTextFile) != None:
            change = input('please enter '+ i.lower())
            newTextFile = re.compile(i).sub(change, newTextFile, count=1)
    if checkFile == newTextFile:
        break
# Prints changed text and saves it as 'newfile.txt'.
print(newTextFile)
newFile = open('newfile.txt', 'w')
newFile.write(newTextFile)
newFile.close()
