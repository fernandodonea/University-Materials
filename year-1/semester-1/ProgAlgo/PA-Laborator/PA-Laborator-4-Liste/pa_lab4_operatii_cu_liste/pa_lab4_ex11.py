#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 00:42:43 2025

@author: fernandodonea
"""

'''
Se dau două liste L1 si L2 de lungime n. Să se înlocuiască elementele de pe poziții
pare din L1 cu cele de pe poziția corespunzătoare din L2 folosind feliere (slice).
'''
l1=[1,2,3,4,5]
l2=[67,87,32,543,54]
n=len(l1)
# l1=[l2[i] if i%2==0 else l1[i] for i in range(0,len(l1)) ]
l1[1:n:2]=l2[1:n:2]

print(l1)