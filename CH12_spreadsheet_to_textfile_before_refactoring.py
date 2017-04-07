#! python3
import openpyxl

sheet = openpyxl.load_workbook('textToSheet.xlsx').active
colNum = 0
for column in sheet.columns:
    textFile = open('column'+str(colNum)+'.txt', 'a')
    for cell in column:
        textFile.write(str(cell.value))
    textFile.close()
