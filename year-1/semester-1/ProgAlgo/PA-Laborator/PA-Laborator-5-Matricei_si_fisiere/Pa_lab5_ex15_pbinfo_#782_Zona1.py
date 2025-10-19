#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:18:00 2025

@author: fernandodonea
"""

'''
Se dă o matrice pătratică cu n linii și n coloane și elemente numere naturale mai mici decât 1000.
 Să se afișeze în ordine strict crescătoare valorile care apar sub diagonala principală 
 și sub diagonala secundară de cel puţin 2 ori. 
 Fiecare valoare se va afişa o singură dată.
 '''
 
n,m=[int(x) for x in input().split()]
a=[[int(x) for x in input().split()] for _ in range(n)]
''' 
n=6
a=[
[10, 8, 5, 8, 4, 2],
[6, 5, 3, 1, 3, 8], 
[8, 1, 4, 7, 8, 8], 
[5, 1, 9, 6, 6, 1], 
[8, 9, 3, 2, 3, 6],
[8, 9, 3, 3, 9, 6]
]
'''
 
l=[a[i][j] for i in range(n) for j in range(n) if (i>j and (i+j)>(n-1))]
l.sort(reverse=True)
print(l)
aux={x for x in l if l.count(x)>=2}

rez=[x for x in aux]
rez.sort()
print(*rez)