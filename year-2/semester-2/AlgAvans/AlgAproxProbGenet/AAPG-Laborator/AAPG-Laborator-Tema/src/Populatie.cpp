//
// Created by Fernando-Emanuel Donea on 08.04.2026.
//

#include "../include/Populatie.h"


/*----------------------------
 *  FUNCTII DE AFISARE
 * -------------------------
*/

void Populatie::afisarePopulatie(std::vector <Individ> populatie)
{

    for (int i=0;i<populatie.size();i++)
    {
        populatie[i].afisare(out);
    }
}

void Populatie::afisareProbabilitati(std::vector<double> p, std::vector<double> q)
{

    out<<std::endl;
    out<<"Probabilitatile de selectie pentru fiecare cromozom"<<std::endl;
    for (int i=0;i<n;i++)
    {
        out<<i+1<<": "<<p[i]<<'\n';
    }

    out<<std::endl;
    out<<"Probabilitatile cumulate care dau intervalele de selectie"<<std::endl;
    for (int i=0;i<n;i++)
    {
        out<<i+1<<": ["<<q[i]<<", "<<q[i+1]<<"]"<<std::endl;
    }

}

void Populatie::afisarePerformantaPopulatie(std::vector <Individ> populatie)
{
    double maxFitness=0, meanFitness=0;
    for (int i=0;i<populatie.size();i++)
    {
        meanFitness=meanFitness+populatie[i].getFitness();
        if (populatie[i].getFitness()>maxFitness)
            maxFitness=populatie[i].getFitness();
    }
    out<<"................................"<<std::endl;
    out<<"Max Fitness: "<<maxFitness<<std::endl;
    out<<"Mean Fitness: "<<meanFitness/populatie.size()<<std::endl;
    out<<"................................"<<std::endl;
}

void Populatie::afisarePopulatieInitiala()
{
    out<<"---------------------------POPULATIE INITIALA-------------------------------";
    out<<std::endl;
    out<<std::endl;
    afisarePopulatie(generatie);
}







/*-------------------------
 *  FUNCTII HELPER
 *--------------------------
 */

Individ Populatie::creazaIndividAleator()
{
    double valoare=getNumarRandomReal(a,b); //numar random din domeniul de definitie

    double fitness=functieGradulDoi(x2,x1,x0,valoare);
    if (fitness<0)
        fitness=1/pow(10,precizie-1);

    int index =(int)((valoare-a)/d); //indexul in intervalul descretizat

    std::string cromozomi=fromIntToBinary(index,l);//reprezentarea binara a nr din intervalul descretizat

    Individ individ=Individ(cromozomi,valoare, fitness);
    return individ;
}

Individ Populatie::creeazaIndividFromString(std::string s)
{
    int index=fromBinaryToInt(s);
    double valoare=a+index*d;

    double fitness=functieGradulDoi(x2,x1,x0,valoare);
    if (fitness<0)
        fitness=1/pow(10,precizie-1);

    Individ individ=Individ(s,valoare,fitness);
    return individ;
}

int Populatie::getIndiceElitist(std::vector<Individ> populatie)
{
    double valoareElitist=-1;
    int indexElitist=-1;
    for (int i=0;i<n;i++)
    {
        if (populatie[i].getFitness()>valoareElitist)
        {
            valoareElitist=populatie[i].getFitness();
            indexElitist=i;
        }
    }
    return indexElitist;

}


/*-------------
 *  CONSTRUCTOR
 *--------------
 */

Populatie::Populatie(
    int dimPopulatie, double intervSt, double intervDr, double coefX2, double coefX1, double coefX0,
    int precizie, double probCrossover, double probMutatie, int nrEtape, std::ostream& fout) : n(dimPopulatie),a(intervSt),b(intervDr),x2(coefX2),x1(coefX1),x0(coefX0),
    precizie(precizie),probC(probCrossover),probM(probMutatie),etape(nrEtape),out(fout)
{
    //numarul de biti necesari
    l=ceil(log2((b-a)*pow(10,precizie)));

    //discretizarea intervalului
    d=(b-a)/(pow(2, l)-1);

    generatie.resize(n);
    for (int i=0;i<n;i++)
    {
        generatie[i]=creazaIndividAleator();
    }
}


