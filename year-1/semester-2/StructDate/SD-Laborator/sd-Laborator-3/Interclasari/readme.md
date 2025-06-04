# Infoarena - Interclasari

La începutul Girl Camp, participantele s-au distrat completând puzzle-urile unui Scavenger Hunt care le-a purtat pe străzile aglomerate, dar frumoase ale Bucureştiului. Participantele s-au împărţit în K echipe, şi fiecare echipă a făcut un număr Ni de fotografii. La sfârşitul zilei, organizatorii au adunat pozele de la fiecare echipă în parte şi doresc sa le pregătească o surpriză: un timeline cronologic cu toate întâmplările din ziua respectivă.

Camerele foto ale echipelor au fost configurate special, în sensul că pentru fiecare fotografie înregistrează şi numărul milisecundei de la startul Scavenger Hunt-ului până la momentul la care aceasta a fost făcută.

Date fiind cele K directoare cu poze, fiecare conţinând Ni poze, şi cunoscând pentru fiecare poză momentul de timp la care a fost făcută, ajutaţi-i pe organizatori să scrie un program care interclasează rapid toate pozele pentru a compune un timeline.

## Date de intrare
Fişierul de intrare interclasari.in va conţine pe prima linie un număr K reprezentând numărul de echipe. Vor urma K perechi de linii care descriu fotografiile făcute de fiecare echipă în parte: pe prima linie se va afla Ni, numărul de fotografii ale echipei, iar pe a doua linie se vor afla Ni numere naturale sortate crescător, reprezentând momentele de timp când ele au fost făcute.

## Date de ieşire
În fişierul de ieşire interclasari.out, pe prima linie se va afla numărul total de fotografii făcute în timpul Scavenger Hunt-ului. Pe urmatoarea linie se vor afisa, în ordine cronologică, toate momentele de timp la care au fost făcute fotografii în decursul zilei.

## Restricţii si precizari
1 ≤ K ≤ 20
0 ≤ Ni ≤ 1.000.000
Fotografiile fiecărei echipe sunt deja sortate în ordine cronologică.
## Exemplu
interclasari.in
```
3
6
0 7 8 11 12 15
0
2
6 12
```
interclasari.out
```
8
0 6 7 8 11 12 12 15
```
Explicaţie
În total au fost realizate 8=6+0+2 fotografii. Puse în ordine cronologică, ele au fost realizate la momentele de timp 0, 6, 7, 8, 11, 12, 12 şi 15.