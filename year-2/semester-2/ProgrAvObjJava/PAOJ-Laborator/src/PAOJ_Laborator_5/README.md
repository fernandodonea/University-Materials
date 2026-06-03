# PAOJ Laborator 5

## ex 1

Sa se defineasca una sau mai multe clase pentru a modela un **editor de paragraph** cu urmatoarele functionalitati: 		
- Salveaza un memorie un .paragraf
- Pentru sirul de caractere salvat ofera optiunea de a elimina spatiile libere in plus. Exemplu : ‘ana  are    mere’->’ana are mere’
- Poate numara cuvintele din paragraf
- Numara de cate ori apare un cuvant dat intr-un paragraf
- Extrage propozitiile din paragraf. O propozitie e definita ca un sir de caractere continue separate prin caracterele {‘.’, ‘!’, ‘?’ sau ‘...’}
- Pentru un cuvant dat inlocuieste toate aparitiile lui din paragraf cu o varianta a lui formata doar din litere mici.
- Creaza un rezumat al paragrafului concatenand primele 2 cuvinte din fiecare propozitie.
- Sorteaza propozitiile dupa numarul de cuvinte sau lungime. Folositi interfata Comparator.

Pentru a modela editorul de paragraph definiti urmatoarele interfete:

```java
public interface TextProcessor {
    String normalizeSpaces(String paragraph);
    int countWords(String paragraph);
}
```
```java
public interface TextAnalyzer {
    int countOccurrences(String paragraph, String word);
    List<String> extractSentences(String paragraph);
}
```
```java
public interface TextSummarizer {
String summarize(String paragraph);
}
```


## ex 2

Definiti o clasa utilitara `ValidatorInscriereStudent` necesara unui sistem de inscriere online pentru studentii unei facultati.

Clasa trebuie sa implementeze urmatoarele functionalitati:
1. Valideze o forma corecta a unui cnp
2. Valideze o forma corecta a unui numar de telefon
3. Sa valideze campurile pentru nume si prenume.(doar litere)
4. Pentru un string de forma “MM-DD-YYYY” unde MM reprezinta luna, DD reprezinta ziua iar YYYY anul sa extraga anul nasterii unui student ca un numar intreg. Exemplu pt “10-15-2001” se va returna 2001

5. In implementarea validatorului folositi interfata :
```java
public interface Validator<T> {
boolean validate(T value);
}
```

Pentru 1), 2), 3) implementati interfata in cate o clasa separata.

6. Utilizati urmatoarea clasa pentru un validator generic pentru a apela metodele definite a: 
```java
public class ValidationEngine {
public static boolean validate(String value, Validator<String> validator) {
return validator.validate(value);
}
}
```

Exemplu :
```java
Validator startA= new Validator<String>() 
{
    @Override
    public boolean validate(String value) 
    {
        return value.startsWith("A");
    }
};

boolean incepeCuA=ValidationEngine.validate("Aba", startA);
System.out.println(incepeCuA);
```



## ex 3
Se considera urmatoarele clase :
```java
class Facultate 
{
    private String nume;
    public void setNume(String nume) { this.nume = nume; }
    public String getNume() { return nume; }
}
```
```java
final class Student 
{
    private final String nume;
    private final Facultate facultate;

    public Student(String nume, Facultate facultate)
    {
        this.nume = nume;
        this.facultate = facultate;
    }

    public Facultate getFacultate() 
    {
        return facultate;
    }


    public String getNume() {
    return nume;
    }

}
```

6.1 Modificati codul astfel incat clasa Student sa fie imutabila
