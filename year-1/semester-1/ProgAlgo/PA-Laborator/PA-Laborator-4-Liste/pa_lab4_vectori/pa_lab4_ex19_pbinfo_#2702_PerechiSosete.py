#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 01:55:20 2025

@author: fernandodonea
"""

'''
Se dă un vector v de n<100 numere naturale de cel mult două cifre. Să se determine
numărul de perechi disjuncte de elemente de egale (de forma (v[i], v[j]) cu i!=j și v[i]=v[j])
care se pot forma cu elementele vectorului. - folosind vector de frecvențe

n=10
1 3 2 1 2 2 1 2 1 2

'''
fr=[0]*99

n=int(input())
v=[int(x) for x in input().split()]
for i in v:
    fr[i]+=1
k=0
for i in fr:
    k+=i//2
    
print(k)


