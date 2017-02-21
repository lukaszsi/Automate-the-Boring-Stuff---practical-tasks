#!python3

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def prints_rotated(ourList):
    #Loops as many times as long is any list inside of the main one.
    for i in range(len(ourList[0])):
        #Loops as many times as long is the main list.
        for n in range(len(ourList)):
            print(ourList[n][i], end='')
        print()
        
prints_rotated(grid)
