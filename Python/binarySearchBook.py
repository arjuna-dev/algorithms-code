import importlib, time, math
from parser import JSONParser, keysToList


sortedWordsDict =  JSONParser('data/sortedWords.json')
sortedWords     = keysToList(sortedWordsDict)

myWord = 'mother'
index = sortedWords.index(myWord)
print('index', index)


def binary_search(aList, item): 
    low = 0
    high = len(aList)-1

    while low <= high: 
        mid = (low + high)//2
        guess = aList[mid] 
        if guess == item:
            return print(mid, aList[mid], low, high)
        if guess > item: 
            high = mid - 1
        else:
            low = mid + 1
    return None

binary_search(sortedWords, myWord)