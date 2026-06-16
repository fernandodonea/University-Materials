# Tehnici de căutare informată: Algoritmul A*

Algoritmul A* se folosește pentru a găsi un drum de cost minim de la un nod-start la un nod-scop într-un graf ponderat.

Datele de intrare:

* graful (nodurile, muchiile împreună cu costurile lor)
* nodul din care începe căutarea (nodul-start)
* un scop dat sub forma unei condiții pe care trebuie să o îndeplinească nodul căutat (se poate oferi chiar nodul propriu-zis, condiția fiind relația de egalitate cu acest nod). Vom numi mai departe nodul care îndeplinește condiția nod-scop
* o estimare (euristică) a costului de la fiecare nod din graf la nodul (nodurile) scop.

Notații:

* $f$ - costul unui drum
* $\hat{f}$ - costul estimat al unui drum
* $g(nod_c)$ - costul unui drum de cost minim de la nodul start la un nod curent, $nod_c$, din drum
* $h(nod_c)$ - costul efectiv al drumului de cost minim de la nodul curent la nodul scop pe un anumit drum
* $\hat{h}(nod_c)$ - costul estimat de la nodul curent la nodul scop (euristica)

Pentru un drum dat D, avem formula: $f_D$ = $g_D(nod_c$) + $h_D(nod_c$), unde $nod_c$ e un nod din drumul D

Deoarece pe parcursul construirii arborelui de parcurgere nu cunoaștem costul adevărat de la nodul curent la nodul scop (graful fiind descoperit pe măsura ce e parcurs), ne vom folosi în algoritm de formula costului estimat: $\hat{f}_D$ = $g_D$($nod_c$) + $\hat{h}_D$($nod_c$).

### Admisibilitate

Spunem că euristica este *admisibilă* dacă îndeplinește condiția: $\hat{h}(nod) \leq h(nod)$

### Consistență

Regula de consistență: Având o muchie $n_1 \rightarrow n_2$, euristica calculată în nodul $n_1$ trebuie să fie mai mică sau egală decât costul muchiei $n_1 \rightarrow n_2$ adunat la euristica nodului $n_2$

$\hat{h}(n1) \leq cost(n1 \rightarrow n2) + \hat{h}(n2)$

## Pașii algoritmului

Se consideră două liste: OPEN (cu nodurile descoperite care înca nu au fost expandate) și CLOSED (cu nodurile descoperite și expandate).

1. În lista open se pune la început doar nodul de pornire.
2. Inițial lista closed e vidă
3. Cât timp lista open nu e vidă se execută repetitiv pașii următori:
  - Se extrage primul nod, n, din lista open și se pune în closed.
  - Dacă nodul n este nod scop, se oprește căutarea și se afișează drumul de la nodul-start până la nodul n.
  - Se extinde nodul n, obținând succesorii lui în graf. Nu se vor lua în considerare succesorii care se află în drumul de la nodul start la n. Toți succesorii îl au ca părinte pe n. Toți succesorii care nu se află deja în open sau closed sunt inserați în lista open astfel încât aceasta să fie în continuare ordonată crescător dupa f.
  - Pentru succesorii care sunt deja în open sau closed, în cazul în care pentru drumul care trece prin n, s-a obținut un f mai mic, li se schimbă părintele în n și li se actualizează f-ul, iar nodurile din open sunt repoziționate în lista astfel încât să rămână ordonată crescător după f.
  - Pentru nodurile din closed (care au fost deja expandate) ar trebui refăcut calculul pentru nodurile succesoare lor, prin urmare cel mai simplu este să le readăugăm direct în open.

## Implementare

Pentru implementare putem considera niște clase ajutătoare, care ar fi adaptate la particularitățile problemei curente rezolvate cu A*.

Clasa **Nod** reprezintă clasa prin care se memorează informațiile despre nodurile din graf. Poate avea următoarele proprietăți:

- informație - referință către informația nodului
- părinte - referință către nodul-părinte din arbore. Pentru rădăcina arborelui, părintele va avea valoarea None.
- g - costul de la rădăcina arborelui până la nodul curent
- f - costul estimat pentru drumul care pornește de la rădăcină și trece prin nodul curent
- h - estimarea făcuta pentru nod (valoarea funcției euristice pentru nod)

și următoarele metode:

- expandează / succesori - care va returna o listă cu toți succesorii posibili ai nodului curent
- scop - care testează dacă nodul e nod scop

