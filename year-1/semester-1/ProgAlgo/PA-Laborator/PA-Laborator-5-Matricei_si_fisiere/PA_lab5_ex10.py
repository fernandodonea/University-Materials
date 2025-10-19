#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 14:36:37 2025

@author: fernandodonea
"""

'''
Se citeşte o matrice cu 𝑚 𝑛
linii, coloane şi elemente numere întregi. Să se afişeze
matricea citită astfel: 
    prima linie de la stânga spre dreapta, 
    a doua linie de la dreapta spre stânga,
    a treia linie de la stânga spre dreapta,
    a patra linie de la dreapta spre stânga etc.
'''

#n,m=[int(x) for x in input().split()]
#a=[[int(x) for x in input().split()] for _ in range(n)]

a=[[5,5,10,5],[3,9,1,9],[4,10,1,2]]
n=len(a)
m=len(a[0])
for i in range(0,n):
    if (i+1)%2==1:
        print(*a[i])
    else:
        print(*a[i][::-1])
    