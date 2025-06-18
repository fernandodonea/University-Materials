#include <iostream>
#include <string>
using namespace std;


class Curs
{
    protected:
        string denumire;
        unsigned pret;
        string durata;
        static int counter;
        int id;
    public:
        Curs():id(counter++){};
        Curs(const Curs&)=default;
        Curs& operator=(const Curs&)=default;

        friend istream& operator>>(istream&, Curs&);
        friend ostream& operator<<(ostream&, const Curs&);

        virtual istream& citire(istream&);
        virtual ostream& afisare(ostream&) const;



        virtual ~Curs()=default;
       
       
};




class Persoana
{
    protected:
        string nume;
        string prenume[60];
        unsigned vechime;

        Curs cursuri[10];
    public:
        Persoana();
        virtual ~Persoana()=default;
        Persoana(const Persoana&)=default;
        virtual void addCurs();//o suprascriem in fiecare, la student iei pretul si inmultesti cu 0.5
};

class Student: public Persoana
{
    private:
        string universitate;
        unsigned an;
    public:
        Student();
        virtual ~Student()=default;
        Student(const Student&);
};
class Angajat: public Persoana
{
    private:
        string tipContract;
    public:
        Angajat();
        virtual ~Angajat()=default;
        Angajat(const Angajat&);
};
class Somer:public Persoana
{
    private:
        string ultimLocMunca;
    public:
        Somer();
        virtual ~Somer()=default;
        Somer(const Somer&);
        //daca tipul cursului e initiere, pretul cursului e zero else 0.5*pret
};


int main()
{




    
    return 0;
}