#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 20:19:22 2025

@author: fernandodonea
"""


'''
Consultați documentația pentru a vedea cum se folosesc metodele replace, upper ,
isupper , center .
'''

s='ana are mere are mere are mere'
s=s.capitalize()
print(s)
s=s.replace('are mere' ,'gigel',2)
print(s)
s=s.upper()
print(s)
if s.isupper():
    print('true')
s='ana gigel  '
s=s.center(30)
print(s)