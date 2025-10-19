#SIRURI - continuare
#split - are si parametrul maxsplit = cate imparitire sa faca maxim
p="acesta este un exemplu"
lp=p.split(" ")
print(lp)
lp=p.split(" ",maxsplit=1)
print(lp)
#rsplit

#exemplu - pe o line de forma nume varsta. Sa se afiseze varsta e o linie, numele pe alta
p="Marinescu Ghemeci Ruxandra  36"
lp=p.rsplit(maxsplit=1)
print(lp)
print(int(lp[1]))
print(lp[0])

#exemplu coordonatele carteziebne si eticheta
p="3 7 acesta este un punct in plan"
ls=p.split(maxsplit=2)
x=int(ls[0])
y=int(ls[1])
eticheta=ls[2]
print(f"({x},{y}) are \"eticheta {eticheta}\"")
print(f'({x},{y}) are "eticheta {eticheta}" ')

#ord, chr
#caractere UNICODE
#Modificari -> obiect nou

#s=s.replace(sect,sect_noua,cate_aparitii) - v. laborator
s="un exemplu"
s1=s.replace("u","")
print(s1)
s2=s.replace("u","",1)
print(s2)
x="am mancat"
y="am "+"mancat"
print(x,y,id(x),id(y))
z=input()
w="am "+z
print(x,w,id(x),id(w))
x=w
print(x,w,id(x),id(w))