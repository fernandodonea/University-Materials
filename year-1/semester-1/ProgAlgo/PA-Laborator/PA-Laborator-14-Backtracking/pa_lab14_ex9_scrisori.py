'''

la bkt sunt importante conditiile de continuare si conditiile de solutie


folosim
- permutari cand vrem
- aranjamente cand vrem elemente distincte, lungimea sol<=m
- combinari cand vrem elemente distincte, lungimea sol<=m, si sunt ordonate crescatori
- produs cartezian (nu prea are conditii) lungimea sol depinde de numarul de submultimi?


ne trebuie 4 functii
-functia de bkt (ea pune chestii) verifica daca e ok, daca e solutie ->afisare
'''

'''
Un grup de n persoane distincte dorește să-și trimită scrisori între ele. Fiecare
persoană are pregătită o scrisoare, dar există o regulă strictă: nimeni nu trebuie să
primească propria scrisoare. Se cere să se determine toate modurile posibile de distribuire
a scrisorilor astfel încât regula să fie respectată. Fiecare distribuție va fi reprezentată ca o
corespondență între persoane și destinatarii lor, iar soluțiile trebuie afișate în ordine
lexicografică după numele persoanelor. De exemplu pentru datele:

Intrare: 
Ana Bogdan Carla

Iesire:
Ana - Bogdan Bogdan - Carla, Carla - Ana
Ana - Carla Bogdan - Ana Carla - Bogdan

ne gandim la permutari fara puncte fixe

1 2 3 x isi trimit scrisori singuri
1 3 2 x ana isi trimite singura
2 1 3 x carla singura
2 3 1 bun
3 1 2 bun
3 2 1 x bogdan singura

->deranjamente


'''

#mai intai facem permutari normale
'''
n=3

x=[0]*(n+1)


def ok(k):
    for i in range(1,k):
        if x[k]==x[i]:
            return False
    return True

def solutie(k):
    return k==n
def afisare():
    for i in range(1,n+1):
        print(x[i],end=' ')
    print()

def bkt(k):
    #k pozitia in bkt pe care o folosesc
    for i in range(1,n+1):
        x[k]=i
        if ok(k):
            if solutie(k):
                afisare()
            else:
                bkt(k+1)
bkt(1)

'''

#permutari fara puncte fixe
pers=input().split()

n=len(pers)


x=[0]*(n+1)


def ok(k):
    for i in range(1,k):
        if x[k]==x[i]:
            return False
    if x[k]==k:
        return False
    return True

def solutie(k):
    return k==n
def afisare():
    for i in range(1,n+1):
        #i-1 pentru ca lista e indexata de la 0
        print(f'{pers[i-1]}-{pers[x[i]-1]}',end=' ')

    print()

def bkt(k):
    #k pozitia in bkt pe care o folosesc
    for i in range(1,n+1):
        x[k]=i
        if ok(k):
            if solutie(k):
                afisare()
            else:
                bkt(k+1)
bkt(1)


a=1.254
a=round(a,2)
print(a)


a=1.2
print('{:.5f}'.format(a))



