# Paoj Laborator 8

Implementati o aplicatie Java de tip **joc de întrebări și răspunsuri**.

Aplicația citește întrebările dintr-un fișier, răspunsurile corecte din alt fișier și permite utilizatorului să joace un quiz în consolă.

Pentru eficiență, întrebările și răspunsurile trebuie **cache-uite** în memorie, astfel încât fișierele să nu fie recitite la fiecare rundă.
**Cachingul** se face la pornirea aplicatiei si se reseteaza dupa 10 accesari aleatorii.

Fiecare utilizator trebuie sa-si defineasca un username unic si o parola inainte de a putea juca.
Daca utilizatorul are deja cont prima data va trebui sa se logheze inainte de a se putea juca.

Aplicatia va retine intre rulari userii creati precum si scorul lor.

Dupa ce un utilizator e logat aplicatia va afisa scorul lui, un leaderboard cu scorurile a top 10 utilizatori precum si pozitia utilizatorului in leaderbord.

nformatiile despre leaderboard, precum si credentiale se vor salva in unul sau mai multe fisiere.

Fișierul
`questions.txt`

Fiecare linie conține un identificator unic și textul întrebării:
```
Q1;Care este capitala Franței?
Q2;Câte zile are un an bisect?
Q3;Ce limbaj rulează pe JVM?
Q4;Care este rezultatul expresiei 2 + 2 * 3?
```

Fișierul answers.txt

Fiecare linie conține identificatorul întrebării și răspunsul corect:
```
Q1;Paris
Q2;366
Q3;Java
Q4;8
```
