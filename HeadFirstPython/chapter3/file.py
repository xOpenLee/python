#!/usr/bin/env python3
# coding=utf-8

import os


def getFilePath():
    os.getcwd()


def fileProc(filename):
    if not os.path.exists(filename):
        print(filename,"not exists")
        return
    the_file = open(filename)
    for each_line in the_file:
        #        if each_line.find(":") == -1:
        #            continue
         try:
             (role, line_spoken) = each_line.split(':', 1)
             print(role, end='')
             print(' said: ', end='')
             print(line_spoken, end='')
         except ValueError:
             pass
    the_file.close()

if __name__ == "__main__":
    fileProc('sketch.txt')
