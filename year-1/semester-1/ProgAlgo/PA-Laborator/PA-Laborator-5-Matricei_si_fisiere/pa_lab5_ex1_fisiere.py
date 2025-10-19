#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:45:20 2025

@author: fernandodonea
"""

'''
Să se copieze conținutul unui fișier text în alt fișier 
folosind diferite funcții de citire din fișier 
-read 
-readline
-readlines
-iterarea liniilor cu for)
'''
fin=open("date.in",'r')
fout=open("date.out",'w')

content=fin.read()


# !!! functie fout.write merge doar pe stringuri
fout.write(content)
fin.close()
fout.close()

#ff important sa inchidem fisierul !!! SE SCAD 25 DE SUTIMI LA TEST

fin=open("date.in",'r')
fout=open("date.out",'w')

#citeste prima linie
content=fin.readline()
while content:
    print(content, end=" ")
    fout.write(content)
    content=fin.readline()
    
fin.close()
fout.close()

fin=open("date.in",'r')
fout=open("date.out",'w')

'face fiecare linie un element al unei liste'
content=fin.readlines()
print(content)
for line in content:
    line=line.strip()
    print(line)
fin.close()
fout.close()
    

