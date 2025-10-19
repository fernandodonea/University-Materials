#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 00:48:09 2025

@author: fernandodonea
"""

'''
Se dă o listă de numere naturale. Să se șteargă din listă subsecvența delimitată de
primele două zerouri din listă (inclusiv zerourile).
'''

l=[1,2,0,2,2,0,0,0,7,8]

start=l.index(0)
end=l.index(0,start+1)+1
l[start:end]=[]
print(l)
    