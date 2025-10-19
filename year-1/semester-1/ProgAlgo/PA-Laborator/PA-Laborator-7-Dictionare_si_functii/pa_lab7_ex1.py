#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 21:47:16 2025

@author: fernandodonea
"""

'''
a) Scrieți o funcție care să citească de la tastatură o listă cu elemente numere întregi.
Numărul de elemente ale listei și elementele sale se vor citi în cadrul funcției

b) Scrieți o funcție care primește ca parametru o secvență s, un element x și, opțional,
doi indici i și j și returnează poziția primului element mai mare decât x din s[i:j] (dacă
i sau j nu se specifică, atunci comportamentul va fi cel de la feliere) și -1 în caz că nu
există un astfel de element.

c) Scrieți un program care, folosind apeluri utile ale funcției definite anterior, afișează
mesajul "Da" în cazul în care o listă de numere întregi, citită de la tastatură, este
sortată strict descrescător sau mesajul "Nu" în caz contrar. Aceeași cerință și pentru o
listă de cuvinte.
'''

#a)

def citire():
    n=int(input())
    l=[int(x) for x in input().split()]
    return n,l

    
#b)

def indici(s,x,i=None,j=None):
    
    if i==None:
        i=0
    if j==None:
        j=len(s)
    
    for k in range(i,j):
        if s[k]>x:
            return k
    return -1

n,s=citire()
ok=True
for i in range(n-1,0,-1):
    if(indici(s, s[i],i-1,i)==-1):
        print("nu e descresc")
        ok=False
        break
        
if ok==True:
    print("sir descrescator")
    
    
    



    
    
    
    
    
    
    
    
