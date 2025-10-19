/* Donea Fernando-Emanuel 143
 Clion
 Alexandru Cristian Virgil Precupetu */

#include <iostream>
using namespace std;



class Produs
{
protected:
    string nume;
    float gramaj;
    int energie_preparare;
public:
    Produs()=default;
    Produs(const Produs&)=default;
    Produs& operator=(const Produs&)=default;
    virtual ~Produs()=default;

    friend istream& operator>>(istream&, Produs&);
    friend ostream& operator<<(ostream&, Produs&);

    virtual istream& citire(istream&) ;
    virtual ostream& afisare(ostream&) ;


    virtual void calcEnergie()=0;

};

istream& Produs::citire(istream&is)
{
    cout<<"nume produs:";is>>nume;
    cout<<"gramaj:";is>>gramaj;
    return is;
}

ostream& Produs::afisare(ostream&os)
{
    os<<"nume produs:"<<nume<<"\n";
    os<<"gramaj:"<<gramaj<<"\n";
    os<<"energie preparare:"<<energie_preparare<<"\n";
    return os;
}

istream& operator>>(istream&is, Produs&p)
{
    return p.citire(is);
}

ostream& operator<<(ostream&os, Produs&p)
{
    return p.afisare(os);
}








class Bautura: public Produs
{
protected:
    bool sticla;
public:
    Bautura():sticla(false){}
    Bautura(const Bautura&)=default;
    Bautura& operator=(const Bautura&)=default;
    virtual ~Bautura()=default;


    virtual istream& citire(istream&) override ;
    virtual ostream& afisare(ostream&)  override;



    void calcEnergie() override;

};

istream& Bautura::citire(istream&is)
{
    Produs::citire(is);

    string opt;
    cout<<"Sticla?da/nu";is>>opt;
    if (opt=="da")
        sticla=true;
    return is;
}

ostream& Bautura::afisare(ostream&os)
{
    os<<"Bautura"<<"\n";
    Produs::afisare(os);
    os<<"sticla:";
    if (sticla==true)
        os<<"da"<<"\n";
    else os<<"nu"<<"\n";
    return os;
}

void Bautura::calcEnergie()
{
    if (sticla==false)
    {
        energie_preparare=25;
    }
    else
    {
        energie_preparare=gramaj*0.25;
    }

}





class Desert: public Produs
{
protected:
    string format_servire;
public:
    Desert()=default;
    Desert(const Desert&)=default;
    Desert& operator=(const Desert&)=default;
    virtual ~Desert()=default;


    virtual istream& citire(istream&) override;
    virtual ostream& afisare(ostream&)override ;


    void calcEnergie() override;

};

istream& Desert::citire(istream&is)
{
    Produs::citire(is);
    cout<<"format servire:";is>>format_servire;
    return is;
}

ostream& Desert::afisare(ostream&os)
{
    os<<"Desert"<<"\n";
    Produs::afisare(os);
    os<<"format servire:"<<format_servire<<"\n";
    return os;
}

void Desert::calcEnergie()
{
    if (format_servire=="felie")
        energie_preparare=25;
    else if (format_servire=="portie")
        energie_preparare=0.5*gramaj;
    else if (format_servire=="cupa")
        energie_preparare=2*gramaj;
}









class Burger: public Produs
{
protected:
    vector<string> ingrediente;
public:
    Burger()=default;
    Burger(const Burger&)=default;
    Burger& operator=(const Burger&)=default;
    virtual ~Burger()=default;


    virtual istream& citire(istream&) override ;
    virtual ostream& afisare(ostream&)override ;


    void calcEnergie() override;

};

istream& Burger::citire(istream&is)
{
    Produs::citire(is);

    int n;
    cout<<"introduceti numarul de ingrediente:";is>>n;
    for (int i=1;i<=n;i++)
    {
        string temp;
        cout<<"ingredient "<<i<<":";
        is>>temp;
        ingrediente.push_back(temp);
    }
    return is;
}

ostream& Burger::afisare(ostream&os)
{
    os<<"Burger"<<"\n";
    Produs::afisare(os);
    os<<"ingrediente:";
    for (auto i:ingrediente)
    {
        os<<i<<" ";
    }
    os<<"\n";

    return os;
}

void Burger::calcEnergie()
{
    cout<<ingrediente.size();
    energie_preparare=gramaj*0.25*ingrediente.size();
}








class Angajat
{
protected:
    string tip;
    int puncte_energie;
public:
    Angajat():puncte_energie(100){}
    Angajat(const Angajat&)=default;
    Angajat& operator=(const Angajat&)=default;
    virtual ~Angajat()=default;

    friend istream& operator>>(istream&, Angajat&);
    friend ostream& operator<<(ostream&, Angajat&);

    virtual istream& citire(istream&) ;
    virtual ostream& afisare(ostream&) ;

    string getTip() const{return tip;}
    int getEnergie() const{return puncte_energie;}
    void scadeEnergie(int val){puncte_energie-=val;}
    void resetEnergie(){puncte_energie=100;}
};

istream& operator>>(istream&is, Angajat&a)
{
    return a.citire(is);
}

