#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:26:02 2025

@author: fernandodonea
"""

'''
 Fie n un numar natural. Aflati cifra de control cu/fara instructiuni repetitive
'''

n=int(input('n='))

while n>9:
    s=0
    while n!=0:
        print(n%10,end=" ")
        s=s+n%10
        n//=10
    print(s)
    n=s
print(n)

if n%9==0:
    print("Cifra de control: 9")
else:
    print(f"Cifra de control este {n}")