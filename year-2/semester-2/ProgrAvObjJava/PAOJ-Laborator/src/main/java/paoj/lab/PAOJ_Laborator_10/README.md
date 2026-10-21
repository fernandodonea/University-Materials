# Paoj Laborator 10

## Exercitiul 1
Creează o clasă `Studet` cu câmpuri: nume, grupa, List<Integer> note, double medie. Fiecare obiect trebuie să fie serializabil.
1. Creează o colecție List<Student> cu cel puțin 5 obiecte.

2. Salvează lista într-un fișier binar folosind serializarea.


3. Încarcă lista din fișier și afișează la consola doar studenții cu medie >= 8


## Exercitiul 2

Pentru clasa Student de mai sus (fără metodele hashCode() și equals() suprascrise)creati doi studenți cu aceleași date și inseratii într-un HashSet<Student>.
Afisati la consola dimensiunea hashsetului.
Suprascieti metodele equals() și hashCode() corect, astfel încât HashSet să nu contina studenti cu aceleasi informatii. Adaugati 2 studenti apoi cu date identice si afisati dimensiunea HashSet-ului

```xml
<dependencies>
   <!-- https://mvnrepository.com/artifact/mysql/mysql-connector-java -->
   <dependency>
       <groupId>mysql</groupId>
       <artifactId>mysql-connector-java</artifactId>
       <version>8.0.22</version>
   </dependency>


   <!-- Source: https://mvnrepository.com/artifact/org.xerial/sqlite-jdbc -->
   <dependency>
       <groupId>org.xerial</groupId>
       <artifactId>sqlite-jdbc</artifactId>
       <version>3.53.1.0</version>
       <scope>compile</scope>
   </dependency>


   <!-- Source: https://mvnrepository.com/artifact/org.postgresql/postgresql -->
   <dependency>
       <groupId>org.postgresql</groupId>
       <artifactId>postgresql</artifactId>
       <version>42.7.11</version>
       <scope>compile</scope>
   </dependency>
</dependencies>


```
```java
//  jdbc:{baza-de-date}://{server}:{port}/{database-name}, {db-user}, {db-user-password}                
// Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/andrei", "root", "mysecretpassword");
```

## Twitter in consola
Creeaza o aplicatie de tip retea “Twitter”(X) fara interfata grafica.
Inputul utilizatorului va fi doar de la tastatura.
Fiecare utilizator va avea un username, parola precum si datele personale de baza(nume, prenume, email, varsta) salvate intr-o baza de date. Parola  se va salva in baza de date ca un hash folosind un salt citit dintr-o variabila de mediu.
Simularea interfetei grafice se va face printr-un meniu basic in consola. De ex: pentru a se loga se va selecta o comanda dintr-un meniu si ulterior utilizatorii vor primii in consola un mesaj care le cere sa introduca username-ul si apoi parola

Utilizatorii pot :
- Sa-si creeze cont adaugand datele de mai sus
- Sa se logheze in aplicatia folosind username-ul si parola definite
- Sa posteze tweets pe propriul perete. Va exista o optiune in interfata de a vedea peretele unui utilizator
- Sa vizualizeze alti useri in consola si ulterior sa le vada postarile dand ca parametru id-ul ori username-ul lor
- Sa dea mesaje altui utilizator caruia i-a dat in prealabil follow si cererea lui a fost acceptata. Un utilizator dupa ce se logheaza va primi o lista de cereri de follow si va putea sa le accepte ori refuze. In urma acestei interactiuni emitentul cererii de follow va primi o notificare la urmatoare logare care-i va spune daca cererea lui a fost refuzata sau acceptata.
- Cererile de follow vor expira automat dupa o perioada de 7 zile de la initiere. 

