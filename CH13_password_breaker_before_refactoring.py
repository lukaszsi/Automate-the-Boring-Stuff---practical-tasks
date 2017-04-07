#! python3
import docx
import os
import PyPDF2

os.chdir('C:\\Python')
wordsFile = open('dictionary.txt')
text = wordsFile.read()
wordsList = text.split('\n')
pdfFile = open('watermarkEncrypted.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
for word in wordsList:
    if pdfReader.decrypt(word) != 0:
        print(word)
        break
    elif pdfReader.decrypt(word.lower()) != 0:
        print(word.lower())
        break
    else:
        continue
