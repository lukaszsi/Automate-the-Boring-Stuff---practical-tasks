#! python3
'''Script enables to put gap in between certain file numbers.'''
import os
import shutil

# Which number has to be a gap
gap_number=int(input('Which number has to be a gap? '))
# Checks how many such files are in a folder
files_number=0
numbers_list = []
for i in range(1,1000):
    if 'spam'+str(str('000'+str(i))[-3:])+'.txt' in os.listdir('F:\\spam'):
        files_number+=1
        numbers_list.append(i)
numbers_list.sort()
print('Pliki zaczynają się od liczby '+str(numbers_list[0]))
x = int(numbers_list[0])-1    
# Changes from the end numbers of files to +1 
for n in range(files_number+x,(gap_number-1),-1):
    shutil.move('F:\\spam\\'+'spam'+str(str('000'+str(n))[-3:])+'.txt',
                'F:\\spam\\'+'spam'+str(str('000'+str(n+1))[-3:])+'.txt')
