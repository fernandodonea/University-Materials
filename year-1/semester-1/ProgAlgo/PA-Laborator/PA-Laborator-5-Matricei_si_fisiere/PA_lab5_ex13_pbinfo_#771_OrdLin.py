#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:05:26 2025

@author: fernandodonea
"""
'''
Se dă o matrice cu n linii şi m coloane şi elemente numere naturale. 
Să se ordoneze liniile matricei crescător după suma elementelor.
'''


#n,m=[int(x) for x in input().split()]
#a=[[int(x) for x in input().split()] for _ in range(n)]
a=[[1,2,3,4],[1,1,1,1],[1,1,1,2],[2,2,2,2]]
n=len(a)
m=len(a[0])

a.sort(key=sum)
for line in a:
    print(*line)
