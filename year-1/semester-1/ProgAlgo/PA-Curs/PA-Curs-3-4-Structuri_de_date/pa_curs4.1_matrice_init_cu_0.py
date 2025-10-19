#initializam o matrice de 0 de dimnesniuni n,m
print("var 1 - gresit")
n,m=2,3
a=[[0]*m]*n
print(a)
a[0][0]=1
print(a)
print("var 2 - corect")
a=[[0 for i in range(m)] for j in range(n)]
print(a)
a[0][0]=1
print(a)
print("var 3 - gresit")
a=[[0 for i in range(m)]]*n
print(a)
a[0][0]=1
print(a)
print("var 4")
a=[[0]*m for j in range(n)]
print(a)
a[0][0]=1
print(a)
#rec- var 2
#operatorii <,<=,==, != - element cu element
ls=[1,2,4]
ls2=[3,1]
print(ls<ls2) #!!compar element cu element, deci ls2 e mai mare
#deoarece ls2[0]>ls[0]
print([1,3]==[3,1]) #fals

#sort vs sorted
ls=[7,1,5]
ls_sort=sorted(ls) #returneaza o noua lista
print(ls_sort,ls) #ls nu se modifica
ls.sort(reverse=True) #!!!nu retunreaza, modifca ls
print(ls)
m=[[6,9],[3,1],[1,11]]
m.sort()
"""(elemente sunt liste corespunzatoare liniilor)
sunt comparate aceste liste => crescator dupa prima coloana 
prin interschimbare de linii"""
print(m)