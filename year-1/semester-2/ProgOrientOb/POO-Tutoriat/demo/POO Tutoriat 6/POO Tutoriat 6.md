# POO Tutoriat 5
9 apr 2025

## Polimorfism
### Polimorfism static
- early binding (facut la inceputul programului)
- destul de rigid
- se face la compilare

```c++
class D: public B
{
    ...
}
B obj;
D obj2;
B *p=new D;
```
```
|B|D|
 ^
 |
 p //se uita doar la baza
```
o derivata poate fi tratata ca un obiect de baza

### Instanta
```c++
    class B {...} // clasa
    B *p=new B;
//  ^        ^
//  |        |_____
//  instanta    obiect 
```
## Upcasting
- transformarea unui obiect derivat intr-unul de baza

## Downcasting
- transformarea unui obiect de baza intr-unul derivat
```
    A
/  \   \
B   C   D
|   \  / 
G    E
     |
     F
```

```c++
A *p=new G;
```

## Functii virtuale
- functii membre definite in clase de baza si apoi sunt redefinite (overrided) in clasele derivate

```c++
class B
{
    virtual void f(){cout<<"1";}
    void f(int a){cout<<a;}
}//supraincarcare

class D:public B
{
    void f(){cout<<"2";}
}//suprascriere
//OBS: in clasa derivata pierdem accesul la functia parametrizata din baza


B *p=new D;
p->f(); // 2

//daca nu defineam functia ca fiind virtuala in baza, se apela functia f() dn B
```
Exemplu 2
```
            drum
            /   \
          /        \
    autostrada     drum european 
         |              |
         130km          100km
```
Nu dorim sa facem doi vectori separati pentru fiecare tip de drum.
Facem un vector de baza unde putem apela pentru fiecare tip de drum functia virtuala pentru viteza.

# Precizari
- o functie virtuala nu poate fi statica
- o functie virtuala poate fi declarata ca fiind friend cu o alta clasa
- pentru a avea polimorfism la executie, functia virtuala trebubuie sa fie accesata ptrntr-un pointer sau referinta

**OBS** Constructorii NU pot fi virtuali,
dar destructorii DA!

De ce? Pentru a asigura distrugerea corecta a obiectelor derivate. 

## Early & late binding
**Binding**=procesul de convertire a identificatorilor (variabile, functii etc) in adresa de memorie. 

**Early binding**
- la momentul compilarii
- este un tip de compile time
- *build*

**Late binding**
- la momentul executarii
- este un tip de run time
- *run*

```
            Polimorfism
            /        \
    early binding   late binding
       /      \       
function
overloading
```

### Comparatie intre polimorfism static si dinamic
**Static**
- la compilare
- prin supradefinire, sabloane, operatori
- mai rapid


**Dinamic**
- la runtime
- prin functii virtuale
- mai lent

## Clase abstracte
- o clasa care contine cel putin o functie virtuala pura dar si alte componente
```c++
class Abstract
{
    int f(){...}
    virtual int functie()=0;//functie virtuala pura
}

```

**f()=0;**
 - "te declar dar nu faci nimic", doar o declari
 - nu putem instantia obiecte din aceasta clasa
 
## Interfete
- o clasa care contine doar functii virtuale pure
- functie de citire, de afisare, de cost, upgrade etc
```c++
class Interfata
{
    virtual int f()=0;
    virtual int functie()=0;
}
```
**OBS**: din interfata nu putem face nici macar pointeri

```c++
class B: public Abstract{...}

Abstract *p=new B;
```

**OBS:** Un pointer de tip baza poate stoca un obiect derivat, dar nu invers!.

**lista de intializare** aloca memoria si imi si pune valoarea
**componenta constructorului** ai deja memoria alocata 


6

21

3
