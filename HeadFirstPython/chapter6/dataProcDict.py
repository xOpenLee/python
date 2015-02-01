#!/usr/bin/env python3
# coding=utf-8

import os

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

def getCoachData(fileName):
    try:
        with open(fileName) as handler:
            dataList = handler.readline()
        return (dataList.strip().split(','))
    except IOError as ioerr:
        print("file err:" + str(ioerr))

def saveToDict(manList):
    manDict = {}
    manDict['Name'] = manList.pop(0)
    manDict['DOB'] = manList.pop(0)
    manDict['Times'] = manList
    return manDict

def procManData(fileName):
    manList = []
    manDict = {}
    manList = getCoachData(fileName)
    #print (manList)
    
    manDict = saveToDict(manList)
    #print (manDict)
    
    manDict['Times'] = sorted(set([sanitize(t) for t in manDict['Times']]))
    manDict['Times'] = manDict['Times'][0:3]
   # print (manDict['Name'])
   # print (manDict['DOB'])
   # print (manDict['Times'])
    print (manDict)

def getCurDirFileUseListdir(path = './', format = 'txt'):
    files = [ file for file in os.listdir(path) if os.path.isfile(file) ]
    files = [file for file in files if file.endswith(format)]
    return files



if __name__ == "__main__":
    manList = []
    manList = getCurDirFileUseListdir()
    for fileName in manList:
        procManData(fileName)
