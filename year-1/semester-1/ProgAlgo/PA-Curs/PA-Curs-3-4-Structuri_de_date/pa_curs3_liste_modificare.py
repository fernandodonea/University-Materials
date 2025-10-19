"""
append(element) -> adaugarea elementului la final
extend(iterabil) -> adauga elementele din iterabil unul cate unul
    la finalul listei
"""
ls=[3,4]
ls.append(5)
print(ls)
ls.extend([7,8,9])
print(ls)
ls.append("abc")
print(ls)
ls.extend("abc")
print(ls)

#Modifcarea listei - cu felieri
"""
ls[i]=x
ls[i:j]=iterabil (care nu are neaparat aceeasi lungime cu secv ls[i:j]
ls[i:j:k]=iterabil (de aceeasi lungime)
"""
ls=[1,2,3,4]
ls[1:3]=[5]
print(ls)
ls=[1,2,3,4,5,6]
ls2=[11,12,13,14,15,16]
ls[::2]=ls2[::2]
print(ls)
#adaugarea unui element x in lista pe pozitia i
#insert(i,element)
ls=[6,8,9]
ls.insert(1,7)
print(ls)
ls[1:2]=[17] #inlocuirea ui ls[1]
print(ls)
ls[1:1]=[18] #inserare pe pozitia 1
print(ls)
#del ls[i:j]
#del ls[i]
#metode: pop(pozitie), insert(poz,element)
#liste - remove(x) - elimina doar prima aparitie a lui x din lista
ls=[1,2,3,4]
ls[2]=[]
print(ls)
ls[2:3]=[]
print(ls)
del ls[2]
print(ls)

ls=ls+[4] #NU
#copiere
l=[7,8]
l1=l #nume pentru aceeasi lista
l1[0]=9
print(l1,l)
l1=l.copy()
l1[0]=11
print(l1,l)
m=[[1,2],[4,5]]
m1=m.copy() #copiere superficiala -doar de referinta
m1[0][0]=13
print(m1)
print(m)



