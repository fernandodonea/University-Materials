#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 19:16:16 2025

@author: fernandodonea
"""

'''
a) Se dă o sumă S şi n tipuri de monede având valorile v1, v2, ..., vn lei (un număr
nelimitat de valori de fiecare tip). Se cer toate modalitățile de plată a sumei S utilizând
aceste monede.
Exemplu: Pentru S=20 şi n=3 tipuri de monede, cu valorile v1=1, v2=5, v3=10 putem avea
următoarele modalități de plată (pentru fiecare monedă de la 1 la n se afișează numărul de
monezi de acest tip care se plătesc):
0, 2, 1 (0 monede de 1 leu, 2 de 5 lei şi 1 de 10 lei)
0, 0, 2
5, 1, 1
5, 3, 0
10, 0, 1
10, 2, 0
15, 1, 0
20, 0, 0
'''
s=int(input("s="))
v=[int(x) for x in input().split()]
n=len(v)

'''
1. Reprezentarea solutiei:
    x=x1,x2...,xn
    unde xk reprezentina cate monede de vk
2. Conditii interne(finale)
    
3. Conditii continuare:
    xk*vk<s

'''
x=[0]*n

def afisare():
    for i in range(n):
        print(x[i],end=" ")
    print()
    

def suma_curenta():
    suma=0
    for i in range(0,n):
        suma+=v[i]*x[i]
    return suma

def solutie():
    return s==suma_curenta()

def bkt(k):
    
    max_val=(s-suma_curenta())//v[k]
    for i in range(max_val+1):
        x[k]=i
        if k==(n-1):#am ajuns la ultima moneda:
            if solutie():
                afisare()
        else:
            bkt(k+1)
        x[k]=0
bkt(0)


            
    
    
    
    
