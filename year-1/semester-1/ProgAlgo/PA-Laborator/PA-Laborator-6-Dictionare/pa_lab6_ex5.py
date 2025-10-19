#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:47:31 2025

@author: fernandodonea
"""

'''

a) Scrieți o funcție care primește ca parametru două nume de fișiere (variantă: un
număr variabil de nume de fișiere) și returnează un dicționar cu cuvintele care apar în cel
puțin unul dintre fișiere și frecvența totală cu care apare fiecare cuvânt (suma frecvențelor cu
care apar în fișiere). Cuvintele pot fi pe mai multe linii și pe o linie sunt separate prin spații.
b) Se consideră fișierele cuvinte1.in si cuvinte2.in. Să se afișeze cuvintele care apar în cel
puțin unul dintre fișiere ordonate crescător lexicografic
c) Se consideră fișierul cuvinte1.in. Să se creeze o listă de perechi (cuvinte, frecvențe) cu
cuvintele care apar în fișier și frecvența cu care apar, ordonată descrescător după frecvență
(folosind funcția de la a)).
d) Să se determine un cuvânt care apare cel mai des în cuvinte2.in, folosind funcția de la a) și
funcția max. Dacă sunt mai multe posibilități, se va afișa cuvântul cel mai mic din punct de
vedere lexicografic
'''

def citire_fisier(*f1):
    d={}
    for x in f1:
        fin=open(x,'r')
        
        
        lines=fin.readlines()
        for line in lines:
            for cuv in line.split():
                if cuv not in d:
                    d[cuv]=1
                else:
                    d[cuv]+=1
        fin.close()

    return d

d=citire_fisier("cuvinte1.in", 'cuvinte2.in')
print(d)

#b)
l=sorted(d)
print(*l)

#c)
d1=citire_fisier('cuvinte1.in')
l=[]
for x in d1:
    l.append((x,d1[x]))
l=sorted(l,key=lambda x:-x[1])
print(l)


#d)
d2=citire_fisier("cuvinte2.in")
l=[]
for x in d1:
    l.append((x,d1[x]))
l.sort(key=lambda x:x[0])
maxi=max(l,key=lambda x:x[1])
print(maxi[0])


#e)



def dcos(F1,F2):
    d1=citire_fisier(F1)
    d2=citire_fisier(F2)
    c=citire_fisier(F1,F2)
    suma=0
    s1=0
    s2=0
    
    for x in c:
        if x in d1 and x in d2:
            suma+=d1[x]*d2[x]
            s1+=d1[x]*d1[x]
            s2+=d2[x]*d2[x]
    
    rez=suma/((s1**0.5)*(s2**0.5))
    rez=round(rez,2)
    print(rez)

dcos("cuvinte1.in","cuvinte2.in")

    
    
    
    