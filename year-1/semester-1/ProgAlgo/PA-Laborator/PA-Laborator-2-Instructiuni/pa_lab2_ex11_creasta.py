#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:17:22 2025

@author: fernandodonea
"""

'''
Un vector 𝑣 𝑛
format din numere întregi se numește vector creastă dacă există un indice 𝑝 
astfel încât 𝑣[0]≤𝑣[1] ≤…≤𝑣[𝑝] si 𝑣[𝑝]≥𝑣[𝑝 + 1] ≥…≥𝑣[𝑛 − 1]. 
Scrieţi un program care citeşte un vector format din 𝑛
numere întregi şi verifică dacă este vector creastă sau nu.
'''
n=int(input("n="))
print("cititi vectorul")

v=[int(x) for x in input().split()]

maxi=max(v)
p=v.index(maxi)

ok=True
for i in range(0,p):
    if v[i]>v[i+1]:
        ok=False
        break
for i in range(p,n-1):
    if v[i]<v[i+1]:
        ok=False
        break
if ok==True:
    print("creastaa")
else:
    print("nu")
    

