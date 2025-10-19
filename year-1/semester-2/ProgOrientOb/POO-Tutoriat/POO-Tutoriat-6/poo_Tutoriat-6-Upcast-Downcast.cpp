#include <iostream>
#include <string>
#include <typeinfo>

using namespace std;

class Animal {
public:
    virtual void vorbeste() {
        cout << "Animalul face un sunet generic." << endl;
    }
};

class Caine : public Animal {
public:
    void vorbeste() override {
        cout << "Cainele latra: Ham Ham!" << endl;
    }
};

class Pisica : public Animal {
public:
    void vorbeste() override {
        cout << "Pisica miauna: Miau Miau!" << endl;
    }
};

int main() {
    Animal* animal = new Pisica;


    // 1. Static cast: priveste obiectul direct sub alta forma - poate duce la comportament nedefinit
    // sau la eroare, daca obiectul nu poate fi transformat in alta clasa
    // sintaxa:
    // static_cast<tip_la_care_vrem_sa_ajungem>(obiect)

    // Exemplu cu static_cast care poate duce la comportament nedefinit
    Caine* caine = static_cast<Caine*>(animal); // Cast incorect
    if (caine) {
        caine->vorbeste(); // Comportament nedefinit
    } else {
        cout << "static_cast a esuat: animalul nu este un Caine." << endl;
    }

    // Solutie: folosirea typeid pentru a verifica tipul obiectului - typeid
    if (typeid(*animal) == typeid(Caine)) {
        cout << "Animalul este un Caine." << endl;
    } else if (typeid(*animal) == typeid(Pisica)) {
        cout << "Animalul este o Pisica." << endl;
    } else {
        cout << "Animalul este de un alt tip." << endl;
    }


    // 2. Dynamic cast - verifica mai intai daca obiectul se potriveste cu tipul de date
    // la care incercam sa ii dam cast. Daca se potriveste, are loc cast-ul. Daca nu se potriveste,
    // returneaza null
    // sintaxa:
    // dynamic_cast<tip_la_care_vrem_sa_ajungem>(obiect)

    // Exemplu cu dynamic_cast care functioneaza corect
    Caine* caineDinamic = dynamic_cast<Caine*>(animal);
    if (caineDinamic) {
        caineDinamic->vorbeste();
    } else {
        cout << "dynamic_cast a esuat: animalul nu este un Caine." << endl;
    }

    delete animal;
    return 0;
}