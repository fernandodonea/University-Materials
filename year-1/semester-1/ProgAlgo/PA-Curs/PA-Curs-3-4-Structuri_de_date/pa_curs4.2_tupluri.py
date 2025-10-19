#tuplu - clasa tuple
#"lista imutabila"
t=(6,4,8)
print(t,type(t))
#t[0]=13 #eroare does not support item assignment
#nu putem modifica ce refera t[0]
t=([8,5],[9,11])
#pputem modifica valoarea obiectlui referit de t[0]
t[0][0]=123
print(t)

#parantezele pot lipsi
t=5,6
print(t,type(t))
x,y=1,2
x,y=y,x
t=()
t=(2) #nu este tuplu
print(t,type(t))
t=(2,) #tuplu cu un element
print(t,type(t))
t=tuple('abc')
print(t)
t=tuple([2])
print(t,type(t))
#toate metode,  totii operatori - de la liste in afara celor care modifica ob
#in, count,len, idex, feliere
#!!NU comprehensiune
t=[i*i for i in range(1,10)] #list
print(t,type(t))
print(sum(t))
print(sum(t))
t=(i*i for i in range(1,10)) #nu e tuple
print(t, type(t)) #este generator
#genereaza "la crere" elemente dupa regula din copmprehsion
print(next(t))
print(next(t))
print(sum(t))
print(sum(t)) #!!0



