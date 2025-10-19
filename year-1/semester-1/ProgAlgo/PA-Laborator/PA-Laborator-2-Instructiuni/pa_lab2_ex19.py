#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:49:36 2025

@author: fernandodonea
"""

n=int(input("n="))
nr=0
for i in range(0,10**n):
    ok=True
    x=i
    l=[]
    while x!=0:
        c=x%10
        l.append(c)
        x=x//10
    for j in range(0,10):
        k=l.count(j)
        if k>1:
            ok=False
    if ok==True:
        nr=nr+1
        
print(10**n-nr)




