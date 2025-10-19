#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 22:30:07 2025

@author: fernandodonea
"""

'''
Scrieți o funcție cu număr variabil de parametri care să caute un cuvânt dat în mai
multe fișiere text. Funcția va scrie într-un fișier text câte o linie pentru fiecare fișier
text de intrare, astfel: numele fișierului text de intrare și apoi numerele de ordine ale
liniilor pe care apare cuvântul dat în acel fișier (numerotate de la 1) sau un mesaj
corespunzător dacă fișierul nu conține cuvântul respectiv. Antetul funcției va fi:
cautare_cuvant(cuv, nume_fis_out, *nume_fis_in). Se vor număra aparițiile
cuvântului fără a face diferența între literă mare și literă mică. De exemplu, prin
apelul cautare_cuvant("floare","rez.txt", "eminescu.txt", "paunescu.txt") se va
căuta cuvântul “floare” în fișierele text “eminescu.txt” și “paunescu.txt”, iar rezultatul
căutării va fi scris în fișierul text “rez.txt”.
'''

def cautare_cuvant(cuv, nume_fis_out, *nume_fis_in):
    cuv=cuv.lower()
    fout=open(nume_fis_out,'a')
    for fisier in nume_fis_in:
        l=[]
        fin=open(fisier,'r')
        lines=fin.readlines()
        n=len(lines)
        for i in range(n):
            line=lines[i]
            line=line.lower()
            if cuv in line:
                l.append(i+1)
       
        x=" ".join(map(str,l))
        
        rez=fisier
        rez+=" "+x
        fout.write(rez+'\n')
        
        fin.close()
    
    fout.close()
        
        

cautare_cuvant('floare', "rez.txt", "eminescu.txt","paunescu.txt")