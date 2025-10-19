#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 13:55:55 2025

@author: fernandodonea
"""

'''
Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii fiind date
pe o linie separate cu spațiu. Se citește în plus un număr natural k. Să se permute
fiecare linie a matricei circular la dreapta cu k poziții (Echivalent: Să se permute
coloanele matricei circular spre dreapta cu k poziții)
'''

#n,m=[int(x) for x in input().split()]
#a=[[int(x) for x in input().split()] for _ in range(m)]
a=[
[1, 1, 4, 5],
[11, 123, 243, 222],
[0, 111,111, 0],
[7, 8, 9, 10]
]

n=m=4
#permutarea liniilor
k=int(input("k="))
b=[[0 for i in range(n)] for j in range(m)]

for i in range(0,m):
    b[i]=a[(i-k)%m]
    
print(b)

