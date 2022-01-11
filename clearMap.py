import os

saveFolder = input('What save do you want to edit?: ')
    
startCoordX = int((int(input('Enter the first coordinate: ')))/10)
startCoordY = int((int(input('Enter the second coordinate: ')))/10)
endCoordX = int((int(input('Enter the first coordinate: ')))/10)
endCoordY = int((int(input('Enter the second coordinate: ')))/10)

startChunkX = int(input('Enter the first chunk number: '))
startChunkY = int(input('Enter the second chunk number: '))
endChunkX = int(input('Enter the first chunk number: '))
endChunkY = int(input('Enter the second chunk number: '))

files = os.listdir(saveFolder)

for f in files:
    curItem = f[:-4].split('_')
    if len(curItem) == 3 and curItem[0] == 'map':
        if int(curItem[1]) >= startCoordX and int(curItem[1]) <= endCoordX and int(curItem[2]) >= startCoordY and int(curItem[2]) <= endCoordY:
            print(f'Deleting {f}')
            os.remove(f'{saveFolder}\\{f}')
    elif len(curItem) == 3 and (curItem[0] == 'chunkdata' or curItem[0] == 'zpop'):
        if int(curItem[1]) >= startChunkX and int(curItem[1]) <= endChunkX and int(curItem[2]) >= startChunkY and int(curItem[2]) <= endChunkY:
            print(f'Deleting {f}')
            os.remove(f'{saveFolder}\\{f}')
        
