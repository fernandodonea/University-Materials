#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:39:15 2025

@author: fernandodonea
"""

fin=open("nrdiv.in",'r')
fout=open("nrdiv.txt",'w')
n=int(fin.readline())

k=0
for i in range(1,n+1):
    if n%i==0:
        k+=1


print(k)

fout.close()
fin.close()

