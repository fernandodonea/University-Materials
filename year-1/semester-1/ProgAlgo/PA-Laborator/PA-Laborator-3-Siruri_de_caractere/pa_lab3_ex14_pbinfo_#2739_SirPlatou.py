#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 22:24:35 2025

@author: fernandodonea
"""

'''

Se dă un șir de caractere care conține cuvinte. Cuvintele sunt formate din litere mici ale alfabetului englez și sunt separate prin unul sau mai multe spații.

Determinați secvențele de cuvinte de lungime maximă cu proprietatea că fiecare cuvânt din secvență, cu excepția ultimului, se termină cu litera de început a cuvântului următor. Secvențele au minim 2 cuvinte și se afișează în ordinea în care apar în șir.

Fiecare secvență determinată va fi afișată pe câte o linie a ecranului, cuvintele dintr-o secvență fiind separate prin atâtea spații cât sunt între ele în șir. Dacă nu există nicio astfel de secvență se va afișa -1.


intrare:
    
ab   bc  cd ef fg  gh

iesire:
    
ab   bc  cd
ef fg  gh
    
'''



s=input()
prop=s.split()
n=len(prop)
idk=[]
k=0
secv=[]
secv.append(prop[0])
for i in range(n-1):
    
    if prop[i][-1]==prop[i+1][0]:
        secv.append(prop[i+1])
    else:
        l=" ".join(secv)
        l=l.split()
        idk.append(l)
        
        secv.clear()
        secv.append(prop[i+1])

l=" ".join(secv)
l=l.split()
idk.append(l)
maxi=0
for i in idk:
    if len(i)>maxi:
        maxi=len(i)

if maxi<2:
    print(-1)

else:
    for i in idk:
        if len(i)==maxi:
            start=i[0]
            end=i[len(i)-1]
            
            a=s.find(start)
            b=s.find(end,a)+len(end)
            print(s[a:b])
        

        
            
        
        
        

