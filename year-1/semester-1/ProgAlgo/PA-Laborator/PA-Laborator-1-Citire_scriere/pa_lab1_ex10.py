#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:00:49 2025

@author: fernandodonea
"""

'''
Să se scrie un program care citeşte de la tastatură trei numere naturale distincte și le afișează în
ordine crescătoare.
'''

l=[int(x) for x in input().split()]
l=sorted(l,reverse=True)
print(*l)