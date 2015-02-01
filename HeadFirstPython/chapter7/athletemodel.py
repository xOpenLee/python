#!/usr/bin/env python3
# coding=utf-8

import os
import pickle

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

class AtheteList(list):
    def __init__ (self, a_name, a_bod=None, a_times = []):
        list.__init__([])
        self.name = a_name
        self.dob = a_bod
        self.extend(a_times)
    def  sortTopData(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])

class Athlete:
    def __init__ (self, a_name, a_bod=None, a_times = []):
        self.name = a_name
        self.dob = a_bod
        self.times = a_times

    def  sortTopData(self):
        return (sorted(set([sanitize(t) for t in self.times]))[0:3])


def getCurDirFileUseListdir(path = './', format = 'txt'):
    files = [ file for file in os.listdir(path) if os.path.isfile(file) ]
    files = [file for file in files if file.endswith(format)]
    return files

def getCoachData(fileName):
    try:
        with open(fileName) as handler:
            data = handler.readline()
        tmp = data.strip().split(',')
        return Athlete(tmp.pop(0), tmp.pop(0), tmp)
    except IOError as ioerr:
        print("file error :", str(ioerr))

def putToStore(fileList):
    allAthletes = {}
    for eachFile in fileList:
        ath = getCoachData(eachFile)
        allAthletes[ath.name] = ath
    try:
        with open("athlete.pickle", "wb") as handler:
            pickle.dump(allAthletes, handler)
    except IOError as ioerr:
        print ("file error:" + str(ioerr))
    return allAthletes

def getFromStore():
    allAthletes = {}
    try:
        with open("athlete.pickle", "rb") as handler:
            allAthletes = pickle.load((handler))
    except IOError as ioerr:
        print ("file error:" + str(ioerr))
    return allAthletes

def main():    
    fileList = getCurDirFileUseListdir()
    ath = putToStore(fileList)
    for eachFile in ath:
        print (ath[eachFile].name + ' ' + ath[eachFile].dob)

    loadAth = getFromStore()
    for eachFile in loadAth:
        print (ath[eachFile].name + ' ' + ath[eachFile].dob)

if __name__ == "__main__":
    main()
