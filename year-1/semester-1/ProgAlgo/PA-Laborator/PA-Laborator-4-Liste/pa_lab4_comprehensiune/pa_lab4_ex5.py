#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 00:14:03 2025

@author: fernandodonea
"""

'''
Pentru un număr natural n citit de la tastatură, să se genereze lista de forma 1, -2, 3,
-4, ... până la n (cu semnul corespunzător).
'''

n=int(input("n="))

l=[x if x%2==1 else -x for x in range(1,n+1)]
print(l)