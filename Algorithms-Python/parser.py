import json
# from pprint import pprint

def JSONParser(JSONFilePath):
    with open(JSONFilePath) as f:
        data = json.load(f)
    return data

sortedWords = JSONParser('data/sortedWords.json')

def keysToListFile(dictionary):
    textFile = open('data/keysFromDic.txt', 'w+')
    for key in dictionary:
        textFile.write(key+'\n')
    textFile.close()
    return textFile

def keysToList(dictionary):
    array = []
    for key in dictionary:
        array.append(key)
    return array

