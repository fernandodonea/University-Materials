#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:50:27 2025

@author: fernandodonea
"""
#Subiectul 4 – metoda Backtracking (3 p.)
'''
Să se afișeze toate permutările mulțimii A = {1,2, ..., n}, 
unde n este un număr natural nenul .
'''

#n=int(input("n="))
#A=[int(x) for x in range(1,n+1)]
A=[15,34,2]
n=len(A)

x=[0]*(n+1)

def afisare():
    for i in range(1,n+1):
        print(A[x[i]-1],end=" ")
    print()

def solutie(k):
    return k==n

def verif(k):
    for i in range(1,k):
        if x[i]==x[k]:
            return False
    return True
def bkt(k):
    for i in range(1,n+1):
        x[k]=i
        if verif(k):
            if k==n:
                afisare()
            else:
                bkt(k+1)
bkt(1)