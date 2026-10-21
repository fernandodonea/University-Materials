# Paoj Laborator 7





## Exercițiul 1:
Scrie un program care:
- citește două numere dintr-un fișier paragraph (numere.txt)
- realizează împărțirea primului la al doilea


- tratează următoarele excepții:
    - `FileNotFoundException` => cand fisierul nu exista(nume gresit sau nu exista pe disc)
    - `InputMismatchException` => cand apelam o functie care se asteapta sa citeasca un anumit tip de data dar in fisier exista alt timp. De exemplu daca avem un string intr-un fisier si-l citim ca nr
    - `ArithmeticException` => apare cand facem o operatie care nu are sens pentru numere. Ex /0

## Exercițiul 2:
Modifică programul de mai sus astfel încât să:
- se folosească de Scanner pentru citire și de PrintWriter pentru afișarea rezultatului într-un fișier `rezultat.txt`

## Exercițiul 3:

Implementeaza un program care citeste din fisierul date.txt mai multe cuvinte si verifica pentru fiecare in parte de cate ori apare pentru un site predefinit. (vezi exemplul de mai jos)
```java
URL url = new URL("https://www.gsp.ro/");
InputStream is = url.openStream();

int ptr = 0;
StringBuffer buffer = new StringBuffer();
while ((ptr = is.read()) != -1) 
{
    buffer.append((char)ptr);
}
System.out.println(buffer);

```


## Exercițiul 4:

Ai un fișier `cuvinte.txt` cu 10 cuvinte.

Programul alege unul aleator și îl oferă jucătorului pentru un joc de tip „**Spânzurătoarea**”:
- Se vor afisa toate literele cuvantului ales mai putin prima si ultima
- Jucatorul va introduce de la consola in ordine doua litere reprezentand prima si ultima din cuvant
- In cazul in care nu sunt introduse caractere valide(ex: % ^&) sa se trateze exceptia si sa se prezinte un mesaj edificator

## Exercițiul 5
:
Sa se scrie o clasa `ParserCSV` folosita pentru a parsa informatii dintr-un fiesier `CSV`(comma separated value).
Informatiile din fisier sunt pe mai multe linii, iar fiecare linie are cuvintele separate prin virgula.
- Va contine un **singur** constructor in care se va seta numele fisierului din care se face citirea
- Va implementa metodele `readInt` si `readString` din fisier care citesc de pe linia curenta urmatorul **token**(cuvant separat prin virgula) ca intreg, respectiv string. Se va arunca e exceptie relevanta in cazul in care datele nu pot fi convertite la tipul asteptat.
- Daca nu mai exista tokens pe o linie va returna valoarea null
- Metoda nextLine muta cursorul de citire pe urmatoarea linie
- Sa se exemplifice in main cateva apeluri ale metodelor descrise mai sus.

Exemplu fisier
```txt
12, student, 12x4
100, facultatate, rezultat
```
readInt va return 12

readString va returns ‘student’

readInt va arunca o exceptie

nextLine urmat de reatInt va returna 100

readInt va arunca o exceptie

readString va returna ‘rezultat’

readString va returna Null intrucat nu mai sunt tokens pe aceasta linie

