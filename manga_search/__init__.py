# -*- coding: utf8 -*-

def linsearch(data, x):
    for i in range(1, len(data)):
        if data[i] == x:
            return i
    return -1
