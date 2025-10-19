#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 00:16:26 2025

@author: fernandodonea
"""

'''
Se dă o listă de numere. Să se obțină lista cu elementele impare din lista dată.
'''

l1=[1,23,435,656,2,56]

l2=[x for x in l1 if x%2==1]
print(l2)