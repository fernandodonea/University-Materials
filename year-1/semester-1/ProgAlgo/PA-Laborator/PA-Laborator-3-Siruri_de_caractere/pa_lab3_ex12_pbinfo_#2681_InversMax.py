#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 22:03:28 2025

@author: fernandodonea
"""

'''
Se citește un șir de caractere reprezentând o propoziție care conține litere mari și mici ale alfabetului englez, spații, cifre și alte simboluri. În cele ce urmează, considerăm cuvânt orice secvență delimitată de spații ce conține cel puțin o literă.

Se se afișeze șirul citit astfel încât cuvintele de lungime maximă să fie înlocuite cu inversul (oglinditul) lor, restul cuvintelor și aranjarea lor în propoziție să rămână neschimbate.
'''

s=input()
prop=s.split(sep=" ")
print(prop)

maxi=0
for cuv in prop:
    ok=False
    n=len(cuv)
    for i in range(n):
        if cuv[i].isalpha()==True:
            ok=True
            break
    if ok==True:
        if n>maxi:
            maxi=n
    
for cuv in prop:
    ok=False
    n=len(cuv)
    for i in range(n):
        if cuv[i].isalpha()==True:
            ok=True
            break
    if ok==True and n==maxi:
        cuv=cuv[::-1]
    print(cuv,end=" ")