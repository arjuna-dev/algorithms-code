import importlib, time, math
from parser import JSONParser, keysToList


sortedWordsDict =  JSONParser('data/sortedWords.json')
sortedWords     = keysToList(sortedWordsDict)

myWord = 'acolyte'
index = sortedWords.index(myWord)
print('index', index)
print('index', index)
print('index', index)

totalWordCount =  len(sortedWords)
middleIndex = 0
count = 0

print(totalWordCount)
middleIndex = round(totalWordCount/2)
displaceBy = totalWordCount/2
print(middleIndex)

while myWord != sortedWords[middleIndex]:
    count += 1
    time.sleep(.200)
    displaceBy /= 2
    if displaceBy == 0:
        displaceBy = 1
    if myWord > sortedWords[middleIndex]:
        middleIndex += round(displaceBy)
        print('displaceBy', round(displaceBy))
        print('new middleIndex', middleIndex)
    else:
        middleIndex -= round(displaceBy)
        print('displaceBy', round(displaceBy))
        print('new middleIndex', middleIndex)


print('Found it ' + sortedWords[middleIndex] )