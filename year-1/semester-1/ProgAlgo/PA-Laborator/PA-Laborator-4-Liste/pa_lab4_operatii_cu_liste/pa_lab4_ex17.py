#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 01:40:20 2025

@author: fernandodonea
"""

'''
Se dă o listă de numere reale (toate elementele sale se vor da pe o linie separate prin
spațiu). Să se insereze câte un 0 după fiecare element negativ (fără a folosi liste
suplimentare).
'''
l=[float(x) for x in input().split()]

for i in range(0,len(l)):
    if l[i]<0:
        l[i:i+1]=[l[i],0]
print(l)