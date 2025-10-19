x=1
print(x, type(x))
x="abd"
print(x, type(x))
if x=="abc":
    print("nu")#plint("nu")
else:
    print("da",end=" ") #end - ce sir foloseste ca final, implicit-endline
    print("pauza")
print(x,"un sir", sep="=") #sep implicit spatiu
print(x,"un sir", sep=" este ") #sep implicit spatiu
x=input("dati x ") #str -pana la finalul liniei
x=int(x)
y=input("dati y ")
y=int(y)
print(x+y)