ostream& operator<<(ostream&os, Angajat&a)
{
    return a.afisare(os);
}

istream& Angajat::citire(istream&is)
{
    string opt;
    cout<<"tip(casier,livrator,bucatar)";is>>opt;
    if (opt=="casier" || opt=="livrator" || opt=="bucatar")
    {
        tip=opt;
    }
    else cout<<"Nu exista acest tip de angajat"<<endl;
    return is;
}

ostream& Angajat::afisare(ostream&os)
{
    os<<"tip"<<tip<<"\n";
    return os;
}



class Comanda
{
private:
    static int counter;
    int id;
    vector<Produs*> produse;
public:
    Comanda():id(++counter){}
    Comanda(const Comanda&){}
    Comanda& operator=(const Comanda&);
    virtual ~Comanda()=default;

    friend istream& operator>>(istream&, Comanda&);
    friend ostream& operator<<(ostream&, Comanda&);

    virtual istream& citire(istream&) ;

    //functie de tip factory
    Produs* createProdus(string type);

};
int Comanda::counter=0;

istream& operator>>(istream&is, Comanda&c)
{
    return c.citire(is);
}



istream& Comanda::citire(istream&is)
{
    int n;
    cout<<"Comanda"<<id<<endl;
    cout<<"nr produse:";
    is>>n;
    for (int i=1;i<=n;i++)
    {
        string tip;
        cout<<"Ce tip de produs este?";is>>tip;
        Produs* obj=createProdus(tip);
        if (obj)
        {
            cin>>*obj;
            //calculam energie
            obj->calcEnergie();
            produse.push_back(obj);
        }
    }
    return is;
}


Produs* Comanda::createProdus(string type)
{
    if (type=="bautura")
        return new Bautura;
    if (type=="desert")
        return new Desert;
    if (type=="burger")
        return new Burger;
    else return nullptr;
}


class ApLivrari
{
private:
    vector<Angajat*> angajati;
    vector<Comanda*> comenzi;

    ApLivrari()=default;
    ApLivrari(const ApLivrari&) = delete;
    ApLivrari& operator=(const ApLivrari&) = delete;

    inline static ApLivrari* instance = nullptr;

public:
    ~ApLivrari();
    static ApLivrari* getInstance();

    void adaugaAngajat();
    void afisareAngajati();

    void simulareCiclu();
    void adaugaComenzi();
    void preluareComenzi();
    void preparareComenzi();
    void livrareComenzi();


};



ApLivrari* ApLivrari::getInstance()
{
    if (instance == nullptr)
    {
        instance = new ApLivrari();
        return instance;
    }
    else return instance;
}

void ApLivrari::adaugaAngajat()
{
    Angajat *a=new Angajat();
    cin>>*a;
    angajati.push_back(a);
}

void ApLivrari::afisareAngajati()
{
    string tip;
    cout<<"ce tip de angajat?";
    cin>>tip;
    int k=0;
    for (auto a:angajati)
    {
        if (a->getTip()==tip)
            k++;
    }
    cout<<k<<" angajati de tip "<<tip<<endl<<endl;
}

void ApLivrari::simulareCiclu()
{
    for (auto a: angajati)
    {
        a->resetEnergie();
    }
    int opt=1;
    while (opt==1)
    {
        cout<<"1/0";
        cin>>opt;
        cout<<endl;
        if (opt==0)break;
        adaugaComenzi();

        //preluare
        bool preluat=false;
        for (auto a:angajati)
        {
            if (a->getTip()=="casier")
            {
                if (a->getEnergie()>=25)
                {
                    a->scadeEnergie(25);
                    preluat=true;
                }
            }
        }
        if (preluat==false)
        {
            for (auto a:angajati)
            {
                if (a->getEnergie()>=100)
                {
                    a->scadeEnergie(100);
                    preluat=true;
                }
            }
        }
        if (preluat==true)cout<<"Comanda preluata"<<endl;
        if (preluat==false)cout<<"comanda nu a putut fi preluata"<<endl;
    }


    //preparari comenzi
    for (auto c :comenzi)
    {

    }
}

void ApLivrari::adaugaComenzi()
{
    Comanda *c=new Comanda();
    cin>>*c;
    comenzi.push_back(c);
}

void meniu()
{
    int opt;
    cout << "1. Afisare angajati" << endl;
    cout<<"2. Simulare ciclu"<<endl;
    cout<<"3. Exit"<<endl;
    cout << "Opt. dvs:";
    try
    {
        cin >> opt;
        if (cin.fail())
        {
            cin.clear();
            cin.ignore(1000, '\n');
            throw string("Format invalid");
        }
        if (opt < 1 || opt > 3)
            throw string("Optiune invalida");
        switch (opt)
        {
        case 1: ApLivrari::getInstance()->afisareAngajati();break;
        case 2:ApLivrari::getInstance()->simulareCiclu();break;
        case 3: return;
        }
    }
    catch (string s) { cout << s << endl; }
    meniu();
}

int main()
{
    int n;
    cout<<"Cati anagajati are firma?";cin>>n;
    for (int i=1;i<=n;i++)
    {
        ApLivrari::getInstance()->adaugaAngajat();
    }
    meniu();
    return 0;
}
