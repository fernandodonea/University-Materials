#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 02:36:46 2025

@author: fernandodonea
"""

'''
Se citește un vector cu n elemente, numere naturale. Să se determine câte elemente ale vectorului sunt egale cu diferența dintre cea mai mare și cea mai mică valoare din vector.

'''
n=int(input())
v=[int(x) for x in input().split()]
mini=min(v)
maxi=max(v)

dif=maxi-mini
k=v.count(dif)
print(k)