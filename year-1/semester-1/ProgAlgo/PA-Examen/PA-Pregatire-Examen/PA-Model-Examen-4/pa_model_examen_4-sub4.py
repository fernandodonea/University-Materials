#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 00:35:16 2025

@author: fernandodonea
"""
#sub4


'''
a) Un număr natural se numește p-mărginit (0 ≤ 𝑝 ≤ 9) dacă valoarea absolută a
diferenței dintre oricare două cifre ale sale este cel mult egală cu p. De exemplu, numărul
27383 este 6-mărginit, iar numărul 2022 este 2-mărginit. Scrieți un program Python care
să citească de la tastatură numerele naturale p și c, după care afișează toate numerele
naturale p-mărginite formate din cifre nenule având suma cifrelor egală cu c sau mesajul
"Imposibil" dacă nu există niciun astfel de număr. (2.5 p.)
'''

p=3
c=6

x=[0]*(c+1)

def afisare(k):
    if x[1]==x[k]:
        for i in range(1,k+1):
            print(x[i],end="")
        print()
    
def suma_curenta(k):
    s=0
    for i in range(1,k+1):
        s+=x[i]
    return s

def solutie(k):
    return suma_curenta(k)==c

def verif(k):
    for i in range(1,k):
        if abs(x[i]-x[i+1])>p:
            return False
    return True

def bkt(k):
    if k<=c:
        for i in range(1,10):
            x[k]=i
            if verif(k):
                if solutie(k):
                    afisare(k)
                else:
                    bkt(k+1)
bkt(1)


