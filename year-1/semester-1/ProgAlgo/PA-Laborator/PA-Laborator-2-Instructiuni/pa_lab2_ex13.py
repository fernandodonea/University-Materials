#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:35:01 2025

@author: fernandodonea
"""

x=int(input("x="))

while x!=1:
    print(x,end=" ")
    
    if x%2==0:
        x=x-1
    else:
        x=x+1
        x=x//2
print(1)
