#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:54:55 2025

@author: fernandodonea
"""

'''
Cifrul lui Cezar - folosind comprehensiune
'''

s="abz" #=>bca
k=2
l=[ chr((((ord(lit)-97)+k)%26)+97) for lit in s]
print(l)