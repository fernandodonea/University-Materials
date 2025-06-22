### Cerinta
Pentru fiecare dintre programele de mai jos, supneți dacă sunt corecte. În caz afirmativ, spuneți ce afișează, în caz negativ spuneți ce nu este corect , de ce și ce ați corecta.

# Tutoriat 1

--> **pointeri, referinte, alocare dinamica**

-->introducere in POO – clase & obiecte , modificatori de acces si compunere

#### ex 1
```c++
#include<iostream>

using namespace std;

int main()

{

    int a=3,b=2;
    int *ptr_a=nullptr, *ptr_b;
    int& ref_a=a;

    ptr_a=&ref_a;
    ref_a=b;
    ptr_b=&b;
    b=5;
    ptr_b=&ref_a;
    ref_a=10;
    b=2;

    cout<<"ref_a: "<<ref_a<<endl;
    cout<<"a: "<<a<<endl;
    cout<<"b: "<<b<<endl;
    cout<<"*ptr_a: "<<*ptr_a<<endl;
    cout<<"*ptr_b: "<<*ptr_b<<endl;
    cout<<"ptr_a: "<<ptr_a<<endl;
    cout<<"ptr_b: "<<ptr_b<<endl;
    return 0;

}
```

#### Raspuns: Compileaza
```
ref_a: 10
a: 10
b: 2
*ptr_a: 10
*ptr_b: 10
ptr_a: 0x5ffe84 //adresa lui a
ptr_b: 0x5ffe84 //adresa lui a
```


#### ex 2
```c++
#include<iostream>

using namespace std;

int main()
{
    int a=3,b=5,c=8;
    int &ref_a=a, &ref_b, &ref_c=c;

    ref_a=ref_b;
    ref_c=ref_a;

    cout<<ref_b<<' '<<ref_c<<' '<<ref_a;

    return 0;
}
```
#### Raspuns: NU COMPILEAZA
Eroare la linia 8 : “reference variable "ref_b" requires an initializer”

Explicatie: Referintele trebuie mereu initializate in momentul declararii. Aici ref_b nu e initializata

**Modificare: Initializam referinta: 
```c++
&ref_b=b;
```


#### ex 3
```c++
#include<iostream>

using namespace std;

int f(int& x)
{
    x++;
    x*=2;
    return x;
}

int* g(int x) 
{
    x+=7;
    x/=2;
    return x; //nu compileaza -> functia g returneaza int* iar x e de tip int
}

int main()
{
    int x=5;
    f(x);
    cout<<x<<endl;
    g(x);
    cout<<x<<endl;
    return 0;
}
```

**Eroare la linia 16 : la return x; in functia g**
**Explicatie:**

**-x este de tip intreg (int), iar subprogramul returneaza un int* adica o adresa de memorie** **à incompatibilitatea tipului de date returnat.** 

**-Nu putem face conversie de la int la int* si invers.**

**Modificare: declaram antetul lui g : int g(int x);** **à adica il obligam sa returneze un int, nu un int***

#### ex 4
```c++
#include<iostream>

using namespace std;

int f(int& x)
{
    x++;
    x*=2;
    return x;
}

int g(int x)
{
    x+=7;
    x/=2;
    return x;
}

int main()
{
    int x=5;
    f(x);//x = 12
    cout<<x<<endl;
    g(x);
    cout<<x<<endl;
    return 0;
}
```
#### Raspuns: Compileaza
```
12
12
```
**Explicatie:**

**-se apeleaza  f ce are ca parametru un int&**

**-orice modificari vom face asupra parametrului x din f , vor fi vizibile si in main** **è x=5, il transmitem prin referinta in functia f . Dupa calcule … x=12 in f, dar si in main**

**-apoi apelam functia g ce are ca parametru un int**
**-avand in vedere ca nu e transmis prin referinta, x-ul din main nu va suferi modificari**

**-x-ul LOCAL din g va avea valorea 9, dar dupa ce incheiem subprogramul, acel x LOCAL inceteaza sa existe. Astfel, in urma apelului functiei g, x isi va pastra vechea valoare.**

**-x LOCAL != x din MAIN in acest caz**

