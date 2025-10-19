#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:58:51 2025

@author: fernandodonea
"""

#Subiectul 3 – metoda Programării Dinamice (3 p.)
#Complexitatea maximă a soluției: O(n2)
'''
Să se determine un subșir crescător de lime maximă al unui șir t format din n numere
întregi.
'''
t=[1,4,2,5,3,-1,4,105,6]
n=len(t)

'''
              0  1   2   3   4   5    6   7    8
    t:       1   4   2   5   3   -1   4  105  6
    
l:        5   3   4   2   3    3   2   1   1

pred:                                 8   n+1    n+1

'''

l=[0]*n
poz=[0]*n

l[n-1]=1
poz[n-1]=n+1

for i in range(n-2,-1,-1):
    l_max=0
    urm=n
    
    for j in range(i,n):
        if t[i]<t[j]:
            if l[j]>l_max:
                l_max=l[j]
                urm=j
    if l_max!=0:
        l[i]=l_max+1
        poz[i]=urm
    else:
        l[i]=1
        poz[i]=n
    

maxi=max(l)
print(maxi)
index=l.index(maxi)
print(index)

path=[]
while index<n:
    path.append(t[index])
    index=poz[index]
print(path)