## Pseudocod

Puteți accesa pseudocodul algoritmului [aici](https://en.wikipedia.org/wiki/A*_search_algorithm)

Alternativ:

```
Inițial lista open e vidă
Adaugă nodStart din graf în lista open
Crează o listă numită closed care inițial e vidă

Cât timp lista open nu e vidă repetă:
  Extrage primul nod din open (numit nodCurent) și adaugă-l în lista closed

  Dacă nodCurent este nod-scop:
    Returnează drumul de la nodul de start la nodul curent
    Oprește căutarea

  Expandează nodul curent. Din definiția funcției de succesori, aceștia nu sunt strămoși ai nodului curent

  Pentru fiecare succesor al nodCurent:
    NodNou devine None
    Dacă succesorul este în open:
      Dacă f-ul succesorului curent este mai mic decât f-ul nodului din open SAU f-urile sunt egale și g-ul succesorului curent este mai mare decât g-ul nodului din open:
        Elimină nodul din open
        NodNou devine succesorul

    Altfel, dacă succesorul este în closed:
      Dacă f-ul succesorului curent este mai mic decât f-ul nodului din open SAU f-urile sunt egale și g-ul succesorului curent este mai mare decât g-ul nodului din open:
        Elimină nodul din closed
        NodNou devine succesorul
    
    Altfel:
      NodNou devine succesorul

    Dacă NodNou nu e None:
      Adaugă NodNou în lista open astfel încât open să rămână ordonată crescător după f și, în caz de egalitate, descrescător după g
```

Explicații pas cu pas pe exemplu: https://docs.google.com/document/d/1fjezmPKjN6jB5Uv_m_jhKKoNtk9MzD6EaLTnChuBlI0/edit?usp=sharing

## Aplicarea algoritmului A* în probleme

https://docs.google.com/document/d/1KecWOD3DnSjK1Chfs27xZDyo1uh76aEYZc63pmDmFjk/edit?usp=sharing

# IDA*

Deoarece algoritmul A* folosește o coadă, în care salvează întreaga frontieră a arborelui de căutare, se poate ajunge ușor la o cantitate mare de memorie ocupată, iar pentru unele probleme, se depășesc resursele sitemului ducând la eșecul algoritmului.
Prin urmare s-a încercat limitarea memoriei utilizate combinând A* cu modul de lucru al strategiei DepthFirst.

## Pseudocod (varianta recursivă)

Considerăm nodStart nodul de la care începe căutarea. Considerăm că trebuie să afișăm primele N soluții.


```
Se inițializează variabila Limita = f̂(nodStart).
Setăm nodul curent ca fiind nodStart

Creăm o funcție expandeaza(nodCurent, Limita, eventual alti parametri), care are rolul de a expanda nodul curent și descendenții acestuia numai dacă măsura f̂ a acestora nu depășește limita. Funcția va returna și noua limită de cost pentru expandare care va fi cel mai mic f̂ întâlnit pentru nodurile care nu au putut fi expandate
	Considerăm variabila nodCurent ca fiind nodul curent de expandat.
	Dacă nodul curent are măsura f̂ > Limita atunci:
		Nu expandăm nodul, ci doar returnăm măsura f̂ a acestuia
	Altfel (dacă nodul curent are măsura f̂ <= Limita):
		Dacă este nod scop, și drumul până la el nu a mai fost afișat anterior (pentru o Limita mai mică), atunci afișăm drumul soluție (de la nodStart până la el) și decrementăm numărul de soluții de afișat.
		Expandăm nodul curent, obținând lista de succesori LS.
		Dacă există succesori:
			Pentru fiecare succesor din LS:
				Apelăm Lim_succesor = expandeaza(succesor, Limita)
			Calculăm minimul pentru limitele returnate pentru toți succesorii, returnăm acel minim
		Dacă nu există succesori, returnăm N_MAX, un număr foarte mare (mai mare decât orice f̂ al oricărui nod).

	Repetitiv apelăm funcția Limita=expandeaza(nodStart, Limita), (setând mereu noua limită la valoarea returnată de funcție).

	Ne oprim fie în cazul în care Limita ajunge să fie N_MAX (înseamnă că numărul de soluții din graf e mai mic decât numărul de soluții care a fost cerut) fie când s-a afișat numărul de soluții cerute.
```