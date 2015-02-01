#!/usr/bin/env python3
# coding=utf-8
"""
This is my first python exmaple
hello world
"""


def print_loop(var,level=0):
    for each_item in var:
        if isinstance(each_item,list):
            print_loop(each_item, level + 1)
        else:
            for tab_stop in range(level):
                print("\t",end='')
            print(each_item)

def movieFunc():
    movies = ["the holy grail", "1975", "terry jones & terry gilliam", "91",
          ["graham chapman", ["michael palin", "John cheele",
                              "terry gilliam", "eric idle", "terry jones"]]]

    print (movies)
    print_loop(movies, 0)


if __name__ == "__main__":
    movieFunc()
