#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 23:30:43 2025

@author: fernandodonea
"""

'''
n=int(input("n="))
tipar=input("tipar")
l=[x for x in input()]
s=[x for x in input()]
'''
n=6
tipar="lslsll"
l=['a','b','c','D']
s=['@','.']

x=[0]*n

def afisare():
    for i in range(n):
        print(x[i],end="")
    print()
    
    
def solutie(k):
    return k==n-1

def verif(k):
    for i in range(0,k):
        if x[k]==x[i]:
            return False
    return True
    
def bkt(k):
    if tipar[k]=='l':
        posib=l
    else:
        posib=s
    
    for i in posib:
        x[k]=i
        if verif(k):
            if solutie(k):
                afisare()
            else:
                bkt(k+1)


lung_s=len(s)
lung_l=len(l)
for lit in tipar:
    if lit=='l':
        lung_l-=1
    else:
        lung_s-=1
if lung_s<0 or lung_l<0:
    print("imposibil")
else:
    bkt(0)
