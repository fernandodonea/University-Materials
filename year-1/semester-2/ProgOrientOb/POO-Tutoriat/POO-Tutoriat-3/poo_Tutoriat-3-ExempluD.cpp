#include <iostream>
#include <string>
using namespace std;

class Persoana
{
    private:
        static int CONTOR;
        const int ID;
        string nume;
        int varsta;
    public:
        // Constructor
        Persoana(string nume, int varsta) : ID(++CONTOR), nume(nume), varsta(varsta) {}

        // Copy constructor
        Persoana(const Persoana& obj) : ID(++CONTOR), nume(obj.nume), varsta(obj.varsta) {}

        // Assignment operator
        Persoana& operator=(const Persoana& obj) 
        {
            if (this != &obj) 
            {
                nume = obj.nume;
                varsta = obj.varsta;
            }
            return *this;
        }

        // Destructor
        ~Persoana() {}

        // Operator citire
        friend istream& operator>>(istream& in, Persoana& p) {
            cout << "Nume: ";
            in >> p.nume;
            cout << "Varsta: ";
            in >> p.varsta;
            return in;
        }

        // Operator afisare
        friend ostream& operator<<(ostream& out, const Persoana& p) {
            out << "ID: " << p.ID << ", Nume: " << p.nume << ", Varsta: " << p.varsta;
            return out;
        }

        // Getter pentru ID
        int getID() const {
            return ID;
        }

};

int Persoana::CONTOR = 100;

int main()
{
    Persoana pers[] = {Persoana("Mihai Nicolae", 20),Persoana("Am uitat cum ma cheama", 25)};

    // observam ca variabile COUNTER din clasa Persoana ne ajuta
    // sa tinem evidenta obiectelor in cauza.
    cout<<pers[0]<<endl<<pers[1]<<endl;

    // de exemplu, caut persoana cu ID-ul 101:
    for (int i=0; i<2; ++i)
        if(pers[i].getID() == 101)
            cout<<pers[i]<<endl;
}