/*---------------------
 *  ALGORTIMII EVOLUTIVI
 *---------------------
 */


void Populatie::selectie(bool primaGeneratie)
{

    double fitnessPopulatie=0;
    for (int i=0;i<n;i++)
    {
        fitnessPopulatie+=generatie[i].getFitness();
    }

    std::vector<double> p(n);//probabilitati de selectie in functie de fitness
    for (int i=0;i<n;i++)
    {
        p[i]=generatie[i].getFitness()/fitnessPopulatie;
    }

    std::vector<double> q(n+1,0);//probabilitatile cumulate care dau intervalele de selectie
    for (int i=0;i<n;i++)
    {
        q[i+1]=q[i]+p[i];
    }

    if (primaGeneratie)
    {
        afisarePopulatieInitiala();
        afisareProbabilitati(p,q);
        afisarePerformantaPopulatie(generatie);
    }



    std::vector<Individ> generatieNoua;

    int indexElitist=getIndiceElitist(generatie);
    //elitistul trece automat in generatia urmatoare
    generatieNoua.push_back(generatie[indexElitist]);

    if (primaGeneratie)
    {
        out<<std::endl;
        out<<"=====================PROCESUL DE SELECTIE======================"<<std::endl;
        out<<std::endl;
    }



    for (int i=1;i<n;i++)
    {
        double u=getNumarRandomReal(0,1);

        //cautam intervalul in care se gaseste u
        int indiceInterval=cautareBinara(0,n,u,q);
        if (indiceInterval>=n)
            indiceInterval=n-1;
        if (indiceInterval<0)
            indiceInterval=0;

        if (primaGeneratie)
        {
            out<<"Numar random ales: "<<u<<'\n';
            out<<"["<<q[indiceInterval]<<", "<<q[indiceInterval+1]<<"] individ ales:"<<indiceInterval<<'\n'<<'\n';

        }

        generatieNoua.push_back(generatie[indiceInterval]);
    }
    generatie=generatieNoua;

    if (primaGeneratie)
    {
        out<<"-------------------Noua generatie dupa selectie-------------"<<std::endl;
        afisarePopulatie(generatieNoua);
        afisarePerformantaPopulatie(generatie);

    }




}


void Populatie::crossover(bool primaGeneratie)
{

    if (primaGeneratie) {
        out<<std::endl;
        out<<"===========================PROCESUL DE CROSSOVER========================"<<std::endl;
        out<<std::endl;

    }

    std::vector<Individ> indiviziCrossover;//vector in care adaugam indivii selectati pentru incrucisare
    std::vector<Individ> generatieNoua;


    int indexElitist=getIndiceElitist(generatie);
    //elitistul trece automat in generatia urmatoare
    generatieNoua.push_back(generatie[indexElitist]);


    for (int i=1;i<n;i++)
    {
        double u=getNumarRandomReal(0,1);
        if (u<probC)
            indiviziCrossover.push_back(generatie[i]);
        else generatieNoua.push_back(generatie[i]);
    }

    if (primaGeneratie)
    {
        out<<"Indivizi supusi crossoveru-ului"<<std::endl;
        afisarePopulatie(indiviziCrossover);
        bigBreak(out);
    }


    int m=indiviziCrossover.size();
    int limita=m-(m%2); //daca e impar, ignoram ultimul individ


    for (int i=0;i<limita;i+=2)
    {
        int punctRupere=getNumarRandomIntreg(1,l-1);

        std::string cromozom1, cromozom2;
        cromozom1=indiviziCrossover[i].getCromozomi();
        cromozom2=indiviziCrossover[i+1].getCromozomi();

        std::string incrucisare1, incrucisare2;
        incrucisare1=incrucisareString(cromozom1,cromozom2,punctRupere);
        incrucisare2=incrucisareString(cromozom2,cromozom1,punctRupere);

        Individ copil1=creeazaIndividFromString(incrucisare1);
        Individ copil2=creeazaIndividFromString(incrucisare2);

        generatieNoua.push_back(copil1);
        generatieNoua.push_back(copil2);

        if (primaGeneratie)
        {
            out<<"Punct rupere: "<<punctRupere<<std::endl;

            out<<"Parinte 1:";
            indiviziCrossover[i].afisare(out);
            out<<"Parinte 2:";
            indiviziCrossover[i+1].afisare(out);

            out<<"Copil 1:";
            copil1.afisare(out);
            out<<"Copil 2:";
            copil2.afisare(out);

            out<<"---------------------------------"<<std::endl;
        }

    }
    if (m%2==1)
        generatieNoua.push_back(indiviziCrossover.back());

    generatie=generatieNoua;

    if (primaGeneratie)
    {
        out<<"-------------------Noua generatie dupa crossover-------------"<<std::endl;
        afisarePopulatie(generatie);
        afisarePerformantaPopulatie(generatie);
    }





}

