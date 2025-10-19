#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:01:11 2025

@author: fernandodonea
"""

'''
Se citește un număr n și un șir de n numere naturale. Să se afișeze cele mai mari două
valori distincte din șir (dacă nu există se va afișa un mesaj corespunzător)
'''
n=int(input("n="))
print('citi sirul')
l=[int(x) for x in input().split()]

a=b=-1
for i in range(0,n):
    if l[i]>a:
        b=a
        a=l[i]
    elif l[i]>b:
        b=l[i]
if a==b:
    print("nu")
else:
    print(b,a)