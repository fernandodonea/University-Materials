#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:59:41 2025

@author: fernandodonea
"""

'''
În fișierul text “test.in” se află testul unui elev de clasa a II-a la matematică,
conținând 9 înmulțiri scrise pe rânduri distincte. Un calcul corect este notat cu un
punct, iar unul incorect cu 0 puncte. Să se realizeze un program care să evalueze
testul dat, astfel: în dreptul fiecărui calcul corect se va scrie mesajul ‘Corect’ , iar în
dreptul fiecărui calcul greșit se va scrie mesajul ‘Gresit’ și rezultatul corect, iar la
final se va scrie nota (un punct se acordă din oficiu!). Rezultatul evaluării testului
se va afișa în fișierul test.out
'''

fin=open("test.in",'r')
fout=open('test.out','w')

nota=1
lines=fin.readlines()

for line in lines:
    line=line.strip() #liniile au \n la final
    calcul,rez=line.split("=")
    
    rez=int(rez)
    c=0
    if "*" in calcul:
        a,b=calcul.split("*")
        a=int(a)
        b=int(b)
        c=a*b
    elif "+" in calcul:
        a,b=calcul.split("+")
        a=int(a)
        b=int(b)
        c=a+b
        
    elif "-" in calcul:
        a,b=calcul.split("-")
        a=int(a)
        c=a-b
    elif "/" in calcul:
        a,b=calcul.split("/")
        a=int(a)
        b=int(b)
        c=a//b
    if c==rez:
        fout.write(line+' corect\n')
        nota+=1
    else:
        fout.write(line+' gresit '+str(c)+'\n')
fout.write(str(nota)+'\n')
        


        
    
    