void Populatie::mutatie(bool primaGeneratie)
{

    if (primaGeneratie) {
        out<<std::endl;
        out<<"===========================PROCESUL DE MUTATIE========================"<<std::endl;
        out<<std::endl;

    }


    std::vector <Individ> generatieNoua;

    int indexElitist=getIndiceElitist(generatie);
    //elitistul trece automat in generatia urmatoare
    generatieNoua.push_back(generatie[indexElitist]);

    for (int i=1;i<n;i++)
    {
        std::string mutatie=generatie[i].getCromozomi();
        std::string cromozomiIndivid=generatie[i].getCromozomi();
        bool ok=false;//verificam daca a avut loc o mutatie

        // for (int j=0;j<l;j++)
        // {
        //     double u=getNumarRandomReal(0,1);
        //     if (u<probM)//dam flip la biti
        //     {
        //         if (mutatie[j]=='0')
        //             mutatie[j]='1';
        //         else mutatie[j]='0';
        //
        //         ok=true;
        //     }
        // }


        for (int j=0;j<n;j++) {
            double u=getNumarRandomReal(0,1);
            if (u<probM)
            {
                int val;
                int x=0,y=0,z=0;
                if (j!=0) {
                    x=(int)cromozomiIndivid[j-1];
                }
                y=(int)cromozomiIndivid[j];
                if (j!=n-1) {
                    z=(int)cromozomiIndivid[j+1];
                }
                val = (x+y+z) %2;


                if (val==1) {
                    mutatie[j]='1';
                }
                else mutatie[j]='0';
                ok=true;
            }
        }

        //nu a avut loc nicio mutatie
        if (ok==false)
            generatieNoua.push_back(generatie[i]);
        else
        {
            Individ mutant=creeazaIndividFromString(mutatie);
            generatieNoua.push_back(mutant);
            if (primaGeneratie)
            {
                out<<"Mutant: ";
                mutant.afisare(out);
            }
        }
    }

    generatie=generatieNoua;

    if (primaGeneratie)
    {
        out<<"-------------------Noua generatie dupa mutatie-------------"<<std::endl;
        afisarePopulatie(generatie);
        afisarePerformantaPopulatie(generatie);
    }
}


void Populatie::evolutie()
{
    selectie(true);
    crossover(true);
    mutatie(true);

    for (int i=1;i<etape;i++)
    {
        out<<std::endl;
        out<<std::endl;
        out<<"GENERATIA "<<i+1<<std::endl;
        selectie(false);
        crossover(false);
        mutatie(false);

        afisarePerformantaPopulatie(generatie);
    }


}


