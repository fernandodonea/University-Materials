# PAOJ Laborator 4

# ex 1

Se da un string str citit de la tastatura sau declarat direct in program. 
 
Sa se afise substringul de lungime maxima al lui str ale carui caractere (excluzand cifrele) se afla in ordine alfabetica.
Str poate contine litere mici si cifre.

## ex 2
Se considera doua strignuri str1 si str2 definite direct in metoda main. Stringurile contin doar litere mici.

Sa se verifice daca str1 reprezinta o permutare a literelor din str2.

Exemplu :
```
Str1:”abc” e permutare str2=”cab”
```

## ex 3

Modelati un sistem simplificat de cursuri universitare digitale.
Vor fi create cel putin 4 clase:
- `Facultate`
- `Profesor`
- `Curs`
- `Lectie curs`

In definirea relatiilor dintre clase folositi **agregare** sau **compozitie** respectand urmatoarele reguli:
1. Un profesor poate sa colaboreze cu mai multe facultati
2. Orice facultate ofera unul sau mai multe cursuri
3. Orice curs are un profesor care il tine si mai multe lectii de curs.
4. Lectiile de curs sunt specifice unui curs si nu pot fi refolosite intre 2 cursuri diferite
5. Cand un curs e scos din curicula nu trebuie sa mai existe nici lectiile de curs asociate

Implementati:

- **Constructori**(inclusiv copiere unde e cazul)
- **Metode de acces** private/public/protected in functie de caz
- **Suprascrieti** metoda `toString`() pt fiecare clasa
- Operatiile de : 	
  - Stergere/Adaugare profesor la o facultate
  - Listarea tuturor profesorilor unei facultati
  - Adaugare/stergere curs la o facultate
  - Cautare unui curs in cadrul unei facultati dupa un nume sau un cuvant cheie din descrierea cursului
  - Adaugare/stergere unei lectii in cadrul unui curs
