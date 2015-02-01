#!/usr/bin/env python3
# coding=utf-8

import os
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

def getCoachData(filename):
    try:
        with open(filename) as handler:
            data = handler.readline()

        return (data.strip().split(','))
    except IOError as ioerr:
        print("file error:" + str(ioerr))

def procManData(fileName):
    man = getCoachData(fileName)
    (man_name, man_dob) = man.pop(0), man.pop(0)
    print (man_name + "'s fastest times are:" + str(sorted(set([sanitize(t) for t in man]))[0:3]))

def getCurDirFileUseListdir(path = './', format = 'txt'):
    files = [ file for file in os.listdir(path) if os.path.isfile(file) ]
    files = [file for file in files if file.endswith(format)]
    return files

def getCurDirFile(path = './', format = 'txt'):
    fileList = []
    for subdir, dirs, files in os.walk(path):
        for file in files:
            (fileName, fileFormat) = file.split('.')
            if fileFormat == format:
                fileList.append(file)
    return fileList


    
if __name__ == "__main__":
    manFile = []
    manFile = getCurDirFile()
    manFile = getCurDirFileUseListdir()
    for man in manFile:
        procManData(man)
    
