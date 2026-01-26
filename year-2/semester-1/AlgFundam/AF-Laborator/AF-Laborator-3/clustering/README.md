# Clustering

Fişierul `cuvinte.in` conţine cuvinte separate prin spaţiu.

 Se citeşte de la tastatură
un număr natural k. Se consideră [distanţa Levenshtein](https://en.wikipedia.org/wiki/Levenshtein_distance.) între două cuvinte

Să se împartă cuvintele din fişier în k clase (categorii) nevide astfel încât gradul de separare
al claselor să fie maxim ( = distanţa minimă între două cuvinte din clase diferite) - v. curs; 

Se vor afişa pe câte o linie cuvintele din fiecare clasă și pe o altă linie gradul de separare al
claselor. O(n2 log n) / O(n2)

cuvinte.in
```
martian care este sinonim ana case apa arbore partial minim
```

Ieșire pentru k=3 (clasele nu sunt
unice, dar gradul de separare da)
```
care este ana case apa arbore
martian partial
sinonim minim
4
```