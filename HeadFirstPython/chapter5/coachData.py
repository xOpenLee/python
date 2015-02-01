#!/usr/bin/env python3
# coding=utf-8


manDataList = ["james.txt", "julie.txt", "mikey.txt", "sarah.txt"]


def delRepeat(unique,dataList):
    for each_t in dataList:
        if each_t not in unique:
            unique.append(each_t)

def sanitize(time_string):
    if '-'  in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

def procFile(filename, dataList):
    try:
        with open(filename, "r+") as fileHandler:
            data = fileHandler.readline()
        dataNo = data.strip().split(',')
        for each_timer in dataNo:
            dataList.append(sanitize(each_timer))
    except IOError as ioerr:
        print ('File error:' + str(ioerr))

def manDataSetMode():
    print ("**********set Mode***********")
    manData = []
    for file in manDataList: 
        (man, format) = file.split('.')
        procFile(file, manData)
        setDist = sorted(set(manData))
        print(man,':',setDist[0:3])
        del manData[:] 

def manData():
    manData = []
    unique = []
    for file in manDataList: 
        (man, format) = file.split('.')
        procFile(file, manData)
        delRepeat(unique, manData)
        unique = sorted(unique)
        print(man,':',unique[0:3])
        del manData[:], unique[:]
    

if __name__ == "__main__":
    print ("coachData.py")
    manData()
    manDataSetMode()
