#!/usr/bin/env python3
# coding=utf-8

import os


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

    def addTime(self, timeValue):
        self.times.append(timeValue)

    def addTimeList(self, time_list):
        self.times.extend(time_list)


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

def getCoachData(fileName):
    try:
        with open(fileName) as handler:
            data = handler.readline()
        tmp = data.strip().split(',')
        return Athlete(tmp.pop(0), tmp.pop(0), tmp)
    except IOError as ioerr:
        print("file error :", str(ioerr))

def getCurDirFileUseListdir(path = './', format = 'txt'):
    files = [ file for file in os.listdir(path) if os.path.isfile(file) ]
    files = [file for file in files if file.endswith(format)]
    return files

def main():
    vera = AtheteList("vera v")
    vera.append("1.3")
    print (vera.name)
    print(vera)
    print(vera.sortTopData())
    
    fileList = getCurDirFileUseListdir()
    print (fileList)
    for fileName in fileList:
        manClass = getCoachData(fileName)
        manClass.addTimeList(["1.1","1.2"])
        print ("###INFO: " + manClass.name + "'s fastest times are: " + str(manClass.sortTopData()))


if __name__ == "__main__":
    main() 

