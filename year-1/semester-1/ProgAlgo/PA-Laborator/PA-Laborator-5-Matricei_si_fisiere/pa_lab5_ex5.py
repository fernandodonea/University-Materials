#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 13:38:57 2025

@author: fernandodonea
"""

'''
Se consideră tabloul bidimensional cu m linii şi n coloane, care conţine doar
valorile {0,1,2}. Să se determine câte linii au produsul elementelor maxim
(folosind și comprehensiune)
'''
#n,m=[int(x) for x in input().split()]
#a=[[int(x) for x in input().split()] for _ in range(m)]
a=[
[0, 1, 2, 2],
[1, 1, 2, 2],
[2, 2, 2, 0],
[1, 1, 2, 2]
]
m=len(a)
maxi=0
k=0
for line in a:
    prod=1
    for x in line:
        prod*=x
    if prod>maxi:
        maxi=prod
        k=1
    elif prod==maxi:
        k=k+1
print(maxi,k)