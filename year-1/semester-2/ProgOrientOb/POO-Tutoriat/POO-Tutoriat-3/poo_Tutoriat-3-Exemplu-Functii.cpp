#include <iostream>
#include <cstring>
using namespace std;

/// VARIANTA 1 - eroarea initiala

// class Angajat
// {
//     private:
//         int varsta;
//         string nume;
//         Functie func; // tipul Functie inca nu exista!!
// };

// class Functie
// {
//     private:
//         string nume;
//         int salariu;
//         Angajat ang;
// };


/// VARIANTA 2 - acum de ce am eroare?

// class Functie;

// class Angajat
// {
//     private:
//         int varsta;
//         string nume;
//         Functie func; // tipul Functie exista, dar nu stim ce contine!!
// };

// class Functie
// {
//     private:
//         string nume;
//         int salariu;
//         Angajat ang;
// };

// desi am anuntat la linia 26 ca vom avea in fisierul nostru
// tipul de date Functie, atunci cand dorim sa il folosim ca atare,
// la linia 33, inca nu stim cum arata (adica ce componente are, si deci,
// compilatorul nu stie cata memorie sa aloce pentru el)

// varianta aceasta e gresita si din alt motiv: redundanta
// un angajat are o functie, dar o functe la randul ei are un angajat, care are
// o functie, care are un angajat, si asa mai departe la infinit.
// Aceasta e o problema de logica a programului. 

// Totusi, cum o reparam?



/// VARIANTA 3 - inca nu am ajuns la corectitudine complete

// class Angajat;
// class Functie;

// class Angajat
// {
//     private:
//         int varsta;
//         string nume;
//         Functie *func; // folosim pointer
// };

// class Functie
// {
//     private:
//         string nume;
//         int salariu;
//         Angajat *ang; // folosim pointer
// };
// PS: trebuie sa scrieti constructorii, operatorul =, destructorul
// pentru ca folosim pointeri. Aici e doar un exemplu didactic teoretic

// mai avem probleme cu memoria? Nu. Stim ca vom aloca pointerului o valoare
// dupa ce terminam clasele, si implicit dupa ce stim ce contine clasa Functie
// sau, oare e asa?

// aici redundanta am putea spune ca se rezolva. De ce?
// un pointer nu inseamna obligatoriu alocare dinamica, ci poate sa arate si catre
// un obiect deja existent


/// CONTRAEXEMPLU
// class Angajat;
// class Functie;

// class Angajat
// {
//     private:
//         int varsta;
//         string nume;
//         Functie *func; // folosim pointer

//     public:
//         int metoda(Functie* obj)
//         {
//             return obj->getSalariu(); // eroare (am compilat in Code::Blocks):
//             // Tutoriat3ExempluFunctii.cpp|103|error: invalid use of incomplete type 'class Functie'|
//         }
// };

// class Functie
// {
//     private:
//         string nume;
//         int salariu;
//         Angajat *ang; // folosim pointer
//     public:
//         int getSalariu()
//         {
//             return this->salariu;
//         }
// };

// eroarea de la linia 103 e obtinuta pentru ca noi incercam sa folosim o functie/componenta
// care inca nu exista. Stim deocamdata doar ca va exista tipul de date "Functie"



/// VARIANTA 4 - doamnelor si domnilor, solutia!

class Angajat;
class Functie; // trebuie totusi sa anunt tipul de date, daca vreau
// sa il folosesc intr-o clasa scrisa inaintea lui

class Angajat
{
    private:
        int varsta;
        string nume;
        Functie *func; // folosim pointer

    public:
        int metoda(Functie* obj);
};

class Functie
{
    private:
        string nume;
        int salariu;
        Angajat *ang; // folosim pointer
    public:
        int getSalariu();
};

int Angajat::metoda(Functie* obj)
{
    return obj->getSalariu();
}

int Functie::getSalariu()
{
    return this->salariu;
}

// Explicatie: in "class Angajat" si "class Functie" doar *am anuntat* ca la un moment
// dat voi scrie implementarea pentru functiile/metodele respective.

// De ce e util sa fac asta?
// Dupa cum am vazut mai sus, daca as scrie implementarile in clase, compilarea se face
// in ordinea liniilor, si implicit nu ar gasi ce inseamna "getSalariu", caci inca nu exista.

// Folosind operatorul de rezolutie "::", am scos *implementarile* metodelor in afara claselor
// si astfel functioneaza, pentru ca asa compilatorul intelege ca implementarea nu inseamna
// acelasi lucru cu antetul.

// Totusi, observatie: daca "metoda" din Angajat foloseste un obiect de tip "Functie", atunci
// "metoda" trebuie scrisa in cod dupa *corpul* clasei "Functie".
// Daca mut implementarea pentru "metoda" inaintea clasei "Functie", obtin iar eroare