"""
FUNCTII-continuare
"""
#domeniul de vizibilitate pentru o variabila

"""
La accesara valorii unei variabile- este cautata is spatiul local 
si apoi in global (cautata dupa regula LEGB - local, enclonsing, 
global, builtin)
"""
def f():
    #spatiul local
    print(x)

x=9 #spatiul global
f()

#la actualizare:
"""
o variabila incepe sa existe la prima atribuire
(este creata in spatiul (domeniul) unde se face atribuirea,
daca nu exista)
"""
def f():
   y=7 #devine variabila locala (este prima atribuire in local)
   print(y)
   print(locals())
y=8
f()
print(y)

#putem preciza spatiul(domeniul) in care se cauta o variabila la atriburie
def f():
   global z #la atribuire - z din global
   z=7
   print(z)
   print(locals())
z=8
f()
print(z)



