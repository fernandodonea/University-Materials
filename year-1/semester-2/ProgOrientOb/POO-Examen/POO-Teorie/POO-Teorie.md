

# Referinte

##### Definitie
Referintele sunt variable ce contin **adresa unei zone de memorie**. Altfel spus, ele reprezinta *aliasuri* ale unor variabile deja existente

##### Sintaxa

```c++
tip_de_date &nume_referinta=valoare;
```

##### Utilizare:
Folosim o referinta mai ales pentru a evita construirea unui nou obiect (de exemplu, intr-o functie dorim sa transmitem obiectul original, ci nu o copie a sa).

#### Proprietati:
1. O referinta trebuie initializata in momentul declararii
2. referintele nu pot fi reasignate
3. referinta nu poate sa fie nula


# Pointeri

#### Definitie
Pointerii sunt variabile care contin adresa unei zone de memorie.

#### Sintaxa

```c++
tip_de_date *nume_pointer = valoare;
```
#### Operatori unari
1. **`&`** -> extragerea adresei unei variabile
2. **`*`** -> referirea continutului zonei de memorie indicate de pointer

### Proprietati
1. un pointer poate fi declarat NULL
```c++
int *p=NULL;
int *q=nullptr;
```
2. un pointer poate primi o valoare mai tarziu in program, nu neaparat la declarare (adica putem modifica valoarea pointerilor)
3. tipul pointerului trebuie sa fie **acelasi** cu tip de datei catre care pointeaza
#### Aritemetica pe pointeri

```c++

pointer++;
//sau
p=pointer+sizeof(tip)

p--;

p+=4;

p1-p2; //intoarce un intreg
// <,>,== comparatii
```

# Alocare dinamica

#### Utilizare
Alocarea dinamica se implementeaza prin intermediul pointerilor si are avantajul ca foloseste **atata memorie cat este necesara**

#### Sintaxa
Alocarea dinamica a memoriei in c++ se face utilizand operatorii `new` si `delete`

- Alocarea unui element:

```c++
tip_date_pointer= new tip_date(initializare);
```

- Dezalocarea unui element:

```c++
delete pointer;
```


La eroare se "arunca" exceptia `bad_alloc` din `new`


- Alocarea unui array:

```c++
tip_date_pointer = new tip[nr_elemente];
```

- Dezalocarea unui tablou array:

```c++
delete [] pointer;
```

Intr-un array dinamic, zona de memorie este continua. Astfel, elementele din array vor fi stocate la diferenta de 4 octeti (dimensiunea tipului de date) unele de altele

### Alocarea de obiecte dinamic
- cu `new`
- dupa crearea, `new` intoarce un pointer catre obiect
- dupa creare se executa `constructorul` obiectului
- cand obiectul este sters din memorie se apeleaza `destructorul`
- new si delete pot fi suprascrisi
- Array-uri de obiecte alocate dinamic
	- nu se pot initializa
	- trebuie sa existe un `constructor fara parametri`
	- `delete` poate fi apelat pentru fiecare element din array


# Obiecte
#### Definitie
Obiectul este un element al uneui clase, care are 
- stare (date membre - variabile)
- actiuni (metode - functii)
Actiunile sunt considerata **interfata**, iar starea e considerata partea "ascunsa" de utilizator


# Clase
#### Definitie
Clasa defineste atributele si metodele obiectului. Practic, aceasta mentioneaza proprietatile obiectelor din ea. 


#### Modificatori de acces

By default, class are acces private, iar struct public

| Avem acces?    | public | protected | private |
| -------------- | ------ | --------- | ------- |
| aceeasi clasa  | da     | da        | da      |
| clase derivate | da     | da        | nu      |
| alte clase     | da     | nu        | nu      |

# Principii OOP
- Mostenire
- Abstractizare
- Incapsulare
- Polimorfsim

# Incapsulare

Mecanismul prin care datele si functiile plasate in aceeasi structura (clasa) si stabilirea nivelului de acces la continutul acesteia

NU am vrea ca un utilizator sa aiba acces la informatii confidentiale

Variabilele declarate in clase sunt **private** by default si e important sa ramana asa. Pentru a le accesa/modfica, vom folosi functii publice numite `getter`/`seteri` 

# Compunerea/Agregarea

Se refera la definirea unui obiect ce il include pe altul deja existent, din alta clasa

Indica existenta unui obiect dependent de alt obiect

#### Avantaje
- **reutilizarea codului**: obiectele mai mici pot fi reutilziate in mai multe clase
- **modularitate**: proiectarea claselor devine mai modulara si mai flexibila, prin combinare componentelor mici si independente
- **incapsulare**: obictele componente pot fi ascunse de utilizator, furnizand doar interfetele necesare pentru a interactiona cu ele