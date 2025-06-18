#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    vector<int> numbers = {1, 2, 3, 4, 5};

    // Adaugarea elementelor in vector
    numbers.push_back(6); // Adauga elementul 6 la sfarsitul vectorului
    numbers.push_back(7); // Adauga elementul 7 la sfarsitul vectorului

    // Accesarea elementelor din vector
    cout << "Primul element: " << numbers.front() << endl; // Afiseaza primul element din vector
    cout << "Ultimul element: " << numbers.back() << endl; // Afiseaza ultimul element din vector

    // Stergerea ultimului element
    numbers.pop_back(); // Elimina ultimul element din vector
    cout << "Dupa pop_back, ultimul element: " << numbers.back() << endl; // Afiseaza noul ultim element

    // Verificarea dimensiunii si capacitatii vectorului
    cout << "Dimensiune: " << numbers.size() << ", Capacitate: " << numbers.capacity() << endl;
    
    // Iterarea prin vector
    cout << "Elementele din vector: ";
    for (int i=0; i<numbers.size(); ++i) // Parcurge fiecare element din vector
    {
        cout << numbers[i] << " "; // Afiseaza elementul curent
    }
    cout << endl;

    // Inserarea elementelor in vector
    numbers.insert(numbers.begin() + 2, 10); // Insereaza elementul 10 la pozitia 2
    cout << "Dupa inserarea lui 10 la indexul 2: ";
    for (int i=0; i<numbers.size(); ++i) // Parcurge fiecare element din vector
    {
        cout << numbers[i] << " "; // Afiseaza elementul curent
    }
    cout << endl;

    // Stergerea elementelor din vector
    numbers.erase(numbers.begin() + 2); // Sterge elementul de la pozitia 2
    cout << "Dupa stergerea elementului de la indexul 2: ";
    for (int i=0; i<numbers.size(); ++i) // Parcurge fiecare element din vector
    {
        cout << numbers[i] << " "; // Afiseaza elementul curent
    }
    cout << endl;

    // Golirea vectorului
    numbers.clear(); // Elimina toate elementele din vector
    cout << "Dupa golire, dimensiune: " << numbers.size() << endl; // Afiseaza dimensiunea vectorului dupa golire

    // Verificarea daca vectorul este gol
    if (numbers.empty())
    {
        cout << "Vectorul este gol." << endl;
    }
    else
    {
        cout << "Vectorul nu este gol." << endl;
    }

    // Redimensionarea vectorului
    numbers.resize(5, 42); // Redimensioneaza vectorul la 5 elemente, completand cu 42 daca este necesar
    cout << "Dupa redimensionare: ";
    for (int i=0; i<numbers.size(); ++i) // Parcurge fiecare element din vector
    {
        cout << numbers[i] << " "; // Afiseaza elementul curent
    }
    cout << endl;

    // Atribuirea unui nou set de valori
    numbers.assign(3, 99); // Atribuie vectorului 3 elemente, fiecare avand valoarea 99
    cout << "Dupa assign: ";
    for (int i=0; i<numbers.size(); ++i) // Parcurge fiecare element din vector
    {
        cout << numbers[i] << " "; // Afiseaza elementul curent
    }
    cout << endl;

    // Schimbarea continutului cu un alt vector
    vector<int> otherNumbers = {8, 9, 10};
    numbers.swap(otherNumbers); // Schimba continutul vectorului numbers cu otherNumbers
    cout << "Dupa swap, numbers: ";
    for (int i=0; i<numbers.size(); ++i) // Parcurge fiecare element din vector
    {
        cout << numbers[i] << " "; // Afiseaza elementul curent
    }
    cout << endl;

    cout << "Dupa swap, otherNumbers: ";
    for (int i=0; i<otherNumbers.size(); ++i) // Parcurge fiecare element din vector
    {
        cout << otherNumbers[i] << " "; // Afiseaza elementul curent
    }
    cout << endl;

    return 0;
}