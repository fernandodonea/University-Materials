#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 00:17:36 2025

@author: fernandodonea
"""

'''
Se dă o listă de numere. Să se obțină lista cu elementele aflate pe poziții impare în
lista dată.

'''
l1=[1,32,543,657,2,43,312]

l2=[l1[i] for i in range(0,len(l1)) if i%2==1]
print(l2)