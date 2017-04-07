#! python3
import openpyxl

files = ['text1.txt', 'text2.txt', 'text3.txt']
wb = openpyxl.Workbook()
sheet = wb.active
rowNum = 1
colNum = 1
for file in files:
    for line in open(file).readlines():
        sheet.cell(row=rowNum, column=colNum).value = line
        rowNum +=1
    colNum += 1
    rowNum = 1
wb.save('textToSheet.xlsx')
