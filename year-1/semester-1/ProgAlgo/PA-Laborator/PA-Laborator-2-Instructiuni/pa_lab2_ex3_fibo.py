#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:27:30 2025

@author: fernandodonea
"""

'''
Se citesc două numere naturale a și b. Să se afișeze cel mai mic număr Fibonacci din
intervalul [a,b].
'''
a,b=input('a,b=').split()
a=int(a)
b=int(b)

x=0
y=1
z=x+y
while z<a:
    x=y
    y=z
    z=x+y
if z<=b:
    print(z)
else:
    print("nu exista")
