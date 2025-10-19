#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 00:27:10 2025

@author: fernandodonea
"""

'''

Să se obțină lista cu toate permutările circulare ale unui șir dat. De exemplu, pentru sir="abcde"
vom obține lista ['abcde', 'bcdea', 'cdeab', 'deabc', 'eabcd'].

'''
s="abcde"

l=[s[i:]+s[:i] for i in range(0,len(s))]

print(l)