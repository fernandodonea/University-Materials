#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:33:45 2025

@author: fernandodonea
"""

'''
Se citește numărul natural n. Să se afișeze următoarea piramidă de numere:
1
1 2
1 2 3
.......
1 2 3 ... n
'''

n=int(input('n='))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    