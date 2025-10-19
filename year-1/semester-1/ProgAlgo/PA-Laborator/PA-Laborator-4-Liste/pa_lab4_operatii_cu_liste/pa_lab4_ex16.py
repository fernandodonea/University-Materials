#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 01:09:22 2025

@author: fernandodonea
"""

'''
Se dă o listă de numere naturale ordonată crescător (toate elementele sale se vor da
pe o linie separate prin spațiu). Să se elimine duplicatele din listă
'''
l=[1,1,2,3,4,4,5,5,5]

i=0
n=len(l)
while i<n-1:
    if l[i]==l[i+1]:
        l[i:(i+1)]=[]
        i=i-1
    n=len(l)
    i+=1
print(l)
