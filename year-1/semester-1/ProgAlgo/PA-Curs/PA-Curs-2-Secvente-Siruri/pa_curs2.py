# Instructiuni
# atribuire
x = y = 2
print(id(x), id(y))
x, y = 1, 2
print(x, y)
x, y = y, x  # de tupluri dreapta => tuplu, nu este echivalent cu x=y , y=x
print(x, y)

# if .. elif... else
# ultima cifra a lui 3**k
k = 8
if k % 4 == 0:
    print(1)
elif k % 4 == 1:
    print(3)
elif k % 4 == 2:
    print(9)
else:
    print(7)
# while
# for
# for var in secventa
s = "abc"
for litera in s:
    print(litera)
# range:
"""
range(n) -> 0,1,..n-1
range(a,b) -> a,a+1,...,b-1
range(a,b, pas)
"""
print(list(range(10, 1, -1)))
# break, continue
# else - si pentru structuri repetitive (se executa daca nu s-a iesit cu break)
"""
Sa se afiseze primul divizor propriu al lui n
"""
n = 25
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        print(i)
        break
else:
    print("nu are divizori proprii")

# pass
i = 0
for i in range(0, 4):
    print(i)
    # i=i+1
print(i)
