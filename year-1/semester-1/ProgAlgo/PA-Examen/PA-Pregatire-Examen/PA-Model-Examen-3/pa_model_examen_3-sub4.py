#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 00:06:39 2025

@author: fernandodonea
"""

'''
 O țeavă cu lungimea de p metri (1 ≤ 𝑝 ≤ 50) trebuie să fie tăiată în cel puțin două
bucăți ale căror lungimi să fie divizori ai lungimii sale. De exemplu, o țeavă cu lungimea
de 4 metri poate fi tăiată în 4 bucăți de câte 1 metru, 2 bucăți de câte 2 metri sau 2 bucăți
de câte 1 metru și 1 bucată de 2 metri, dar nu poate fi tăiată într-o bucată de 1 metru și o
bucată de 3 metri (deoarece 3 nu este un divizor al lui 4). Scrieți un program Python care
să citească de la tastatură numărul natural p și afișează toate modalitățile distincte în care
poate fi tăiată corect o bară de lungime p metri, precum și numărul acestora. Două
modalități de tăiere se consideră identice dacă sunt formate din aceleași bucăți de țeavă,
dar în altă ordine. De exemplu, pentru o țeavă cu lungimea de 4 metri, modalitățile de
tăiere 1+1+2, 1+2+1 și 2+1+1 sunt considerate identice. (2.5 p.)

Exemplu:
Pentru 𝑝 = 6 trebuie afișate următoarele 7 modalități de tăiere (nu neapărat în această ordine):
1+1+1+1+1+1
1+1+1+1+2
1+1+1+3
1+1+2+2
1+2+3
2+2+2
3+3
Nr. modalitati: 7
'''
#p=int(input())
p=6

def divizori(x):
    l=[]
    for i in range(1,x//2+1):
        if x%i==0:
            l.append(i)
    return l
l=divizori(p)

x=[0]*(p+1)

def afisare(k):
    
    for i in range(1,k):
        print(x[i],end="+")
    print(x[k])

def suma_curenta(k):
    s=0
    for i in range(1,k+1):
        s+=x[i]
    return s

def solutie(k):
    return p==suma_curenta(k)

def verif(k):
    if x[k-1]>x[k]:
        return False
    else:
        return True

def bkt(k):    
    if k<=p:
        for i in l:
            x[k]=i
            if verif(k):
                if solutie(k)==True:
                    #b) if len(set(x[1:k+1])) == 2:
                        #afisare(k)
                    afisare(k)
                else:
                    bkt(k+1)
bkt(1)


        
        
