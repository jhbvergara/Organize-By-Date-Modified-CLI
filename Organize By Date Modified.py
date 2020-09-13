import os
import shutil
from datetime import datetime

curDir = os.getcwd()
cycle = 1

while cycle == 1:
    action = input('Simple File Arranger \ns - Sort \ne - Extract \ng - Get folder sizes \nq - Quit: ')
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
    elif action == 'g':
        print('\nGetting folder sizes...')
        folderName = []
        folderSize = []

        for a in os.listdir(curDir):
            if a[-5:] == ' OBDM':
                subCurDir = os.path.join(curDir, a)
                fileSize = 0

                for path, name, files in os.walk(subCurDir):
                    for i in files:
                        fileSize += os.path.getsize(os.path.join(path, i))
                
                folderName.append(subCurDir)
                folderSize.append(fileSize)

        #Arrange from highest to lowest
        for b in range(0, len(folderSize)):
            for i in range(b + 1, len(folderSize)):
                if folderSize[b] < folderSize[i]:
                    folderName[b], folderName[i] = folderName[i], folderName[b]
                    folderSize[b], folderSize[i] = folderSize[i], folderSize[b]

        for x in range(0, len(folderSize)):
            print(folderSize[x], ' == ', folderName[x])

    elif action == 'q':
        cycle = 0
    else:
        print('Invalid Input')

input('Press any key to exit')
    