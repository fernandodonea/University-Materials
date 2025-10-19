#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 22:23:08 2025

@author: fernandodonea
"""

'''
a) Scrieți o funcție cu număr variabil de parametri care să furnizeze numărul natural
obținut prin alipirea cifrelor maxime ale numerelor naturale nenule primite ca
parametri. De exemplu, pentru numerele 4251, 73, 8 și 133 funcția trebuie să
returneze numărul 5783.

b) Scrieți o funcție cu 3 parametri nenuli de tip întreg a,b și c care să verifice dacă
aceștia pot fi considerați ca fiind numere scrise în baza 2 sau nu, folosind apeluri utile
ale funcției definite anterior. De exemplu, pentru numerele 1001, 11 și 100 funcția
trebuie să returneze valoarea True, iar pentru numerele 1001, 17 și 100 trebuie să
returneze valoarea False.
'''

#a)

def alipire(*numere):
    rez=""
    for x in numere:
        y=x
        maxi=0
        while y!=0:
            c=y%10
            if c>maxi:
                maxi=c
            y=y//10
        rez+=str(maxi)
    rez=int(rez)
    return rez

print(alipire(4251,73,8,133))

#b)

def binar(a,b,c):
    d=alipire(a,b,c)
    print(d)
    while(d!=0):
        if d%10!=1:
            return False
        d=d//10
    return True

print(binar(100,1010,117))