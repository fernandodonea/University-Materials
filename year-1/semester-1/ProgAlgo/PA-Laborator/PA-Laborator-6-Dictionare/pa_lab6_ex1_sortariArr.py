#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 18:25:59 2025

@author: fernandodonea
"""

'''
Sortarea unui vector după un criteriu - parametrul key
'''

v=[101,23,43,32,2,3,6,9]

v.sort()
print(v)
#sort aplica schimbarea pe vectorul nostru

b=sorted(v,reverse=True)
print(b)
#sorted face o copie -> nu modifica vectorul


#sortare dupa suma cifrelor
def sumcif(x):
    sum=0
    while x!=0:
        c=x%10
        sum+=c
        x=x//10
    return sum
c=sorted(v,key=sumcif)
print(c)


#sortare dupa numarul de cifre si in caz de egal descresc
def nrcif(x):
    k=0
    if x==0:
        k=1      
    while x!=0:
        k+=1
        x=x//10
    
    return k
d=sorted(v,reverse=True)
d=sorted(d,key=nrcif)
print(d)

#sortare dupa primalitate (numerele prime primele apoi cele neprime
def prim(w):
    if w<=1:
        return 1
    if w==2:
        return 0
    if w%2==0:
        return 1
    for i in range(3,w,2):
        if w%i==0:
            return 1
    return 0
e=sorted(d,key=prim)
print(e)

#sortaredupa divizibilitatea cu 3 (numere div primele) si in caz de egal cresc
def diviz_trei(z):
    if z%3==0:
        return 0
    else:
        return 100
f=sorted(v, reverse=True)
f=sorted(f,key=diviz_trei)
print(f)

#dupa prima cifra si in caz de egal descresc
def primcif(q):
    while q>9:
        q=q//10
    return q
g=sorted(v,reverse=True)
g.sort(key=primcif)
print(g)


        