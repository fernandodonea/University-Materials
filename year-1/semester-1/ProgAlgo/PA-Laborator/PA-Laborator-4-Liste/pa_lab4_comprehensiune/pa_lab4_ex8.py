#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 00:21:12 2025

@author: fernandodonea
"""

'''
Să se obțină, pentru o listă de numere dată, lista conținând elementele care au aceeași
paritate cu poziția pe care se află. De exemplu, pentru lista [2,4,1,7,5,1,8,10], lista calculată va
conține elementele: 2, 7, 1, 8.
'''
l1=[2,4,1,7,5,1,8,10]

l2=[l1[i] for i in range(0,len(l1)) if l1[i]%2==i%2]
print(l2)