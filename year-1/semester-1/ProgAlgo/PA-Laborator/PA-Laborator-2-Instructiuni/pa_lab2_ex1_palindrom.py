#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:18:06 2025

@author: fernandodonea
"""

'''
Se citește un număr natural n. Să se testeze dacă este palindrom
'''

n=int(input("n="))
ogl=0
cn=n
while cn!=0:
    c=cn%10
    cn=cn//10
    ogl=ogl*10+c

if ogl==n:
    print('palindrom')
else:
    print("nu")
