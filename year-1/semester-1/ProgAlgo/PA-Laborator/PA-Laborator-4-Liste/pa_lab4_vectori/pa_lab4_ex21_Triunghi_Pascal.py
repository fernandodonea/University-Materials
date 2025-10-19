#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 02:23:56 2025

@author: fernandodonea
"""

'''
Se dă un număr natural n>2. Să se afișeze primele n linii din triunghiul lui Pascal
(daca c este numărul maxim de cifre ale unui număr din triunghi, toate numerele se vor
afișa pe c+1 caractere). De exemplu, pentru n=6 se va afișa

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1

'''

n=int(input("n="))

v=[0]*(n+1)
for i in range(1,n+1):
    v[i]=1
    for j in range(i-1,1,-1):
        v[j]+=v[j-1]
    for k in range(1,i+1):
        print(v[k],end=" ")
    print()
   

    
        
    