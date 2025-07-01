#include <iostream>
using namespace std;

// OBS: urmatoarele 2 sintaxe sunt echivalente:
// int* x;
// int *x;

class VectorInt
{
    private:
        int x; // variabila care nu e alocata dinamic
        int *a; // variabila care e alocata dinamic - va primi o singura valoare
        int dim; // pentru ca nu am o functie ce imi poate masura lungimea unui vector pentru int,
        // voi folosi dim ca fiind dimensiunea vectorului
        int *vector; // variabila care e alocata dinamic - va primi un vector
    
    public:
        // constructor fara parametri
        VectorInt() : x(0), dim(1) // lista de initializare - se poate folosi doar pt date care nu sunt alocate dinamic
        {
            this->a = new int(5); // e ca si cum am avea "a = 5" pentru o variabila "normala"

            this->vector = new int[this->dim]; // alocam dinamic un vector cu 1 element
            this->vector[0] = 10; // initializam primul element al vectorului - optional
        }

        // constructor complet parametrizat (pentru toate variabilele am cate un parametru)
        // e comentat deoarece trebuie sa ne asiguram inainte ca apelarea lui e coerenta
        // de exemplu, daca "dim" > dimensiunea reala a vectorului, vom obtine eroare. Incercam sa ajungem la un index
        // la care vectorul nu exista/nu are sens/nu are memorie
        // VectorInt(int x, int* a, int dim, int* vector) : x(x), dim(dim) // constructor parametrizat cu lista de initializare
        // {
        //     this->a = new int(*a); // alocam dinamic si initializam "a" cu valoarea "*a"
        //     // *a inseamna valoarea retinuta de pointerul a

        //     this->vector = new int[this->dim]; // alocam dinamic un vector cu "size" elemente
        //     for (int i = 0; i < this->dim; ++i)
        //     {
        //         this->vector[i] = vector[i]; // initializam fiecare element al vectorului (eu mi-am ales niste valori oarecare)
        //     }
        // }

        // Copy constructor
        VectorInt(const VectorInt& other) : x(other.x), dim(other.dim)
        {
            // Alocam dinamic si copiem valorile din alocarea dinamica
            this->a = new int(*other.a);
            this->vector = new int[this->dim];
            for (int i = 0; i < this->dim; ++i)
            {
                this->vector[i] = other.vector[i];
            }
        }


        VectorInt& operator=(const VectorInt& other)
        {
            if (this != &other) // verificam daca nu facem o auto-atribuire
            {
                // Eliberam memoria alocata anterior - vor veni date noi acolo
                if (this->a != NULL)
                    delete this->a;
                if (this->vector != NULL)
                    delete[] this->vector;

                // Copiem valorile/variabilele "normale" din obiectul other
                this->x = other.x;
                this->dim = other.dim;

                // Alocam dinamic si copiem valorile din alocarea dinamica
                this->a = new int(*other.a);
                this->vector = new int[this->dim];
                for (int i = 0; i < this->dim; ++i)
                {
                    this->vector[i] = other.vector[i];
                }
            }
            return *this; // returnam referinta la obiectul curent
        }

        friend istream& operator>>(istream& in, VectorInt& obj)
        {
            cout << "Introduceti valoarea pentru x: ";
            in >> obj.x;

            cout << "Introduceti valoarea pentru a: ";
            int tempA;
            in >> tempA; // citesc intr-o variabila temporara
            if (obj.a != NULL) // golesc vechea memorie a lui a
                delete obj.a;
            obj.a = new int(tempA);

            cout << "Introduceti dimensiunea vectorului: ";
            in >> obj.dim;

            if (obj.vector != NULL)
                delete[] obj.vector;
            obj.vector = new int[obj.dim];

            cout << "Introduceti valorile vectorului: ";
            for (int i = 0; i < obj.dim; ++i)
            {
                in >> obj.vector[i];
            }

            return in;
        }

        friend ostream& operator<<(ostream& out, const VectorInt& obj)
        {
            out << "x: " << obj.x << endl;
            out << "a: " << *obj.a << endl;
            out << "dim: " << obj.dim << endl;
            out << "vector: ";
            for (int i = 0; i < obj.dim; ++i)
            {
                out << obj.vector[i] << " ";
            }
            out << endl;

            return out;
        }

        // Setters
        void setX(int x) { this->x = x; }
        void setA(int value) 
        { 
            if (this->a != NULL)
                delete this->a;
            this->a = new int(value); 
        }
        void setDim(int dim) 
        { 
            if (dim > 0) 
            this->dim = dim; 
        }
        void setVector(const int* vector, int dim) 
        {
            if (this->vector != NULL)
                delete[] this->vector;
            this->dim = dim;
            this->vector = new int[this->dim];
            for (int i = 0; i < this->dim; ++i)
            {
                this->vector[i] = vector[i];
            }
        }

        // Getters
        int getX() const { return this->x; }
        int getA() const 
        { 
            if (this->a != NULL) 
                return *this->a;  
            return 0; // e ca si cum ar fi pe ramura else
        }
        int getDim() const { return this->dim; }
        int* getVector() const { return this->vector; }


        // o functie simpla:
        void adaugaVal(int val) // adauga valoarea in vectorul "vector"
        {
            int* newVector = new int[this->dim + 1]; // alocam un nou vector cu o dimensiune mai mare
            for (int i = 0; i < this->dim; ++i)
            {
                newVector[i] = this->vector[i]; // copiem valorile din vechiul vector
            }
            
            this->dim += 1; // cresc dimensiunea vectorului, acum ca l-am copiat
            newVector[this->dim] = val; // adaugam valoarea la final

            delete[] this->vector; // eliberam memoria vechiului vector
            this->vector = newVector; // actualizam pointerul
        }



        ~VectorInt()
        {
            // aici trebuie eliberata toata memoria alocata dinamic
            // cu alte cuvinte, "a" si "vector"
            
            if(a != NULL) // verific daca pointerul a mai exista - exista situatii in care poate a devenit null
                delete a; // a retine doar o variabila, deci folosim "delete"
                
            if (vector != NULL) // regula ca mai sus
                delete[] vector;
        }
};


int main()
{
    VectorInt primul;
    cout << primul << endl;

    primul.setA(999);

    VectorInt alDoilea(primul);
    cout<< alDoilea << endl;

    alDoilea.setA(-1111);

    cout << primul << endl;
    cout << alDoilea << endl;

}