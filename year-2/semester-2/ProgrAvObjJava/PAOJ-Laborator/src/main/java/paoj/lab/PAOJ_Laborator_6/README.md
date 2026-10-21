# PAOJ Laborator 6


## ex 1

Sa se defineasca urmatoarele clase pentru a modela o solutie de **online banking** :
- `Student`
- `Profesor`
- `FirmaPartenera`

1. Definiți **interfața** `OperatiiContBancar` cu metodele:
- boolean `autentificare`()
- double `soldCurent`()
- void plata(double suma)
2. Definiți **interfața** `Comparable<T>` în utilizarea standard Java și faceți astfel încât:
- un Student să se compare alfabetic după nume;
- un Profesor să se compare descrescător după salariu;
- o FirmaPartenera să se compare descrescător după buget.

3. Implementați clasele:
- `Student` — are nume, medie, sold;
- `Profesor` — are nume, salariu, sold;
- `FirmaPartenera` — are denumire, buget, sold.

4. Pentru toate clasele implementati interfata `OperatiiContBancar`

5. Scrieți o metodă:

public static void `proceseazaPlati`(OperatiiContBancar[] v, double suma)
care:
- autentifică fiecare obiect;
- dacă soldul curent este suficient, efectuează plata;
- altfel afișează un mesaj de forma “Fonduri insuficiente”.

6. În metoda main
- creati un tablou de obiecte pentru fiecare clasa(eventual folosind o instructiune repetitiva si date fictive generate prin cod).
- Sortati tabloul creat
- Apelati `proceseazaPlati` pentru cel putin 2 instante din clase diferite.

# ex 2
1. Definiți **interfața**:
```java
interface FunctieIntreg {
int valoare(int x);
}
```
2. Implementați **clasa utilitară** `Procesari` cu _constructor privat_ și _metode statice_:
- public static int `suma`(FunctieIntreg f, int n) care calculează: suma de la i=1,n din f(i)
- public static int `numara`(FunctieIntreg f, int n)
care numără de câte ori f(i) este strict pozitiv pentru i = 1..n.
- public static int[] `transforma`(FunctieIntreg f, int n)
care construiește vectorul {f(1),f(2),...,f(n)}


3. Scrieți doua implementări concrete ale interfeței:
Identitate : f(x)=x
PatratPerfect : f(x)=x*x
