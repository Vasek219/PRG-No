#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:34:44 2018

@author: lov35174
"""

f = open('text.txt', 'r')

while True:
    radek = f.readline()
    if radek == '':
        break
    radek = radek.strip()
    if radek != '' and radek[0].isupper():
        print(radek.upper(), end='')
    else:
        print(radek, end='')
    
f.close()