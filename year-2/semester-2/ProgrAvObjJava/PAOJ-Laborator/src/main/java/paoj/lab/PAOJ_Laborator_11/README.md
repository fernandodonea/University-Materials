Laborator 11

# ex 1

Se consideră clasa:
```java
public class Student 
{
    private String nume;
    private String grupa;
    private double nota;
    
    public Student(String nume, String grupa, double nota) {
    this.nume = nume;
    this.grupa = grupa;
    this.nota = nota;
    }
    
    public String getNume() {
    return nume;
    }
    
    public String getGrupa() {
    return grupa;
    }
    
    public double getNota() {
    return nota;
    }
    
    @Override
    public String toString() {
    return nume + " (" + grupa + ") - " + nota;
    }
}

```


Se dă următoarea listă de studenți:
```java
List<Student> studenti = List.of(
new Student("Ana", "MI221", 9.5),
new Student("Bogdan", "MI221", 4.8),
new Student("Cristina", "MI222", 8.7),
new Student("Dan", "MI221", 6.2),
new Student("Elena", "MI222", 10.0),
new Student("Florin", "MI223", 5.5),
new Student("George", "MI223", 3.9),
new Student("Irina", "MI222", 7.8)
);
```
#### ex 1.1
Generati o lista cu numele  tuturor studenților promovați (nota ≥ 5) folosind functiile filter,map, collect.

#### 1.2
Calculați media notelor studenților promovați folosind din Streams API metodele filter() și mapToDouble().

# ex 2

Se da urmatorul tabel

```sql
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100) NOT NULL,
category VARCHAR(50) NOT NULL,
price DOUBLE NOT NULL,
stock INTEGER NOT NULL
);
```

Se considera urmatoarea clasa ce modeleaza o intrare din tabelul de mai sus
```java
public class Product {
    private int id;
    private String name;
    private String category;
    private double price;
    private int stock;

}
```

Implementati intr-o clasa interfata `ProductDao`(Dao=data acces object ) de mai jos si exemplificati intr-o metoda main cate un apel al fiecarei metode implementate. 
Clasa Product poate fi imbunatatita adaugand cosntructori, metode setter/getter sau alte functii.
Optional pot fi adaugate si alte clase in implementarea interfetei.

```java
public interface ProductDao {

    /* insereaza in baza de date un produs al carei date vin prin parametrul 'product' */
    void create(Product product);

    /*
    intoarce inapoi din baza de date toate produsele sub forma unei liste
     daca nu exista nici un produs se va returna o lista goala
     */
    List<Product> findAll();


    /*
    intoarce din baza de date un produs cu id-ul dat
    daca nu exista  nici un produs cu id-ul respectiv se va returna null
     */
    Product findById(int id);


   
    /*
    * returneaza toate produsele din baza care au aceasta categorie
    * daca nu exista nici un produs se va returna o lista goala
     */
    List<Product> findByCategory(String category);


    /*
     pentru produsul cu id-ul dat updateaza pretul si stocul
     daca nu exista nici un produs cu id-ul dat se va arunca o exceptie custom
     */
    void updatePriceAndStock(int id, double price, int stock);


    /*
    sterge din baza produsul cu id-ul dat ca parametru
     */
    void deleteById(int id);
}
```

