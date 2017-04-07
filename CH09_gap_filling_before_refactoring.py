#! python3
import os
import shutil

for i in range(1,1000):
    if 'spam'+str(str('000'+str(i))[-3:])+'.txt' in os.listdir('F:\\spam') and\
       'spam'+str(str('000'+str(i+1))[-3:])+'.txt' not in os.listdir('F:\\spam'):
        k=1
        for n in range(2,1000):
            if i+n >= 1000:
                    break
            elif 'spam'+str(str('000'+str(i+n))[-3:])+'.txt' in os.listdir('F:\\spam'):
                shutil.move('F:\\spam\\'+'spam'+str(str('000'+str(i+n))[-3:])+'.txt', 'F:\\spam\\'+'spam'+str(str('000'+str(i+k))[-3:])+'.txt')
                k+=1
