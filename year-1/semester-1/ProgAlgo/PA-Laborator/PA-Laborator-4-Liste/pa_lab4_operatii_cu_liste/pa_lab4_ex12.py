#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 00:45:32 2025

@author: fernandodonea
"""

l=[12,432,543,65765,231,12,22,32]
k=int(input("k="))

l1=[l[i] for i in range(0,len(l)) if i>=k ]
print(l1)

l2=[l[i] for i in range(k,len(l))]
print(l2)