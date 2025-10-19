#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:21:10 2025

@author: fernandodonea
"""

'''
Traseu SE: Se consideră o tablă de șah nxm (n,m date). Pe fiecare careul al tablei
este plasat câte un obiect, fiecare cu o anumită valoare (cunoscută, număr
natural). Pe tablă se deplasează un robot astfel: pornește de pe prima linie și
prima coloană (un colț al tablei) și se poate deplasa numai în direcțiile sud și est.
La parcurgerea unei celule robotul adună obiectul din celulă. Să se determine un
traseu al robotului până în poziția (n, m) (până în colțul opus celui din care a
plecat) astfel încât valoarea totală a obiectelor adunate să fie maximă. Se vor afişa
valoarea totală obţinută şi un traseu optim O(nm)

2 1 4    2  1
1 3 2       3
1 6 1       6  1





a[i][j]-->a[i][j]
        \
        \
        a[i+1][j+1]
            
               a[i-1][j-1] 
                |
                |
        a[i][j-1]-->a[i][j]

MATRICEA DE COSTURI

stim ca pornim din (0,0)
deci d[0][0]=a[0][0]

2 0 0
0 0 0
0 0 0


#pe prima coloana pot veni doar de sus
d[i][0]=d[i-1][0]+a[i][j]
2 0 0
3 0 0
4 0 0

#pe prima coloana putem veni doar din stanga
d[0][j]=d[0][j-1]+a[0][j]
2 3 7
3 0 0
4 0 0

#pt restul relatia de recurenta este
d[i][j]=a[i][j]+max{d[i-1][j],d[i][j-1]}
2 3 7
3 6 9
4 12 13




'''

#n=int(input("n="))
#m=int(int("m="))
n=3
m=3
a=[[2,1,4],[1,3,2],[1,6,1]]


'MATRICEA DE COSTURI'
d=[[0]*m for _ in range(n)]
d[0][0]=a[0][0]
#pe prima coloana putem veni doar din stanga
for i in range(1,n):
    d[i][0]=d[i-1][0]+a[i][0]
#pe prima coloana putem veni doar din stanga   
for j in range(1,m):
    d[0][j]=d[0][j-1]+a[0][j]

for i in range(1,n):
    for j in range(1,m):
        d[i][j]=a[i][j]+max(d[i-1][j],d[i][j-1])
print(d)

'CONSTRUIM DRUMUL'
path=[]
i,j=n-1,m-1
while i>=0 and j>=0:
    path.append((i+1,j+1))
    if d[i-1][j]>=d[i][j-1]:
        i=i-1
    else:
       j=j-1
path=path[::-1]
print(path)
    
    