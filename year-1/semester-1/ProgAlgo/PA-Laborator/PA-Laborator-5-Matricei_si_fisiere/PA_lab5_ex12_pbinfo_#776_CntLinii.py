#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 14:49:43 2025

@author: fernandodonea
"""
'''
Se dă o matrice cu n linii şi m coloane şi elemente numere naturale. 
Să se determine câte linii ale matricei au toate elementele egale.
'''
#n,m=[int(x) for x in input().split()]
#a=[[int(x) for x in input().split()] for _ in range(n)]
a=[[1,2,3,4],[1,1,1,1],[1,1,1,2],[2,2,2,2]]
n=len(a)
m=len(a[0])

l=[1 if i.count(i[0])==m else 0 for i in a ].count(1)
print(l)
