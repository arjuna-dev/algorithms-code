import importlib
from parser import JSONParser

sortedWords =  JSONParser('data/sortedWords.json')

myWord = 'mother'
count = 0
found = False 

for word in sortedWords:
    count += 1
    if word == myWord:
        found = True
        print('Found your word after', count, 'operations')
        break

if found == False:
    print('Your word was not found')