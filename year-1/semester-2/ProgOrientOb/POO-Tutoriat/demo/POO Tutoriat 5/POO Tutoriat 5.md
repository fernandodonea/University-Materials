# POO Tutoriat 5
2 aprilie 2024

## Constructorii clasei derivate
- apelati in oridinea creării obiectelor, a moștenirii

**Apel constructori**:
1. constructor moștenire
```c++
class D: public B {...}//mai intai se apeleaza constructorul pentru B
```
2. constructori ale obiectelor memebre
```c++
class B
{
    class A a;//mai intai se apreaza constructorul pentru A
}
```
3. Următorul nivel de moștenire

## Constructorul de copiere
Fie B=baza si D=derivata
1. **Daca B si D** nu au definit constructor de copiere => se apeleaza cel creat de catre compilator
2. **Daca B il are si D nu** => compilatorul creeaza un construcyor pentru D care apeleaza constructorul de copiere din clasa B
3. **daca B si D il au **=> lui D ii revine in totalitate sarcina transferarii valorilor corespunzatoare membrilor ce apartin clasei de baza

## Redefinirea functiilor membre in derivata

Modalidati:
1) cu acelasi antet ca in clasa derivata
2) cu schimbarea listei de argumente / a tipului

-> *Important*:
la redefinirea unei functii din baza, toate celellalte versiunii ale ei sunt automat ascunse
