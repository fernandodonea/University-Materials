
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
nu afiseaza nimic pentru cu obiectul returnat de functia f este referinta si astfel este distrus la iesirea din functir