#! python3

tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David',],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)
    for w in range(len(table[0])):
        for z in range(len(table)):
            if len(table[z][w]) > colWidths[z]:
                colWidths[z] = len(table[z][w])
    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(colWidths[y] + 1), end='')
        print()
   
printTable(tableData)
