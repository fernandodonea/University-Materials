# PAOJ Laborator 3

## ex 1
Sa se defineasca clasa abstracta `User` care :

- a) Contine urmatoarele campuri :  
  - String `username`,  
  - String `password`, 
  - Boolean `isAuthenticated`, 
  - Integer `id`.

- b)Are definite metodele abstracte `login` si `generateId`.
  - Metoda abstracta generateId() nu are parametrii
  - Metoda abstracta login fara parametrii
  - Metoda publica isLoggedIn() fara alte argumente si returneaza true sau false daca userul s-a logat sau nu.
  - in interiorul clasei sa se suprascrie metodata equals astfel incat 2 instante diferite sunt egale daca au campul id egal.

- c) Sa se defineasca un constructor fara parametrii al clasei User ce initializeaza campul id  apeland metoda generateId() din aceeasi clasa.



## ex 2
Folosind clase User de la 1) sa se defineasca clasa `InMemoryUser`  ce o mosteneste. 

In plus:
- contine 2 campuri noi reprezentand 2 vectori de Strings cu aceeasi dimensiune si valori _predefinite_. Cei 2 vectori reprezinta 2 liste cu combinatii de username si parole valide.
- Pentru implementarea metodei `login` se va verifica existenta variabilelor de instanta username si password in vectorii mentionati anterior.
- Metoda `generateId` se va implementa astfel incat id-ul generat sa fie **unic** pentru fiecare instanta a clasei.
- Sa se **suprascrie** metoda `toString`() a clasei InMemoryUser  astfel incat sa afiseze  campul `id`


## ex 3

Scrieti un program care implementeaza functionalitatea de **catalog digital** pentru studenti si profesori  :


Vor fi definite cel putin 3 clase : `Facultate`, `Elev`, `Profesor`

- `Elevii` pot selecta o facultate si cauta dupa un cuvant cheie numele unei materii.  Pentru o materie returnata elevii vor putea vedea doar nota lor.  
- `Profesorii` pot 
  - selecta o facultate si cauta dupa un cuvant cheie numele unei materii.
  - Cauta un student dupa nume si/sau prenume
  - Adauga note unui student pentru o materie. O nota poate fi si editata.
  
- `Clasele` vor avea campuri publice si cel putin unul privat. Pot fi definite si alte clase.
- Pentru fiecare clasa vom avea nevoie de un camp care sa identifice in mod unic o instanta. NU e mandatoriu ca unicitatea sa persiste intre rulari diferite ale programului
- **Suprascrieti** metoda `toString` astfel incat sa afiseze informatii relevante despre fiecare instanta. Nu expuneti informatii senzitive(exemplu: CNP)
- creati cateva instante ca sa exemplificati implementarile. 

