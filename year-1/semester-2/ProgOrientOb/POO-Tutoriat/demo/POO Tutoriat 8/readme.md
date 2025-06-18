# Tutoriat 8
14 mai 2025

```clasa```=o structura de date care contine atribute si metoide

```obiect```= instanta unei clasei

## Principii POO:
- mostenire
- incapsulare (ascudem datele unei clase -> utilizatorul nu trebuie sa aiba acces direct)
- polimorfism (o functie poate sa aiba mai multe implementari)
- abstractizare (ideea de defini un comportament generic, tipic, fara a specifica detalliile implementarii)

## Modificatori de acces
- public (accesibil din afara clasei)
- private (accesibil doar din interiorul clasei)
- protected (accesibil din interiorul clasei si din clasele derivate)

## Tipul CONST
```c++
class A
{
    const int func(const int x) const {...}
}
```
primul const -> returneaza o variabila constanta
al doilea const -> 
al treilea const -> promite ca nu se va modifica nimic in interiorul functiei

variabilele constante subt obligate sa fie initializate (de ex in lista de intializare a constructorului)


## Tipul STATIC
```c++
class A:
{
    static int x;
    static int func(){...}

    int y;
    void func();
}
int A::x=100; //initializarea globala
```
datele statice apartin clasei, nu instatei

variabilele statice nu pot fi initializare in lista de initializare deoarce se aloca memorie, dar memoria este deja alocata



## Constructori
Constructori = functii care se apeleaza automat la crearea unui obiect

Tipuri de constructori:
- constructori impliciti (fara parametrii)
- constructori cu parametrii
- constructori de copiere (constructori care initializeaza un obiect cu un alt obiect de acelasi tip)

Destructorul
- nu are parametrii
- recomandat sa fie virtual (in ideea de mostenire)
- este unic


In lista de intializare se aloca memorie si se si intializaza 
In corpul constructorului se initializeaza datele

```c++
class A
{
    private:
        int x;
    public:
        A(){x=0;}
        A(int x){this->x=value;}
        A(const A &a){this->x=a.x;}

        virtual ~A();
}

class B: public A
{
    private:
        int y;
    public:
        B(){y=0;}
        ~B();
}
```
```c++
A* a =new B()
delete a;
```
daca nu declaram destructorul virtual, se va apela doar destructorul clasei de baza

## Supraincarcare

```Supraincarcare```= proprietatea unei functii de se comporta difeerit in functie de ce paremtrii primeste

```c++
void f(){}
void f(int a){}
void f(string str){}
=>POLIMOFRISM LA COMPILARE
```
Diferenta intre functie => doar numarul sau tipul de parametrii

## Suprascriere
```Suprascriere```= proprietatea unei functii de a avea aceeasi semnatura ca o alta functie dintr-o clasa de baza
```c++
class A
{
    int f();
}
class B: public A
{
    string f();
}
```
POLIMORFISM LA EXECUTIE

## Problema diamantului
=>mostenire virtuala
```
          A
      x  / \ x
        B   C
    x,y  \ / x,z
          D
        x,y,z
```
```c++
class A
{
    int x;

}
class B: virtual public A
{
    int y;

}
class C: virtual public A
{
    int z;

}
class D: public B, public C
{

}
```

Partea de ambiguitate nu apare la functii, ci la datele membre.

**Solutie** Mostenire virtuala


Pentru a accesa ambele variable, folosim operatorul de rezolutie
```c++
B::x;
C::x;
```

## Clase abstracte si interfete

```c++
class Abstract
{
    int x;
    public:
        virtual void f()=0; //f este o functie pura
}
```
- o ```clasa abstracta``` este o clasa care contine **CEL PUTIN** o functie pura, dar nu numai



```c++
class Interface
{
    public:
        virtual void f()=0;
        virtual void func()=0;
        virtual void func2()=0;
}
```
- o ```interfata``` este o clasa care contine **DOAR** functii pure


Arbore de mostenire
```
          Interfata (de input, output)
                |
                |
            Abstracta ( Obiecte generice)
         /      |      \    (clase specifice)
        ...    ...    ...
           \  /
        
```
Clasa abstracta are scopul de a nu putea instantia obiecte generice.

## Template
- mecanisme care permit crearea de functii ce permit lucrarea cu tipuri de date diferite
=> POLIMORFISM LA COMPILARE

Template generic
```c++
template <typename T> void f(T x)
//SAU
template <class T> void f(T x)
```

Template specializat
```c++
template <> void f(int x) { ...}
```

Functie specializata
```c++
void f(int x) { ...}
```

**Ordine de apelare** a unei functii:
1. Functia normala
2. Functia specializata
3. Functia template generic
4. Daca nu gaseste, eroare de compilare


Apelare
```
f() => functia normala
f<>() => functia template specializata
```
**OBS**: numarul ```2.3``` este by default DOUBLE, nu este FLOAT