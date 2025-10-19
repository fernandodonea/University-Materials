#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 13:28:35 2025

@author: fernandodonea
"""

'''
Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii fiind date
pe o linie (elementele unei linii date pe o linie separate cu spațiu). Se citește în
plus un număr natural k. Să se insereze o linie nouă cu toate elementele 0 între
liniile k și k+1 ale matricei.
'''
m,n=[int(x) for x in input("n,m= ").split()]
a=[[int(x) for x in input().split()] for _ in range(m)]

k=int(input("k="))
#varianta 1
linie_zero=[0]*n
a.insert((k+1),linie_zero)

for linie in a:
    for x in linie:
        print(x,end=" ")
    print()
    
#varianta 2
a2=[]
for i in range(0,m):
    a2.append(a[i])
    if(i==k):
        linie_zero=[0]*n
        a2.append(linie_zero)

for linie in a2:
    for x in linie:
        print(x,end=" ")
    print()

        
