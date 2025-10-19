#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:42:14 2025

@author: fernandodonea
"""

#subiectul 1


#a) 1.5 p
'''
Scrieți o funcție divizori care primește un număr variabil de parametri numere
naturale și returnează pentru fiecare număr primit ca parametru lista divizorilor săi
primi sub forma unui dicționar cu perechi de forma număr: lista divizorilor. De exemplu,
pentru apelul divizori(50, 21) funcția trebuie să furnizeze dicționarul {50: [2,5], 21: [3,7]}.
'''

def divizori(*numere):
    d={}
    for numar in numere:
        l=[]
        for i in range(2,numar//2+1):
            ok=1
            if numar%i==0:
                if i%2==0:
                    ok=0
                if i==2:
                    ok=1
                for j in range(3,i//2+1,2):
                    if i%j==0:
                        ok=0
                if ok==1:
                    l.append(i)
        d[numar]=l
    return d
print(divizori(50,21))


#b) 0.5 p
'''
b) Înlocuiți punctele de suspensie din instrucțiunea litere_10 = […] cu o expresie astfel
încât lista să fie inițializată cu primele 10 litere mici din alfabetul englez. (0.5 p.)
'''
litere_10=[chr(ord('a')+i) for i in range(10)]
print(litere_10)

#c) 1 p
'''
c) Considerăm o funcție recursivă a cărei complexitate este dată de următoarea relație de
recurență:
T(1) = T(2) = 1
T(n) = T(n/3) + 2, pentru n ≥ 1
Determinați complexitatea funcției respective. 
'''


'''
n=3^k, k=log3n
T(n)=T(n/3)+2
    =t(n/(3^2))+2+2
    =T(n/(3^3))+2+2+2
    ...
    =T(n/(3^k))+2*k
    =T(1)+2*log3n
    =O(logn)



'''