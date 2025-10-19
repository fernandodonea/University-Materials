#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:04:11 2025

@author: fernandodonea
"""

'''
Scrieți un program care afișează puterile lui 2 [𝑎, 𝑏]
aflate într-un interval . 
De exemplu, în intervalul [10,100] se găsesc următoarele puteri ale lui 2: 
16, 32 64
'''

a,b=input("[a,b]:").split()
a=int(a)
b=int(b)

for i in range(a,b+1):
    x=i
    while x%2==0:
        x=x//2
    if x==1:
        print(i, end=" ")