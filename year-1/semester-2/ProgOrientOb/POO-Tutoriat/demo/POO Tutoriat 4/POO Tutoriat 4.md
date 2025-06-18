# POO Tutoriat 4
26 mar 2025

## Mostenire

Scop: reutilizare de cod (poarte numele de derivare)

Compunerea este considera pseudo-mostenire

*Clasa de baza* = parinte, superclasa

*Clasa derivata* = copil, subclasa


Sintaxa:
```c++
class NumeDerivata: modificatorAcces ClasaDeBaza1, modificatorAcces2 ClasaDeBaza2, ... {
    // campuri si metode
}
```

### Modificatori de acces al mostenirii (default: private):
- **Public** => toti membrii din clasa de baza isi pastreaza tipul de acces si in derivata
- **Potected** => membrii "publici" din clasa de baza devin membrii "protected" in clasa derivata
- **Private** => toti membrii din clasa de baza devin membrii "private" in clasa derivata

Exemplu 1
```c++
class B{
    int x;
    public:
        void f(){cout<<x;}
};

class D: public B{
    int y;
    public:
        void g(){cout<<y;}
}
int main()
{
    D d;

}
```
Exemplu 2
```c++
class A{...}
class B: protected A{...} // toate datele din A protected
class C: private B{...} // toate datele din A si B private
class D: public C{...} // toate datele din A si B private, dar unele date din C public 

```

Exemplu 3
```c++
class D{
    private:
        int x;
    public:
        void afisare(){cout<<x;}
}
class D:B{
    int y;
    //private: x
    //private: afisare
}
```

Exemplu 4
```c++
class A{
    public:
        int x;
}
class B: private A{
    public:
        int y;
        int f(){return this->x+this->y;}
}
int main()
{
    A oba;
    B obb;
    A.x;
    B.y;
    B.x; //eroare
}
