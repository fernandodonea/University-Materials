#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:31:06 2025

@author: fernandodonea
"""

'''
Se citesc două numere naturale a și b cu cel mult două cifre. Să se afișeze toate numerele
naturale pozitive de cel mult două cifre care se divid cu 5 și nu se află în intervalul [a,b]
(numerele se vor afișa pe aceeași linie, ordonate crescător, apoi descrescător)
'''

a,b=input('a,b=').split()
a=int(a)
b=int(b)

for i in range(10,100):
    if i<a or i>b:
        if i%5==0:
            print(i,end=" ")