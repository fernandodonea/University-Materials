#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 00:22:41 2025

@author: fernandodonea
"""


'''
Sa dă o listă. Să se obțină lista cu perechiile (tupluri) de elementele de pe poziții
vecine. De exemplu pentru lista [1,2,3,4] lista rezultată ar fi [(1,2),(2,3),(3,4)].
'''

l1=[11,22,63,84]

l2=[(l1[x], l1[x+1]) for x in range(0,len(l1)-1)]
print(l2)