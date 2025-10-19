#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 00:53:50 2025

@author: fernandodonea
"""

'''
Se dă o listă de numere naturale. Să se șteargă din listă toate zerourile.
'''

l=[1,2,0,40,0,0,1,2,3,0,0,5]
i=0
n=len(l)
while i<n:
    if l[i]==0:
        l.pop(i)
        i=i-1
    i=i+1
    n=len(l)
    
    
     
print(l)