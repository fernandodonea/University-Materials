[link](https://oopquiz.fly.dev/index.php?id=1)

# ex 1
```c++
#include <iostream>
using namespace std;
class cls1
{
protected:
    int x;

public:
    cls1() { x = 13; }
};
class cls2 : public cls1
{
    int y;

public:
    cls2() { y = 15; }
    int f(cls2 ob) { return (ob.x + ob.y); }
};
int main()
{
    cls2 ob;
    cout << ob.f(ob);
    return 0;
}
```
#### Compileaza
```
28
```


# ex 2
```c++
#include <iostream>
using namespace std;

class A {
    static int x;//fie stergem static si lasam `int x`

public:
    A(int i = 0) { x = i; }
    int get_x() { return x; }
    int& set_x(int i) { x = i; }
    A operator=(A a1)
    {
        set_x(a1.get_x());
        return a1;
    }
};
//adaugam `int A::x;`
int main()
{
    A a(212), b;
    cout << (b = a).get_x();
    return 0;
}
```
#### NU Compileaza
Variabila `static int x` nu este initializata.


# ex 3
```c++
#include<iostream>
using namespace std;

class A
{ int i;
  public: A(int x=2):i(x+1) {}
  virtual int get_i() { return i; }};
class B: public A
{ int j;
  public: B(int x=20):j(x-2) {}
  virtual int get_j() {return A::get_i()+j; }};
int main()
{ A o1(5);
  B o2;
  cout<<o1.get_i()<<" ";
  cout<<o2.get_j()<<" ";
  cout<<o2.get_i();
  return 0;
}
```
#### Compileaza
```
6 21 3
```

# ex 4
```c++
#include <iostream>
using namespace std;
class problema {
    int i;

public:
    problema(int j = 5) { i = j; }
    void schimba() { i++; }
    void afiseaza() { cout << "starea curenta " << i << "\n"; }
};
problema mister1() { return problema(6); }
void mister2(problema& o)//stergem referinta
{
    o.afiseaza();
    o.schimba();
    o.afiseaza();
}
int main()
{
    mister2(mister1());
    return 0;
}
```
#### NU Compileaza
Expicatie: functia `mister2` primeste ca paramtru un obiect de tip `problema` cu referinta, iar functia `mister1` nu returneaza o adresa de memorie, ci doar valoarea.

# ex 5
```c++
#include <iostream>
using namespace std;
//ordinea constructorilor
class B
{
    int i;

public:
    B() { i = 1; }
    virtual int get_i() { return i; }
};
class D : virtual public B
{
    int j;

public:
    D() { j = 2; }
    int get_i() { return B::get_i() + j; }
};
class D2 : virtual public B
{
    int j2;

public:
    D2() { j2 = 3; }
    int get_i() { return B::get_i() + j2; }
};
class MM : public D, public D2
{
    int x;

public:
    MM() { x = D::get_i() + D2::get_i(); }
    int get_i() { return x; }
};
int main()
{
    B *o = new MM();
    cout << o->get_i() << "\n";
    MM *p = dynamic_cast<MM *>(o);
    if (p)
        cout << p->get_i() << "\n";
    D *p2 = dynamic_cast<D *>(o);
    if (p2)
        cout << p2->get_i() << "\n";
    return 0;
}
```
#### Compileaza
```
7
7
7
```

# ex 6
```c++
#include <iostream>
using namespace std;
class B {
    int x;

public:
    B(int i = 7) { x = i; }
    int get_x() { return x; }
    operator int() { return x; }
};
class D : public B {
public:
    D(int i = -12)
        : B(i)
    {
    }
    D operator+(D a) { return get_x() + a.get_x() + 1; }
};
int main()
{
    D a;
    int b = 18;
    b += a;
    cout << b;
    return 0;
}
```
#### Compileaza
```
6
```

# ex 7
```c++
#include <iostream>
using namespace std;
#include <typeinfo>
class B {
    int i;

public:
    B() { i = 1; }
    int get_i() { return i; }
};
class D : B { // modifcam aici `class D : public B`
    int j;

public:
    D() { j = 2; }
    int get_j() { return j; }
};
int main()
{
    B* p = new D;//aici crapa
    cout << p->get_i();
    if (typeid((B*)p).name() == "D*")
        cout << ((D*)p)->get_j();
    return 0;
}
```
#### NU compileaza
Eroare la linia ` B* p = new D;` B este o baza inaccesibila in D;

# ex 8
```c++
#include <iostream>
using namespace std;
class B {
protected:
    int x;

public:
    B(int i = 28) { x = i; }
    virtual B f(B ob) { return x + ob.x + 1; }
    void afisare() { cout << x; }
};
class D : public B {
public:
    D(int i = -32)
        : B(i)
    {
    }
    B f(B ob) { return x + ob.x - 1; }//aici crapa -> modificam `return x-1;`
};
int main()
{
    B *p1 = new D, *p2 = new B, *p3 = new B(p1->f(*p2));
    p3->afisare();
    return 0;
}
```

#### NU compileaza
Functia `D::B(f ob)` nu are acces la `ob.x`( x fiind camp protected, dar considerat ca privat pt alte obiecte


# ex 9
```c++
#include <iostream>
using namespace std;
class B {
protected:
    static int x;
    int i;

public:
    B()
    {
        x++;
        i = 1;
    }
    ~B() { x--; } //!!! Destructorul nu este virtual -> se apeleaza doar b
    static int get_x() { return x; }
    int get_i() { return i; }
};
int B::x;
class D : public B {
public:
    D() { x++; }
    ~D() { x--; }
};
int f(B* q)
{
    return (q->get_x()) + 1;
}
int main()
{
    B* p = new B[10];
    cout << f(p);
    delete[] p;
    p = new D;
    cout << f(p);
    delete p;//se apeleaza doar destructorul din B, cel din D nu!!
    cout << D::get_x();
    return 0;
}
```
#### Compileaza
```
1331
```

# ex 10
```c++
#include <iostream>
using namespace std;
template <class T, class U>
T f(T x, U y)
{
    return x + y;
}
int f(int x, int y)
{
    return x - y;
}
int main()
{
    int *a = new int(3), b(23);
    cout << *f(a, b);// afiseaza valoarea de memorie de la adresa a+23*sizeof(int) 
    //care pt inturi by defualt e 0
    return 0;
}
```
#### Compileaza
```
0
```

# ex 11
```c++
#include <iostream>
using namespace std;
class A {
    int x;

public:
    A(int i = 0) { x = i; }
    A operator+(const A& a) { return x + a.x; }
    template <class T>
    ostream& operator<<(ostream&);
};
template <class T>
ostream& A::operator<<(ostream& o)
{
    o << x;
    return o;
}
int main()
{
    A a1(33), a2(-21);
    cout << a1 + a2; //aici crapa
    //inlocuim cu (a1+a2).operator<<<A>(cout);
    return 0;
}
```
#### NU compileaza
Functia template `template <class T> ostream& A::operator<<(ostream& o)` este apelate de obiect de un obiect de tip A.
- `(a1+a2)`-> facem un obiect de tip A
- `.operator<<` -> apelam operatorul 
- `<A>` -> specializarea template
- `(cout)` - parametrul de tip ostream in care afisam 

# ex 12
```c++
#include <iostream>
using namespace std;
class cls {
    int x;

public:
    cls(int i) { x = i; }//`cls(int i=0){x=i;}
    int set_x(int i)
    {
        int y = x;
        x = i;
        return y;
    }
    int get_x() { return x; }
};
int main()
{
    cls* p = new cls[10];//aici crapa
    int i = 0;
    for (; i < 10; i++)
        p[i].set_x(i);
    for (i = 0; i < 10; i++)
        cout << p[i].get_x();
    return 0;
}
```
#### Nu compileaza 
Dupa ce am supraincarcat constructorul, nu mai avem **constructor default** (necesar pentru crearea de array-uri)


# ex 13
```c++
#include <iostream>
using namespace std;

int f(int y)
{
    try
    {
        if (y > 0)//2>0
            throw y;
    }
    catch (int i)
    {
        throw;//arunca i=2
    }
    return y - 2;
}
int f(int y, int z)
{
    try
    {
        if (y < z)
            throw z - y;
    }
    catch (int i)
    {
        throw;
    }
    return y + 2;
}
float f(float &y)
{
    cout << " y este referinta";
    return (float)y / 2;
}
int main()
{
    int x;
    try
    {
        cout << "Da-mi un numar par: ";
        cin >> x; //se va citi numarul 2
        if (x % 2)
            x = f(x, 0);
        else
            x = f(x);//aici va merge
        cout << "Numarul " << x << " e bun!" << endl;
    }
    catch (int i)//prinde i=2 din functia f
    {
        cout << "Numarul " << i << " nu e bun!" << endl;
    }
    return 0;
}
```
#### Compileaza
```
Da-mi un numar par: Numarul 2 nu e bun!
```
# ex 14
```c++
#include <iostream>
using namespace std;

class A {
    int x;

public:
    A(int i) { x = i; }
    int get_x() { return x; }
    int& set_x(int i) { x = i; }
    A operator=(A a1)
    {
        set_x(a1.get_x());
        return a1;
    }
};
class B : public A {
    int y;

public:
    B(int i)//B(int i=0)
        : A(i)
    {
        y = i;
    }
    void afisare() { cout << y; }
};
int main()
{
    B a(112), b, *c;
    cout << (b = a).get_x();
    (c = &a)->afisare();
    return 0;
}
```
#### NU compileaza
Atunci cand vrem sa cream obiectul `b`, nu avem constructorul default.

# ex 15
```c++
#include <iostream>
using namespace std;

struct cls {
    int x;

public:
    int set_x(int i)
    {
        int y = x;
        x = i;
        return x;
    }
    int get_x() { return x; }
};
int main()
{
    cls* p = new cls[100];
    int i = 0;
    for (; i < 50; i++)
        p[i].set_x(i);
    for (i = 5; i < 20; i++)
        cout << p[i].get_x() << " ";
    return 0;
}
```
#### Compileaza
```
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
```

# ex 16
```c++
#include <iostream>
using namespace std;

class A {
protected:
    int x;

public:
    A(int i = 14) { x = i; }
};
class B : A {
public:
    B()
        : A(2)
    {
    }
    B(B& b) { x = b.x - 14; }
    void afisare() { cout << x; }
};
int main()
{
    B b1, b2(b1);
    b2.afisare();
    return 0;
}
```
#### Compileaza
```
-12
```

# ex 17
```c++
#include <iostream>
using namespace std;

class A {
protected:
    static int x;

public:
    A(int i = 0) { x = i; }
    virtual A schimb() { return (7 - x); }
};
class B : public A {
public:
    B(int i = 0) { x = i; }
    void afisare() { cout << x; }
};
int A::x = 5;
int main()
{
    A* p1 = new B(18);
    *p1 = p1->schimb();
    ((B*)p1)->afisare();
    return 0;
}
```
#### Compileaza
```
-11
```

# ex 18
```c++
#include <iostream>
using namespace std;

template <class T, class U>
T fun(T x, U y)
{
    return x + y;
}
int fun(int x, int y)
{
    return x - y;
}
int fun(int x)
{
    return x + 1;
}
int main()
{
    int *a = new int(10), b(5);
    cout << fun(a, b);//apeleaza int* fun(int *a, int b) ->returneaza pointer
    //->a+b =>aritmetica pe pointeri
    return 0;
}
```
#### Compileaza
```
a+5*sizeof(int)
```

# ex 19
```c++
#include <iostream>
using namespace std;

class B {
protected:
    int x;

public:
    B(int i = 12) { x = i; }
    virtual B f(B ob) { return x + ob.x + 1; }
    void afisare() { cout << x; }
};
class D : public B {
public:
    D(int i = -15)
        : B(i - 1)
    {
        x++;
    }
    B f(B ob) { return x - 2; }
};
int main()
{
    B *p1 = new D, *p2 = new B, *p3 = new B(p1->f(*p2));
    p3->afisare();
    return 0;
}
```
#### Compileaza
```
-17
```

# ex 20
```c++
#include <iostream>
using namespace std;

struct B {
    int i;

public:
    B() { i = 1; }
    virtual int get_i() { return i; }
} a;
class D : virtual public B {
    int j;

public:
    D() { j = 2; }
    int get_i() { return B::get_i() + j; }
};
class D2 : virtual public B {
    int j2;

public:
    D2() { j2 = 3; }
    int get_i() { return B::get_i() + j2; }
};
class MM : public D2, public D {
    int x;

public:
    MM() { x = D::get_i() + D2::get_i(); }
    int get_i() { return x; }
};


///eroare aici
//inlocuim `{` cu `void f(){`
{
    MM b;
}


int main()
{
    B* o = new MM();
    cout << o->get_i() << "\n";
    MM* p = dynamic_cast<MM*>(o);
    if (p)
        cout << p->get_i() << "\n";
    D* p2 = dynamic_cast<D*>(o);
    if (p2)
        cout << p2->get_i() << "\n";
    return 0;
}
```
#### NU compileaza
Eroare expected unqualified id before `{` token

# ex 21
```c++
#include <iostream>
using namespace std;

class A {
public:
    int x;
    A(int i = -13) { x = i; }
};
class B : virtual public A {
public:
    B(int i = -15) { x = i; }
};
class C : virtual public A {
public:
    C(int i = -17) { x = i; }
};
class D : virtual public A {
public:
    D(int i = -29) { x = i; }
};
class E : public B, public D, public C {
public:
    int y;
    E(int i, int j)
        : D(i)
        , B(j)
    {
        y = x + i + j;
    }
    E(E& ob) { y = ob.x - ob.y; }
};
int main()
{
    E e1(5, 10), e2 = e1;
    cout << e2.y;
    return 0;
}
```
#### Compileaza
```
-15
```

# ex 22
```c++
#include <iostream>
using namespace std;
#include <typeinfo>

class B {
    int i;

public:
    B(int x) { i = x + 1; }
    int get_i() { return i; }
};
class D : public B {
    int j;

public:
    D()
        : B(1)
    {
        j = i + 2;//aici crapa
    }
    int get_j() { return j; }
};
int main()
{
    B* p = new D[10];
    cout << p->get_i();
    if (typeid((B*)p).name() == "D*")
        cout << ((D*)p)->get_j();
    return 0;
}
```
#### NU compileaza
Membrul `i` din clasa B este private, deci nu avem acces la el din clasa D

# ex 23
```c++
#include <iostream>
using namespace std;

class B {
protected:
    static int x;
    int i;

public:
    B()
    {
        x++;
        i = 1;
    }
    ~B() { x--; }
    static int get_x() { return x; }
    int get_i() { return i; }
};
int B::x;
class D : public B {
public:
    D()
    {
        x++;
        i++;
    }
    ~D()
    {
        x--;
        i--;
    }
    int f1(B o) { return 5 + get_i(); }
};
int f(B* q)
{
    return (q->get_x()) + 1;
}
int main()
{
    B* p = new B[10];
    cout << f(p);
    delete[] p;
    p = new D;
    cout << p->f1(p);//aici crapa
    delete p;
    cout << D::get_x();
    return 0;
}
```
#### NU compileaza
Pointerul de tip B nu are niciun membru de `f1` -> comentam linia

# ex 24
```c++
#include <iostream>
#include <typeinfo>
using namespace std;

class A
{
    int n;

public:
    A(int x) { n = x; }
    void afis() { cout << n; }
};
int main()
{
    A v[] = {*(new A(3)), *(new A(7))};
    v[0]->afis();//aici crapa
    //v[0].afis();
    return 0;
}
```
#### Nu compileaza
Vectorul `v` are elemente de tip `A`, nu `A*` (`*{new A(3)}` diferentiaza pointerii si adauga in array doar valoarea)

# ex 25
```c++
#include <iostream>
using namespace std;
class A {
    static int x;//aici crapa

public:
    A(int i = 0) { x = i; }
    int get_x() { return x; }
    int& set_x(int i) { x = i; }
    A operator=(A a1)
    {
        set_x(a1.get_x());
        return a1;
    }
};
int main()
{
    A a(212), b;
    cout << (b = a).get_x();
    return 0;
}
```
#### NU compileaza
Variabila `static int x` nu este initializata inafara clasei -> scoatem static

# ex 26
```c++
#include <iostream>
using namespace std;

class A {
protected:
    int x;

public:
    A(int i = 14) { x = i; }
};
class B : A {
public:
    B()
        : A(2)
    {
    }
    B(B& b) { x = b.x - 14; }
    void afisare() { cout << x; }
};
int main()
{
    B b1, b2(b1);
    b2.afisare();
    return 0;
}
```
#### Compileaza
```
-12
```

# ex 27 
```c++
#include <iostream>
using namespace std;
class B {
    int i;

public:
    B() { i = 1; }
    virtual int get_i() { return i; }
};
class D : public B {
    int j;

public:
    D() { j = 2; }
    int get_i() { return B::get_i() + j; }
};
int main()
{
    const int i = cin.get();
    if (i % 3) {
        D o;
    }
    else {
        B o;
    }
    cout << o.get_i(); //(1)
    return 0;
}
```
#### NU compileaza
Variabila `o` este locala in if else statement si este stearsa ->nu exitsa obiectul `o` dupa else

# ex 28
```c++
#include <iostream>
using namespace std;
class problema {
    int i;

public:
    problema(int j = 5) { i = j; }
    void schimba() { i++; }
    void afiseaza() { cout << "starea curenta " << i << "\n"; }
};
problema mister1() { return problema(6); }
void mister2(problema& o)
{
    o.afiseaza();
    o.schimba();
    o.afiseaza();
}
int main()
{
    mister2(mister1()); //crapa comentam linia
    return 0;
}
```

#### Nu compileaza
Functia `mister2` primeste ca parametru o variabila de tip `problema referinta` dar functia `mister1` nu intoarce nicio zona de memorie
Identic cu ex 4

# ex 29
```c++
#include <iostream>
using namespace std;
class B {
    int i;

public:
    B() { i = 1; }
    virtual int get_i() { return i; }
};
class D : virtual public B {
    int j;

public:
    D() { j = 2; }
    int get_i() { return B::get_i() + j; }
};
class D2 : virtual public B {
    int j2;

public:
    D2() { j2 = 3; }
    int get_i() { return B::get_i() + j2; }
};
class MM : public D, public D2 {
    int x;

public:
    MM() { x = D::get_i() + D2::get_i(); }
    int get_i() { return x; }
};
int main()
{
    B* o = new MM();
    cout << o->get_i() << "\n";
    MM* p = dynamic_cast<MM*>(o);
    if (p)
        cout << p->get_i() << "\n";
    D* p2 = dynamic_cast<D*>(o);
    if (p2)
        cout << p2->get_i() << "\n";
    return 0;
}
```
#### Compileaza
```
7
7
7
```

# ex 30
```c++
#include <iostream>
using namespace std;
class B {
    int x;

public:
    B(int i = 7) { x = i; }
    int get_x() { return x; }
    operator int() { return x; }
};
class D : public B {
public:
    D(int i = -12)
        : B(i)
    {
    }
    D operator+(D a) { return get_x() + a.get_x() + 1; }
};
int main()
{
    D a;
    int b = 18;
    b += a;
    cout << b;
    return 0;
}
```
#### Compileaza
```
6
```

# ex 31
```c++
#include <iostream>
using namespace std;
#include <typeinfo>
class B {
    int i;

public:
    B() { i = 1; }
    int get_i() { return i; }
};
class D : B {
    int j;

public:
    D() { j = 2; }
    int get_j() { return j; }
};
int main()
{
    B* p = new D; //aici crapa
    cout << p->get_i();
    if (typeid((B*)p).name() == "D*")
        cout << ((D*)p)->get_j();
    return 0;
}
```
#### Nu compileaza
B este o baza inaccesibila in D

# ex 32
```c++
#include <iostream>
using namespace std;
class B {
protected:
    int x;

public:
    B(int i = 28) { x = i; }
    virtual B f(B ob) { return x + ob.x + 1; }
    void afisare() { cout << x; }
};
class D : public B {
public:
    D(int i = -32)
        : B(i)
    {
    }
    B f(B ob) { return x + ob.x - 1; }//aici crapa
};
int main()
{
    B *p1 = new D, *p2 = new B, *p3 = new B(p1->f(*p2));
    p3->afisare();
    return 0;
}
```
#### Nu compileaza
Functia `D::B f(B ob)` nu are acces la variabila `ob.x` protected

# ex 33
```c++
#include <iostream>
using namespace std;
class B {
protected:
    static int x;
    int i;

public:
    B()
    {
        x++;
        i = 1;
    }
    ~B() { x--; }
    static int get_x() { return x; }
    int get_i() { return i; }
};
int B::x;
class D : public B {
public:
    D() { x++; }
    ~D() { x--; }
};
int f(B* q)
{
    return (q->get_x()) + 1;
}
int main()
{
    B* p = new B[10];
    cout << f(p);
    delete[] p;
    p = new D;
    cout << f(p);
    delete p;
    cout << D::get_x();
    return 0;
}
```
#### Compileaza
```
1131
```

# ex 34
```c++
#include <iostream>
using namespace std;
template <class T, class U>
T f(T x, U y)
{
    return x + y;
}
int f(int x, int y)
{
    return x - y;
}
int main()
{
    int *a = new int(3), b(23);
    cout << *f(a, b);
    return 0;
}
```
#### Compileaza
```
0
```

# ex 35
```c++
#include <iostream>
using namespace std;
class A {
    int x;

public:
    A(int i = 0) { x = i; }
    A operator+(const A& a) { return x + a.x; }
    template <class T>
    ostream& operator<<(ostream&);
};
template <class T>
ostream& A::operator<<(ostream& o)
{
    o << x;
    return o;
}
int main()
{
    A a1(33), a2(-21);
    cout << a1 + a2;
    return 0;
}
```
#### Nu compileaza
` (a1+a2).operator<<<A>(cout);`

# ex 36
```c++
#include <iostream>
using namespace std;
class cls {
    int x;

public:
    cls(int i) { x = i; }
    int set_x(int i)
    {
        int y = x;
        x = i;
        return y;
    }
    int get_x() { return x; }
};
int main()
{
    cls* p = new cls[10]; //aici crapa
    int i = 0;
    for (; i < 10; i++)
        p[i].set_x(i);
    for (i = 0; i < 10; i++)
        cout << p[i].get_x();
    return 0;
}
```
#### Nu compileaza
Atunci cand am redefinit constructorul `cls(int i)`, automatat s-a sters constructorul default. Array-ul `p` are nevoie de constructorul default, dar nu mai exista. 

# ex 37
```c++
#include<iostream>
using namespace std;

class A
{
    int i;
    protected: static int x;
    public: A(int j=7) {i=j;x=j;}
    int get_x() {return x;}
    int set_x(int j) {int y=x; x=j; return y;}
    A operator=(A a1) {set_x(a1.get_x()); return a1;}
};
int A::x=15;
int main()
{
    A a(212),b;
    cout<<(b=a).get_x();//atentie: a are acum x=7 NU 212
    return 0;
}
```
#### Compileaza
```
7
```

# ex 38
```c++
#include<iostream>
using namespace std;

template<class X, class Y>
X f(X x, Y y)
{
    return x+y;
}
int *f(int *x,int y)
{
    return x-y;
}
int main()
{
    int *a=new int(200), *b=a;//inlocuim `*b=a` cu `b=*a`
    cout<<*f(a,b);//sau `*f(a,b)` cu ` *f(a,*b)`
    return 0;
}
```
#### NU compileaza
Noi apelam f(a,b) adica f(int*, int*). Nu avem nicio functie care sa primeasca 2 parametri de acelasi tip

# ex 39
```c++
#include<iostream>
using namespace std;

template<class X>void test(X &a, X &b)
{
    X temp;
    temp=a;
    a=b;
    b=temp;
    cout<<"ttest\n";
}
void test(int &c,int &d)
{
    int temp;
    temp=c;
    c=d;
    d=temp;
    cout<<"test 1\n";
}
void test(int e,int f)//modificam aici si mai adaugam un parametru
{
    int temp;
    temp=e;
    e=f;
    f=temp;
    cout<<"test 2\n";
}
void test(int g,int *h)
{
    int temp;
    temp=g;
    g=*h;
    *h=temp;
    cout<<"test 3\n";
}
int main()
{
    int a=5,b=15,c=25,*d=&a;
    test(a,b);
    test(c,d);
    return 0;
}
```
#### Nu compileaza
Avem ambiguitate intre functiile `void test(int e, int f)` si `void test(int &c, int &g)` deoarce au acelasi antent. 

# ex 40
```c++
#include<iostream>
using namespace std;

class A
{
    int valoare;
    public: A(int param1=3):valoare(param1){}
    int getValoare(){return this->valoare;}
};
int main()
{
    A vector[]={*(new A(3)),*(new A(4)),*(new A(5)),*(new A(6)) };
    cout<<vector[2].getValoare();
    return 0;
}
```
#### Compileaza
```
5
```

# ex 41
```c++
#include <iostream>
using namespace std;

int f(int y)
{
    if (y < 0)
        throw y;
    return y / 2;
}
int main()
{
    int x;
    try
    {
        cout << "Da-mi un numar par: ";
        cin >> x; //se va citi numarul 2
        if (x % 3)
            x = f(x);
        else
            throw x;
        cout << "Numarul " << x << " e bun!\n";
    }
    catch (int i)
    {
        cout << "Numarul " << i << " nu e bun!\n";
    }
    return 0;
}
```
#### compileaza
```
Da-mi un numar par: Numarul 1 e bun!
```


# ex 42
```c++
#include<iostream>
using namespace std;

class A
{
    int i;
    public: A() {i=1;}
    virtual int get_i() {return i;}
};
class B: public A
{
    int j;
    public: B() {j=2;}
    int get_i() { return A::get_i()+j;}
};
int main()
{
    const int i=cin.get();
    if(i%3) {A o;}
    else {B o;}
    cout<<o.get_i();//aici crapa
    return 0;
}
```
#### Nu compileaza
NU exista obiectul `o` in memorie (este distrus dupa ce se iese din if else statement)

# ex 43
```c++
#include<iostream>
using namespace std;

class cls
{
    int x;
public:
        cls(int i=0) {cout<<"c1 "; x=i;}
        ~cls() {cout<<"d1 ";}
};
class cls1
{
    int x; cls xx;
public:
        cls1(int i=0){cout<<"c2 ";x=i;}
        ~cls1(){cout<<"d2 ";}
}c;//atentie la c-ul asta -> c2 c1
class cls2
{
    int x;cls1 xx;cls xxx;
public:
    cls2(int i=0) {cout<<"c3 ";x=i;}
    ~cls2(){ cout<<"d3 ";}
};
int main()
{
    cls2 s;
    return 0;
}
```
#### Compileaza
```
c1 c2 c1 c2 c1 c3 d3 d1 d2 d1 d2 d1
```

# ex 44
```c++
#include<iostream>
using namespace std;
#include<typeinfo>

class B
{
    int i;
public:
    B() { i=1;}
    int get_i() {return i;}
};
class D: public B
{
    int j;
public:
    D() {j=2;}
    int get_j(){return j;}
};
int main()
{
    B *p=new D;
    cout<<p->get_i();
    if(typeid((B*)p).name()=="D*") cout<<((D*)p)->get_j();//nu merge typeid da ceva 1P1
    return 0;
```
# ex 45
```c++
#include<iostream>
using namespace std;

class cls
{
    int x;
public: cls(int i=3) {x=i;}
    int &f() const{ return x;}//crapa
    //`int f() const {return x;}
};
int main()
{
    const cls a(-3);
    int b=a.f();
    cout<<b;
    return 0;
}
```
#### Nu compileaza
functia f este constanta (promite ca nu modifica nimic) dar returneaza `int &` (o adresa de memorrie)

# ex 46
```c++
#include<iostream>
using namespace std;

class B
{
    protected: int x;
    public: B(int i=0) {x=i;}
    virtual B minus() {return (1-x);}
};
class D: public B
{
    public: D(int i=0):B(i) {}
    // adaugam constructorul D(B b) : B(b) {}
    void afisare() {cout<<x;}
};
int main()
{
    D *p1=new D(18);
    *p1=p1->minus();//crapa
    p1->afisare();
    return 0;
}
```
#### Nu compileaza
Functia p1->minus returneaza un obiect de tip B, dar nu exista conversie intre B si D

# ex 47
```c++
#include <iostream>
using namespace std;

class cls1 {
  int x;
public:
  cls1 () {
    x = 13;
  }
  int g() {
    static int i; i++; 
    return (i+x);
  }
};

class cls2 {
  int x;
public:
  cls2() {
    x = 27;
  }
  cls1& f() { //trimite o functie prin referinta, dar obiectul este sters dupa iesirea din functie
     cls1 ob; return ob;
  }
};

int main() {
  cls2 ob;
  cout << ob.f().g();
  return 0;
}
```
#### Compileaza
Nu afiseaza nimic

# ex 48
```c++
#include <iostream>
using namespace std;

class cls1
{ protected: int x;
public:    cls1(int i=10) { x=i; }
	int get_x() { return x;} };
class cls2: cls1 // faci mostenirea public
{ public: cls2(int i):cls1(i) {} }; int main()
{ cls2 d(37);
	cout<<d.get_x();//nu are accees
	return 0; }
```
#### Nu compileaza
Obiectul d nu are acces la metoda `get_x()` ( e privata)

# ex 49
```c++
#include <iostream>
using namespace std;
class cls
{
	int x;

public:
	cls(int y) { x = y; }
	friend int operator*(cls a, cls b) { return (a.x * b.x); }
};
int main()
{
	cls m(100), n(15);
	cout << m * n;
	return 0;
}
```
#### Compileaza
```
1500
```

# ex 50
```c++
#include <iostream>
using namespace std;

class B
{ int i;
public: B() { i=1; cout<<"B ";}
    virtual int get_i() { return i; } };
class D: virtual public B
{ int j;
public: D() { j=2; cout<<"D ";}
    int get_i() {return B::get_i()+j; } };
class D2: virtual public B
{ int j2;
public: D2() { j2=3; cout<<"D2 "; }
    int get_i() {return B::get_i()+j2; } };
class MM: public D, public D2
{ int x;
public: MM() { x=D::get_i()+D2::get_i();cout<<"MM \n"; }
    int get_i() {return x; } };
int main()
{ B *o= new MM();
    cout<<o->get_i()<<"\n";
    MM *p= dynamic_cast<MM*>(o);
    if (p) cout<<p->get_i()<<"\n";
    D *p2= dynamic_cast<D*>(o);
    if (p2) cout<<p2->get_i()<<"\n";
    return 0;
}
```
#### Compileaza
```
B D D2 MM
7
7
7
```

# ex 51
```c++
#include <iostream>
using namespace std;
#include <typeinfo>

class B
{ int i;
  public: B() { i=1; }
          int get_i() { return i; }
};
class D: public B
{ int j;
  public: D() { j=2; }
          int get_j() {return j; }
};
int main()
{ B *p=new D;
  cout<<p->get_i();
  if (typeid((B*)p).name()=="B") cout<<((D*)p)->get_j();
  return 0;
}
```
#### Compileaza
```
1
```

# ex 52
```c++
#include <iostream>
using namespace std;
class B
{ protected: static int x;
             int i;
  public: B() { x++; i=1; }
          ~B() { x--; cout << "b";}
          int get_x() { return x; }
          int get_i() { return i; } };
int B::x;
class D: public B
{ public: D() { x++; }
          ~D() { x--; cout << "d";} };
int f(B *q)
{ return (q->get_x())+1; }
int main()
{ B *p=new B[10];
  cout<<f(p);
  delete[] p;
  p=new D;
  cout<<f(p);
  delete p;
  
  cout<<D::get_x();//crapa aici
  //modificam cout<<p->get_x()
  return 0;
}
```
#### Nu compileaza
Functie `get_x()` nu este statica, deci nu poate fi  apelata de clasa

# ex 53
```c++
#include <iostream>
using namespace std;
class cls
{ int x;
  public: cls(int i/*=0*/) { x=i; }
  int set_x(int i) { int y=x; x=i; return y; }
  int get_x(){ return x; } };
int main()
{ cls *p=new cls[10];
  int i=0;
  for(;i<10;i++) p[i].set_x(i);
  for(i=0;i<10;i++) cout<<p[i].get_x();
  return 0;
}
```
#### Nu compileaza
Nu avem constructorul defualt pt array

# ex 54
```c++
#include <iostream>
#include <typeinfo>
using namespace std;

class A
{
    int n;

public:
    A(int x) { n = x; }
    void afis() { cout << n; }
};

class B : public A
{
public:
    B(int x) : A(x) {}
};
int main()
{
    int x;
    cin >> x;
    if (x > 0)
    {
        A ob(2);
    }
    else
    {
        B ob(2);
    }
    ob.afis();//comentam linia
    return 0;
}
```
#### Nu compileaza
Pretty obviously


# ex 55
```c++
#include <iostream>
using namespace std;
class B
{
    int i;

public:
    B() { i = 50; }
    virtual int get_i() { return i; }
};
class D : public B
{
    int j;

public:
    D() { j = 47; }
    int get_j() { return j; }
};
int main()
{
    D *p = new B;//B *p=new D
    cout << p->get_i();
    cout << ((D *)p)->get_j();
    return 0;
}
```
#### Nu compileaza
avem un pointer derivata de tip baza 

# ex 56
```c++
#include <iostream>
using namespace std;

class cls1 {
  int x;
public:
  cls1 () {
    x = 13;
  }
  int g() {
    static int i; i++; 
    return (i+x);
  }
};

class cls2 {
  int x;
public:
  cls2() {
    x = 27;
  }
  cls1& f() {
     cls1 ob; return ob;
  }
};

int main() {
  cls2 ob;
  cout << ob.f().g();
  return 0;
}
```
#### Compileaza
nu afiseaza nimic

# ex 57
```c++
#include <iostream>
using namespace std;

class D;

class B {
    int x;
    friend void f(B, D);

public:
    B(int i = 0) { x = i; }
};

class D : public B {
public:
    int y;
    D(int i = 0, int j = 0)
        : B(i)
    {
        y = j;
    }
};

void f(B b, D d) { cout << b.x << " " << d.y; }

int main()
{
    B b;
    D d;
    f(b, d);
}
```
#### compileaza
```
0 0
```

# ex 58
```c++
#include <iostream>
using namespace std;

class D;

class B {
    int x;
    friend void f(B, D);

public:
    B(int i = 0) { x = i; }
};

class D : public B {
public:
    int y;
    D(int i = 0, int j = 0)
        : B(i)
    {
        y = j;
    }
};

void f(B b, D d) { cout << b.x << " " << d.y; }

int main()
{
    B b;
    D d;
    f(b, d);
}
```
#### compileaza
```
0 0
```

# ex 59
```c++
#include <iostream>
using namespace std;

class B {
//adaugam protected:
    int x;

public:
    B(int v) { v = x; }
    int get_x() { return x; }
};

class D : private B {
    int y;

public:
    D(int v)
        : B(v)
    {
    }
    int get_x() { return x; }
};

int main()
{
    D d(10);
    cout << d.get_x();
}
```
#### Nu compileaza
Membrul `x` este privat in clasa `B`, deci `D` nu are acces

# ex 60
```c++
#include <iostream>
using namespace std;

class cls {
public:
    float sa;
    cls(float s = 0) { sa = s; }
    operator float() { return sa; }
    float f(float c) { return (sa * (1 + c / 100)); }
};

int main()
{
    cls p(100);
    cout << p.f(p);
}
```
#### Compileaza
```
200
```

# ex 61
```c++
#include <iostream>
using namespace std;

class cls {
    int vi;

public:
    cls(int v = 18) { vi = v; }
    operator int() { return vi; }
    cls operator++()
    {
        vi++;
        return *this;
    }
    cls operator++(int);
};

cls cls::operator++(int)
{
    cls aux = *this;
    vi++;
    return aux;
}

int main()
{
    cls p(20);
    int x = p++, y = ++p;
    cout << "x=" << x << ", y=" << y << endl;
}
```
#### Compileaza
```
x=20, y=22
```

# ex 62
```c++
#include <iostream>
using namespace std;

class cls {
    int vi;

public:
    cls(int v = 18) { vi = v; }
    operator int() { return vi; }
    cls operator++()
    {
        vi++;
        return *this;
    }
    cls operator++(int);
};

cls cls::operator++(int)
{
    cls aux = *this;
    vi++;
    return aux;
}

int main()
{
    cls p(20);
    int x = p++, y = ++p;
    cout << "x=" << x << ", y=" << y << endl;
}
```
#### Compileaza
```
x=20, y=22
```
\
# ex 63
```c++
#include <iostream>
using namespace std;

class cls
{
public:
    int x;
    cls() { x = 3; }
    void f(cls &c) { cout << c.x; } //  friend void f(cls c) { cout << c.x; }
    
};

int main()
{
    const cls d;
    f(d);//eroarea apare aici
}
```
#### Nu compileaza 
- nu exista functia f in afara clasei
- un o functie ce primeste ca parametru o `cls referinta` ar fi apelata de un obiuect constant

# ex 64
```c++
#include <iostream>
using namespace std;

class cls {
public:
    int x, y;
    cls(int i = 0, int j = 0)
    {
        x = i;
        y = j;
    }
};

int main()
{
    cls a, b, c[3] = { cls(1, 1), cls(2, 2), a };
    cout << c[2].x;
}
```
#### Compileaza
```
0
```

# ex 65
```c++
#include <iostream>
using namespace std;

class vector {
    int *p, nr;

public:
    operator int() { return nr; }
    vector(int);
};

vector::vector(int n)
{
    p = new int[n];
    nr = n;
    while (n--)
        p[n] = n;
}

void f(int i)
{
    while (i--)
        cout << i << endl;
}

int main()
{
    vector x(10);
    f(x);
}
```
#### compileaza
```
9
8
7
6
5
4
3
2
1
0
```

# ex 66
```c++
#include <iostream>
using namespace std;
template <class X>
int functie(X x, X y)
{
    return x + y;
}
int functie(int x, int *y)
{
    return x - *y;
}
int main()
{
    int a = 27, *b = new int(45);
    cout << functie(a, b);
    return 0;
}
```
#### compileaza
```
-18
```

# ex 67
```c++
#include <iostream>
using namespace std;

class Y;

class Z;

class X {
    int x;

public:
    X(int n = 0) { x = n; }
    friend Y; // friend Z;
};

class Y {
    int y;
    friend Z;
};

class Z {
public:
    void f(X u) { cout << u.x; }
};

int main()
{
    X a;
    Z b;
    b.f(a);
}
```
#### nu compileaza
Desi `Z` este prieten cu `Y` si are acces la membrii privati din `Y`, si `Y` este prieten cu `X` si are acces la membrii privati din `X`, z NU ARE ACCES la membrii pivati ai lui X (prietenia nu este transmisibila)

# ex 68
```c++
#include <iostream>
using namespace std;

class cls2;

class cls1 {
public:
    int vi;
    cls1(int v = 30) { vi = v; }
    cls1(cls2 p) { vi = p.vi; } //functia nu face conversie implicita
};

class cls2 {
public:
    int vi;
    cls2(int v = 20) { vi = v; }
};

cls1 f(cls1 p)
{
    p.vi++;
    return p;
}

int main()
{
    cls1 p;
    f(p);
    cout << endl
         << p.vi;
    cls2 r;
    f(r);
    cout << endl
         << r.vi;
}
```

# ex 69
```c++
#include <iostream>
using namespace std;
class A
{
    int i;

public:
    A(int x = 3) : i(x) {}
    virtual int get_i() { return i; }
};
class B : public A
{
    int j;

public:
    B(int x = 10) : j(x) {}
    virtual int get_j() { return A::get_i() + j; }
};
int main()
{
    A o1(5);
    B o2;
    cout << o1.get_i();
    cout << o2.get_j();
    cout << o2.get_i();
    return 0;
}
```
#### compileaza
```
5133
```

# ex 70
```c++
#include <iostream>
using namespace std;
class cls1 {
protected:
    int x;

public:
    cls1() { x = 13; }
};
class cls2 : public cls1 {
    int y;

public:
    cls2() { y = 15; }
    int f(cls2 ob) { return (ob.x + ob.y); }
};
int main()
{
    cls2 ob;
    cout << ob.f(ob);
    return 0;
}
```
#### compileaza
```
28
```

# ex 71
```c++
#include <iostream>
using namespace std;
class cls1 {
    int x;

public:
    cls1() { x = 13; }
    int g()
    {
        static int i;
        i++;
        return (i + x);
    }
};
class cls2 {
    int x;

public:
    cls2() { x = 27; }
    cls1& f()
    {
        static cls1 ob;
        return ob;
    }
};
int main()
{
    cls2 ob;
    cout << ob.f().g();
    return 0;
}
```
#### compileaza
```
14
```
# ex 72
```c++
#include <iostream>
using namespace std;
class cls1 {
protected:
    int x;

public:
    cls1(int i = 10) { x = i; }
    int get_x() { return x; }
};
class cls2 : cls1 {
public:
    cls2(int i)
        : cls1(i)
    {
    }
};
int main()
{
    cls d(37);//cls1 d(37)
    cout << d.get_x();
    return 0;
}
```
#### nu compileaza
Nu exista clasa `cls`

# ex 73
```c++
#include <iostream>
using namespace std;

class B {
public:
	int x;
	B(int i = 16) { x = i; }
	B(){}//stergem linia
	B f(B ob) { return x + ob.x; }
};
class D : public B {
public:
	D(int i = 25) { x = i; }
	B f(B ob) { return x + ob.x + 1; }
	void afisare() { cout << x; }
};
int main()
{
	B *p1 = new D, *p2 = new B, *p3 = new B(p1->f(*p2));
	cout << p3->x;
	return 0;
}
```
#### nu compileaza
ambuiguitate intre constructorul fara parametri si cel cu valoare default



# ex 74
```c++
#include <iostream>
using namespace std;
class cls {
    int vi;

public:
    cls(int v = 37) { vi = v; }
    friend int& f(cls);
};
int& f(cls c) { return c.vi; }
int main()
{
    const cls d(15);
    f(d) = 8;
    cout << f(d);
    return 0;
}
```
#### compileaza
nu afiseaza nimic pentru cu obiectul returnat de functia f este referinta si astfel este distrus la iesirea din functie


# ex 75
```c++
#include <iostream>
using namespace std;
class cls1 {
public:
    int x;
    cls1(int i = 20) { x = i; }
};
class cls2 {
public:
    int y;
    cls2(int i = 30) { y = i; }
    operator cls1()
    {
        cls1 ob;
        ob.x = y;
        return ob;
    }
};
cls1 f(cls1 ob)
{
    ob.x++;
    return ob;
}
int main()
{
    cls1 ob1;
    f(ob1);
    cout << ob1.x;
    cls2 ob2;
    f(ob2);
    cout << ob2.y;
    return 0;
}
```
#### compileaza
```
2030
```

# ex 76
```c++
#include <iostream>
using namespace std;
class cls {
    int x;

public:
    cls(int i = 25) { x = i; }
    int f();
};
int cls::f() { return x; }
int main()
{
    const cls d(15);
    cout << d.f();
    return 0;
}
```
#### nu compileaza
un obiect constant apeleaza o metoda neconstanta

# ex 77
```c++
#include <iostream>
using namespace std;
template <class tip>
tip dif(tip x, tip y)
{
    return x - y;
}
unsigned dif(unsigned x, unsigned y)
{
    return x >= y ? x - y : y - x;
}
int main()
{
    unsigned i = 7, j = 8;
    cout << dif(i, j);
    return 0;
}
```
#### compileaza
```
1
```

# ex 78
```c++
#include <iostream>
using namespace std;
class B
{
protected:
    int i;

public:
    B(int j = 5)
    {
        cout << " cb ";
        i = j - 2;
    }
    ~B() { cout << " db "; }
    int get_i() { return i; }
};
class D1 : public B
{
    int j;//!! E PRIVAT

public:
    D1(int k = 10)
    {
        cout << " cd1 ";
        j = i - k + 3;
    }
    ~D1() { cout << " dd1 "; }
};
class D2 : public D1
{
    int k;

public:
    D2(int l = 15)
    {
        cout << " cd2 ";
        k = i + j - l + 3;//nu avem acces la `j`
    }
    ~D2() { cout << " dd2 "; }
};
D1 f(D1 d1, D2 d2) { return d1.get_i() + d2.get_i(); }
int main()
{
    D2 ob2;
    D1 ob1(3);
    cout << f(ob1, ob2).get_i() + ob2.get_i();
    return 0;
}
```
#### nu compileaza
Clasa d2 nu are acces la membrul `j` din d1 -> adaugam protected

# ex 79
```c++
#include <iostream>
using namespace std;
class B {
    int x;

public:
    B(int i = 2)
        : x(i)
    {
    }
    int get_x() const { return x; }
};
class D : public B {
    int* y;

public:
    D(int i = 2)
        : B(i)
    {
        y = new int[i];
        for (int j = 0; j < i; j++)
            y[j] = 1;
    }
    D(D& a)
    {
        y = new int[a.get_x()];
        for (int i = 0; i < a.get_x(); i++)
            y[i] = a[i];
    }
    int& operator[](int i) { return y[i]; }
};
ostream& operator<<(ostream& o, const D& a)//scoatem const
{
    for (int i = 0; i < a.get_x(); i++)
        o << a[i];
    return o;
}
int main()
{
    D ob(5);
    cout << ob;
    return 0;
}
```
#### nu compileaza
Crapa la linia 31 pt ca apeleaza `a[i]` dar `a` e constant, scoatem constul de la linia 31

# ex 80
```c++
#include <iostream>
using namespace std;
class B {
    int x;

public:
    B(int i = 10) { x = i; }
    int get_x() { return x; }
};
class D : public B {
public:
    D(int i)
        : B(i)
    {
    }
    D operator+(const D& a) { return x + a.x; }
};
int main()
{
    D ob1(7), ob2(-12);
    cout << (ob1 + ob2).get_x();
    return 0;
}
```
#### nu compileaza
in clasa D nu avem acces direct la `x` deorece este private -> facem protected

# ex 81
```c++
#include <iostream>
using namespace std;
class B {
public:
    int x;
    B(int i = 16) { x = i; }
    B f(B ob) { return x + ob.x; } //NU E VIRTUAL
};
class D : public B {
public:
    D(int i = 25) { x = i; }
    B f(B ob) { return x + ob.x + 1; }
    void afisare() { cout << x; }
};
int main()
{
    B *p1 = new D, *p2 = new B, *p3 = new B(p1->f(*p2));
    cout << p3->x;
    return 0;
}
```
#### compileaza
atentie: p1 apeleaza B **B::F(B ob)** (functia nu e virtuala)
```
41
```

# ex 82
```c++
#include <iostream>
using namespace std;
class cls {
    int *v, nr;

public:
    cls(int i)
    {
        nr = i;
        v = new int[i];
        for (int j = 1; j < nr; j++)
            v[j] = 0;
    }
    int size() { return nr; }
    int& operator[](int i) { return *(v + i); }
};
int main()
{
    cls x(10);
    x[4] = -15;
    for (int i = 0; i < x.size(); i++)
        cout << x[i];
    return 0;
}
```
#### compileaza
```
0000-1500000
```
# ex 83
```c++
#include <iostream>
using namespace std;
class cls {
    int x;

public:
    cls(int i = -20) { x = i; }
    const int& f() { return x; }
};
int main()
{
    cls a(14);
    int b = a.f()++;
    cout << b;
    return 0;
}
```
#### NU compileaza
nu poti da ++ la o zona de memorie pusa constanta, ca sa rezolvi modifici linia 12 in b=a.f(); si va afisa 14

# ex 84
```c++
#include <iostream>
using namespace std;
class B {
    static int x;
    int i;

public:
    B()
    {
        x++;
        i = 1;
    }
    ~B() { x--; }
    static int get_x() { return x; }
    int get_i() { return i; }
};
int B::x;
class D : public B {
public:
    D() { x++; }
    ~D() { x--; }
};
int f(B* q)
{
    return (q->get_i()) + 1;
}
int main()
{
    B* p = new B;
    cout << f(p);
    delete p;
    p = new D;
    cout << f(p);
    delete p;
    cout << D::get_x();
    return 0;
}
```
#### Nu compileaza
datele din B sunt private DUUH

# ex 85
```c++
#include <iostream>
using namespace std;
class B {
    int x;

public:
    B(int i = 17) { x = i; }
    int get_x() { return x; }
    operator int() { return x; }
};
class D : public B {
public:
    D(int i = -16)
        : B(i)
    {
    }
};
int main()
{
    D a;
    cout << 27 + a;
    return 0;
}
```
#### compileaza
```
11
```

# ex 86
```c++
#include <iostream>
using namespace std;
class cls {
    static int x;

public:
    cls(int i = 1) { x = i; }
    cls f(cls a) { return x + a.x; }
    static int g() { return f() / 2; } //f nu are paremtri
};
int cls::x = 7;
int main()
{
    cls ob;
    cout << cls::g();
    return 0;
}
```
#### nu compileaza
functia f() apelata de g nu exista

# ex 87
```c++
#include <iostream>
using namespace std;
class cls {
    int *v, nr;

public:
    cls(int i = 0)
    {
        nr = i;
        v = new int[i];
        for (int j = 0; j < size(); j++)
            v[j] = 3 * j;
    }
    ~cls() { delete[] v; }
    int size() { return nr; }
    int& operator[](int i) { return v[i]; }
    cls operator+(cls);
};
cls cls::operator+(cls y)
{
    cls x(size());
    for (int i = 0; i < size(); i++)
        x[i] = v[i] + y[i];
    return x;
}
int main()
{
    cls x(10), y = x, z;
    x[3] = y[6] = -15;
    z = x + y;
    for (int i = 0; i < x.size(); i++)
        cout << z[i];
    return 0;
}
```
#### compileaza
```
0012-302430-30424854
```

# ex 88
```c++
#include <iostream>
using namespace std;
class B {
    int i;

public:
    B() { i = 1; }
    int get_i() { return i; }
};
class D : public B {
    int j;

public:
    D() { j = 2; }
    int get_j() { return j; }
};
int main()
{
    B* p;
    int x = 0;
    if (x)
        p = new B;
    else
        p = new D;
    if (typeid(p).name() == "D*")
        cout << ((D*)p)->get_j();
    return 0;
}
```
# ex 89
```c++
#include <iostream>
using namespace std;
class cls {
    int x;

public:
    cls(int i) { x = i; }//eroare aici
    int set_x(int i)
    {
        int y = x;
        x = i;
        return y;
    }
    int get_x() { return x; }
};
int main()
{
    cls* p = new cls[10];
    int i = 0;
    for (; i < 10; i++)
        p[i].set_x(i);
    for (i = 0; i < 10; i++)
        cout << p[i].get_x(i);//si aici
    return 0;
}
```
#### nu compileaza
nu avem constructor default
functia get_x() nu este apelata corect


# ex 90
```c++
#include <iostream>
using namespace std;
template <class T>
int f(T x, T y)
{
    return x + y;
}
int f(int x, int y)
{
    return x - y;
}
int main()
{
    int a = 5;
    float b = 8.6;
    cout << f(a, b);
    return 0;
}
```
#### compileaza
Merge si afiseaza -3 (cum la apel functiei f(a,b) nu se incadreaza nici pt template, nici pt specializare, face conversie din float in int si intra in specializare)

# ex 91
```c++
#include <iostream>
using namespace std;

class A
{
	int x;
public:
	A(int i = 25) { x = i; }
	int& f() const { return x; }//stergem referinta
};
int main()
{
	A ob(5);
	cout << ob.f();
	return 0;
```
#### nu compileaza
referinta de la o zona de memorie la un const int nepermisa

# ex 92
```c++
#include <iostream>
using namespace std;

class A
{
	int x;
public:
	A(int i):x(i){} //i=0
	int get_x() const { return x; }
};
class B : public A
{
	int *y;
public:
	B(int i) :A(i)
	{
		y = new int[i];
		for (int j = 0; j < i; j++) y[j] = 1;
	}
	B(B&);
	int &operator[](int i) { return y[i]; }
};
B::B(B& a)
{
	y = new int[a.get_x()]; 
	for (int i = 0; i < a.get_x(); i++) y[i] = a[i];
}
ostream &operator<<(ostream& o, B a)
{
	for (int i = 0; i < a.get_x(); i++)o << a[i];
	return o;
}
int main()
{
	B b(5);
	cout << b;
	return 0;
}
```
#### nu compileaza
ca nu am constructor pt A fara parametrii, si ca sa rezolvam punem valoarea default

# ex 93

```c++
#include <iostream>
using namespace std;
#include <typeinfo>

class A
{
	int i;
public: A() { i = 1; }
		int get_i() { return i; }
};
class B: public A
{
	int j;
public: B() { j = 2; }
		int get_j() { return j; }
};
int main()
{
	A *p;
	int x = 0;
	if (x) p = new A;
	else p = new B;
	if (typeid(p).name() == typeid(B*).name()) cout << ((B*)p)->get_j();
	else cout << "tipuri diferite";
	return 0;
}
```
#### compileaza
```
tipuri diferite
```

# ex 94
```c++
#include <iostream>
using namespace std;

class A
{
	int x;
public: A(int i = 17) { x = i; }
		int get_x() { return x; }
};
class B
{
	int x;
public: B(int i = -16) { x = i; }
		operator A() { return x; }
		int get_x() { return x; }
};
int main()
{
	B a;
	A b = a;
	cout << b.get_x();
	return 0;
}
```
#### compileaza
```
-16
```

# ex 95
```c++
#include <iostream>
using namespace std;
class B
{
protected:
    int x;

public:
    B(int i = 3) { x = i; }
    virtual B f(B ob) { return x + ob.x; }
    void afisare() { cout << x; }
};
class D : public B
{
public:
    D(int j = 4) : B(j + 2) { int i = j; }
    D f(D ob) { return x + 1; }
};
int main()
{
    B *p1 = new D, *p2 = new B, *p3 = new B(p1->f(*p2));
    p3->afisare();
    return 0;
}
```
#### compileaza
```
9
```

# ex 96
```c++
#include <iostream>
using namespace std;

class A
{
protected: int x;
public: A(int i = -16) { x = i; }
		virtual A f(A a) { return x + a.x; }
		void afisare() { cout << x; }
};
class B: public A
{
public: B(int i=3):A(i){}
		A f(A a) { return x + a.x + 1; }//nu ai acces
};
int main()
{
	A *p1 = new B, *p2 = new A, *p3 = new A(p1->f(*p2));
	p3->afisare();
	return 0;
}
```

#### nu compileaza


# ex 97
```c++
#include <iostream>
using namespace std;

class A
{
protected: int x;
public: A(int i = -16) { x = i; }
		virtual A f(A a) { return x + a.x; }
		void afisare() { cout << x; }
};
class B: public A
{
public: B(int i=3):A(i){}
		A f(A a) { return x + 1; }
		B operator+ (B a) { return x + a.x; }
};
int main()
{
	B a; int b = -21;
	a += b; // a =a+(B)b;
	cout << b;
	return 0;

}
```
#### nu compileaza
nu este definit operatorul + intre B si int



# ex 98
```c++
#include <iostream>
using namespace std;

class A {
    int x;

public:
    A(int i = 2)
        : x(i)
    {
    }
    int get_x() const { return x; }
};
class B : public A {

    int* y;

public:
    B(int i = 2)
        : A(i)
    {
        y = new int[i];
        for (int j = 0; j < i; j++)
            y[j] = 1;
    }
    B(B& b)
    {
        y = new int[b.get_x()];
        for (int i = 0; i < b.get_x(); i++)
            y[i] = b[i];
    }
    int& operator[](int i) const { return y[i]; }
};
ostream& operator<<(ostream& o, const B b)
{
    for (int i = 0; i < b.get_x(); i++)
        o << b[i];
    return o;
}

int main()
{
    const B b(5);//fara const
    cout << b;
    return 0;
}
```
#### nu compileaza
obiect constant apeleaza metoda neconstanta


# ex 99
```c++
#include <iostream>
using namespace std;

class A
{   protected: static int x;
    private: int y;
    public: A(int i) { x=i; y=-i+4; }
        int put_x(A a) { return a.x+a.y; } };
int A::x=7;
int main()
{   A a(10);
cout<<a.put_x(20);
    return 0;
}
```
#### compileaza
```
4
```
# ex 100
```c++
#include <iostream>
using namespace std;

class A
{ int x;
  static int y;
public: A(int i,int j):x(i),y(j){} //!!!!!!!!varibila statica in lista initializare NUUUUU
	int f() const;};
int A::y;
int A::f() const {return y;}
int main()
{ const A a(21,2);
  cout<<a.f();
return 0;
}
```
#### nu compileaza
variabilele statice nu pot fi initializate in lista de initializare

# ex 103
```c++
#include <iostream>
using namespace std;

class B
{ int i;
  public: B() { i=80; }
          virtual int get_i() { return i; }
};
class D: public B
{ int j;
  public: D() { j=27; }
          int get_j() {return j; }
};
int main()
{ D *p=new B; // gresit trebuie invers
  cout<<p->get_i();
  cout<<((D*)p)->get_j();
  return 0;
}
```

# ex 105
```c++
#include <iostream>
using namespace std;

class A
{   static int *x;
    public: A() {}
            int get_x() { return (++(*x))++; } };
int *A::x(new int(19));
int main()
{   A *p=new A,b;
    cout<<b.get_x()<<" ";
    cout<<p->get_x();
    return 0;
}
```
#### compileaza
```
20 22
```

# ex 106
```c++
#include <iostream>
using namespace std;

class X {   int i;
public:   X(int ii = 5) { i = ii; cout<< i<< " ";};
          const int tipareste(int j) const { cout<<i<< " "; return i+j; }; };
int main()
{ X O (7);
  O.tipareste(5);
  X &O2=O;
  O2.tipareste(6);
  const X* p=&O;
  cout<<p->tipareste(7);
  return 0;
}
```
compileaza
```
7 7 7 7 14
```
# ex 107
```c++
#include <iostream>
using namespace std;

class A
{
protected:
    int x;

public:
    A(int i) : x(i) {}
    int get_x() { return x; }
};
class B : A//public A
{
protected:
    int y;

public:
    B(int i, int j) : y(i), A(j) {}
    int get_y() { return get_x() + y; }
};
class C : protected B
{
protected:
    int z;

public:
    C(int i, int j, int k) : z(i), B(j, k) {}
    int get_z() { return get_x() + get_y() + z; }
};
int main()
{
    C c(5, 6, 7);
    cout << c.get_z();
    return 0;
}****
```
nu compileaza
clasa c nu are acces la get_x

# ex 108
```c++
#include <iostream>
using namespace std;

class cls
{	int x;
public: cls(int i=2) { x=i; }
int set_x(int i) { int y=x; x=i; return y; }
int get_x(){ return x; } };
int main()
{ cls *p=new cls[15];
      for(int i=2;i<8;i++) p[i].set_x(i);
	  for(int i=1;i<6;i++) cout<<p[i].get_x();
  return 0;
}
```
compileaza
```
22345
```

# ex 109
```c++
#include <iostream>
using namespace std;

struct X {   int i;
public:   X(int ii ) { i = ii; };
     int f1() { return i; }
X f2() const {   int i=this->f1(); return X(34-i); }};
const X f3() {   return X(16); }
int f4(const X& x) { return x.f1(); }
int main() {X ob(11);
    cout<<f4(ob.f2().f1());
    return 0;
}
```