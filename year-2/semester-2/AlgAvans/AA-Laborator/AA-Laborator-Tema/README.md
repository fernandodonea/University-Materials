# Algoritmi Genetici

Implementați un algoritm genetic pentru determinarea maximului unei funcții pozitive pe un domeniu dat. Funcția va fi un polinom de gradul 2, cu coeficienţi dați.
Algoritmul trebuie să cuprindă etapele de selecție, încrucişare (crossover) şi mutație.

## Rulare cu cmake


### Requirements
- CMake >= 3.16
- Un compilator C++17

### Build
```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --parallel

```

Rulare cu fisierul de input implicit din proiect
### Run 
```bash
./build/AA_Laborator_Tema data/input.txt
````



## Rulare cu Docker

### Contruim imaginea
```bash
docker build -t aa-laborator-tema .
```

### Run 
Rulare cu fisierul de input implicit din proiect
```bash
docker run --rm -v "$PWD/data:/app/data" aa-laborator-tema
```

## Template pentru fisierul de input
```txt
20
-1 2
-1 1 2
6
0.25
0.1
50
```
**Explicatie**
- Dimensiunea populației: 20
- Domeniul de definitie al functiei: [-1, 2]
- Coeficientii pentru polinomul de grad 2: -1, 1, 2 (-x^2+x+2)
- Precizia: 6
- Probabilitatea de recombinare: 0.25
- Probabilitatea de mutatie: 0.1
- Numarul de etape: 50

## Cetinte proiect


### Precizări
* Se vor folosi metoda de codificare discutată la curs şi încrucişarea cu un singur punct de tăietură/de rupere.
* Se va ține cont și de selecţia de tip elitist (individul cu fitness-ul cel mai mare va trece automat în generația următoare).

### Date de intrare
* Dimensiunea populaţiei (numărul de cromozomi)
* Domeniul de definiţie al funcției (capetele unui interval închis)
* Parametrii pentru funcția de maximizat (coeficienţii polinomului de grad 2)
* Precizia cu care se lucrează (cu care se discretizează intervalul)
* Probabilitatea de recombinare (crossover, încrucișare)
* Probabilitatea de mutaţie
* Numărul de etape al algoritmului

### Date de ieşire
* Un fişier text sugestiv care prezintă detaliat operațiile efectuate în prima etapă a algoritmului, iar apoi un rezumat al evoluţiei populaţiei pentru celelalte etape.
* Un exemplu este fişierul Evolutie.txt, care a fost obținut pentru funcția $-x^{2}+x+2$, domeniul [-1, 2], dimensiunea populaţiei 20, precizia 6, probabilitatea de recombinare 25%, probabilitatea de mutaţie 1% şi 50 de etape.
* Extra: o interfață grafică sugestivă, care afişează evoluția algoritmului.

### Conţinut fişier de ieşire
În fişier vor fi incluse cel puţin următoarele informații:
* Populaţia inițială, cu următoarele date pentru fiecare individ i:
    * $B_{i}$, reprezentarea pe biți a cromozomului;
    * $X_{i}$, valoarea corespunzătoare cromozomului în domeniul de definiţie al funcției (număr real);
    * $f(X_{i})$, valoarea cromozomului, adică valoarea funcției în punctul din domeniu care corespunde acestuia.
* Probabilităţile de selecție pentru fiecare cromozom:
  $p_{i}=\frac{f(X_{i})}{\sum_{j}f(X_{j})}$
* Probabilităţile cumulate care dau intervalele pentru selecție:
  $q_{0}=0$
  $q_{i}=\sum_{j=1}^{i}p_{j}=p_{1}+\cdot\cdot\cdot+p_{i}$
* Evidenţierea procesului de selecție, care constă în generarea unui număr aleator u uniform pe [0,1) și determinarea intervalului $[q_{i},q_{i+1})$ căruia aparţine acest număr; corespunzător acestui interval se va selecta cromozomul $i+1$. Procesul se repetă până se selectează numărul dorit de cromozomi.
* Cerinţă: căutarea intervalului corespunzător se va face folosind căutarea binară.
* Evidenţierea cromozomilor care participă la recombinare.
* Pentru recombinările care au loc se evidențiază perechile de cromozomi care participă la recombinare, punctul de rupere generat aleator precum și cromozomii rezultați în urma recombinării (sau, după caz, se evidenţiază tipul de încrucişare ales).
* Populaţia rezultată după recombinare.
* Populaţia rezultată după mutațiile aleatoare.
* Pentru restul generațiilor (populaţiile din etapele următoare) se va afişa doar valoarea maximă şi valoarea mediei a fitness-ului (performanței) populaţiei:
    * Max Fitness $=max_{i}f(X_{i})$
    * Mean Fitness $=\frac{1}{n}\sum_{i}f(X_{i})$
