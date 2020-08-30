import os
import shutil
from datetime import datetime

curDir = os.getcwd()
cycle = 1

while cycle == 1:
    action = input('Sort - s, Extract - e, Quit - q: ')
    if action == 's':
        for a in os.listdir(curDir):
            if a[-5:] != ' OBDM' and a != 'Organize By Date Modified.py':
                curFileAndDir = os.path.join(curDir, a)
                fileModDate = datetime.fromtimestamp(os.path.getmtime(curFileAndDir)).date().strftime('%Y-%m-%d')
                dirToBeMade = os.path.join(curDir, fileModDate + ' OBDM')

                if not os.path.exists(dirToBeMade):
                    os.mkdir(dirToBeMade)
                    print('Directory Created: ' + dirToBeMade)
                    shutil.move(curFileAndDir, dirToBeMade)
                else:
                    shutil.move(curFileAndDir, dirToBeMade)
                print('--> ' + a + ' moved to --> ' + dirToBeMade)
            else:
                print('Item: ' + a + ' is an OBDM item')
    elif action == 'e':
        for a in os.listdir(curDir):
            if a[-5:] == ' OBDM':
                subCurDir = os.path.join(curDir, a)
                print('OBDM item found: ' + subCurDir)
                for i in os.listdir(subCurDir):
                    subCurFileAndDir = os.path.join(subCurDir, i)
                    shutil.move(subCurFileAndDir, curDir)
                    print('<-- ' + i)
    elif action == 'q':
        cycle = 0
    else:
        print('Invalid Input')

input('Press any key to exit')
    