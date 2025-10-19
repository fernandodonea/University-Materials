#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:52:29 2025

@author: fernandodonea
"""

'''
Să se scrie un program care citeşte de la tastatură trei numere naturale și determină diferenţa dintre
cel mai mare şi cel mai mic.
'''
l=[]
for i in range(0,3):
    x=int(input())
    l.append(x)
print(max(l)-min(l))

