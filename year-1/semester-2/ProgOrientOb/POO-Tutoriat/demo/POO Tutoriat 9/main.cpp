#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

class jucarie
{
    protected:
        string denumire;
        double dimensiune;
        string tip;
    public:
        jucarie()=default;
        jucarie &operator=(const jucarie&)=default;

        friend std::istream& operator>>(std::istream&, jucarie&);
        friend std::ostream& operator<<(ostream&, jucarie&);

        virtual std::istream& citire(std::istream&);
        virtual ostream& afisare(std::istream&);

        virtual ~jucarie();
};

std::istream& operator>>(std::istream&is, jucarie&jucarie);
{
    std::cout<<"Denumire: ";
    is>>jucarie.denumire;
}









int main()
{
    cout<<"hello world";
    return 0;
}