# Paoj Laborator 9

## Exercitiul 1

Scrie un program Java care citește din fișierul `parole.txt` mai multe linii, fiecare linie conținând un `username` și o `parolă` separate prin virgulă.

Exemplu:
```
ana/Parola123
ion/abcn
maria/Test2024!
```

Cerințe:
1. Programul citește toate liniile din fișier folosind Scanner.
2. Pentru fiecare linie, separă username-ul și parola după caracterul “/”.
3. Verifică dacă parola e formata doar din cifre de la 1-5 si/sau litere.
4. Verifică dacă parola conține cel puțin o cifră si o litera mare.


## Exercitiul 2
Scrie un program Java care citește din fișierul examene.txt informații despre studenți și notele lor la mai multe materii.
Formatul fiecărei linii este:

Nume,materie1, materie2, materie3,... materien

Numarul de materii poate varia de la 1..n un de 1<=n<50


Exemplu:
```
Ana,9,10,8, 5, 6
Ion,7,abc,6, 3
Maria,10,9
George,11,8,7
Elena,5,4,3
```

Cerințe:

1. Programul citește toate liniile din fișier
2. Pentru fiecare student:
   - verifică dacă linia conține un nume urmat de un numar variabil de note(numere intregi)
   - convertește notele la int;
   - verifică dacă toate notele sunt între 1 și 10.
3. Pentru fiecare student valid:
   - calculează media notelor;
   - stabilește statusul:
     - PROMOVAT dacă media ≥ 5;
     - RESPINS altfel.

3. Scrie rezultatele în fișierul rezultate_examene.txt în format:
```
Ana - media:5.6 - PROMOVAT
Elena - media: 4.0 - RESPINS
```
