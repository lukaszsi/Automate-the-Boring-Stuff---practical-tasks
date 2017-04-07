#! python3
import os
import sys
import PyPDF2
import send2trash

if len(sys.argv) < 2:
    print('Not enough data given, please use run with password added!')
password = sys.argv[1]
while True:
    path = input('Please give the path to search directory for pdf files ')
    if os.path.isdir(path):
        break
    else:
        print('This is not a directory!')
        continue
os.chdir(path)

for folderName, subfolders, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdfFile = open(os.path.join(folderName, filename), 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            if pdfReader.isEncrypted:
                print('File ' + os.path.join(folderName, filename) + ' is already encrypted!')
                continue
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            pdfWriter.encrypt(password)
            resultPdf = open(os.path.join(folderName, filename)[0:-4] + '_encrypted.pdf', 'wb') 
            pdfWriter.write(resultPdf)
            pdfFile.close()
            resultPdf.close()
            doneResultPdf = PyPDF2.PdfFileReader(open(os.path.join(folderName, filename)[0:-4] + '_encrypted.pdf', 'rb'))
            if doneResultPdf.decrypt('123') == 1:
                send2trash.send2trash(os.path.join(folderName, filename))
