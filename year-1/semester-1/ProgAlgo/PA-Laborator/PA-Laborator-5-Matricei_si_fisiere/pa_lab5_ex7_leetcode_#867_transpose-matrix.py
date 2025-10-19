#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 14:08:04 2025

@author: fernandodonea
"""

'''
a) Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii fiind date
pe o linie (elementele unei linii date pe o linie separate cu spațiu). Să se
construiască în memorie și să se afișeze matricea transpusă (folosind și
comprehensiune).


b)Aceeași cerință, dar citirea matricei să se facă din fișierul matrice.in (cu/fără a
da dimensiunile matricei) și afișarea matricei transpuse să se facă în fișierul
matrice.out.
'''
'''

matrix = [[1,2,3],[4,5,6],[7,8,9]]
n=len(matrix)
m=len(matrix[0])

a=[ [matrix[i][j] for i in range(n)] for j in range(m) ]
print(a)

'''

fin=open("matrice.in",'r')
fout=open("matrice.out","w")

matrix=[[int(x) for x in line.split()] for line in fin.readlines()]

n=len(matrix)
m=len(matrix[0])

a=[ [matrix[i][j] for i in range(n)] for j in range(m) ]

for line in a:
    fout.write(" ".join([str(x) for x in line])+"\n")








fin.close()
fout.close()