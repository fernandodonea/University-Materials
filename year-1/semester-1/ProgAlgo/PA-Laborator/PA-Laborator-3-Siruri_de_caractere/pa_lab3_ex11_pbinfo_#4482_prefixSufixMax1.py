#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 21:49:31 2025

@author: fernandodonea
"""

'''

Să se scrie un program care să determine cel mai lung prefix care este palindrom 
și cel mai lung sufix care este palindrom dintr-un cuvânt citit de la tastatură

intrare:
    anamaria
iesire:
    ana a
'''
s=input()


for i in range(0,len(s)+1):
    cuv=s[:i]
    if cuv==cuv[::-1]:
        prefix=cuv
    
    cuv=s[-i:]
    if cuv==cuv[::-1]:
        sufix=cuv
print(prefix,sufix)
