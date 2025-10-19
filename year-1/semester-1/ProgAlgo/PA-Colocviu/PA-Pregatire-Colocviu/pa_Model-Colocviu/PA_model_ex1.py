#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:34:06 2025

@author: fernandodonea
"""

'''
[2 p.] 
Fișierul matrice.in conține elementele unei matrice cu cel puțin 3 coloane
(pe fiecare linie din fișier sunt elementele unei linii din matrice separate cu un spațiu).
Să se șteargă de pe fiecare linie câte 2 elemente astfel încât suma elementelor din
matricea rămasă să fie minimă. Să se scrie matricea obținută în fișierul matrice.out (pe
fiecare linie din fișier se vor scrie elementele unei linii din matrice separate prin câte un
spațiu).
'''

fin=open("matrice.in",'r')
fout=open("matrice.out",'w')
lines=fin.readlines()
a=[[int(x) for x in line.split()] for line in lines]
for i in range(len(a)):
    maxi=max(a[i])
    a[i].remove(maxi)
    maxi=max(a[i])
    a[i].remove(maxi)
for line in a:
    mystring=""
    for x in line:
        mystring+=" "+str(x)
    mystring=mystring.strip()
    fout.write(mystring+"\n")
    
