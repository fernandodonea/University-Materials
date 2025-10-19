#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:10:34 2025

@author: fernandodonea
"""

'''
Scrieţi un program care citeşte de la tastatură un număr natural n 
şi construieşte în memorie o matrice cu n linii şi n coloane 
ale cărei elemente sunt numere naturale, 
fiecare reprezentând ultima cifră a câte unui termen al şirului lui Fibonacci, 
începând de la termenul de indice 1 şi până la termenul de indice  n^2 .
'''
n=int(input())
a=0
b=1
c=a+b
matrix=[]
for i in range(0,n):
    linie=[]
    for j in range(0,n):
        linie.append(b%10)
        a=b
        b=c
        c=a+b
    matrix.append(linie)
for linie in matrix:
    print(*linie)
    