//
// Created by Fernando-Emanuel Donea on 08.04.2026.
//

#ifndef AA_LABORATOR_TEMA_POPULATIE_H
#define AA_LABORATOR_TEMA_POPULATIE_H

#include <ostream>
#include <vector>

#include "Individ.h"


class Populatie
{
    private:
        int n;//dimensiunea populatiei
        double a,b; // intervalul [a,b]
        double x2,x1,x0;//coeficientii pentru functia de maximizat
        int precizie;//precizia
        double probC;//probabilitatea de crossover
        double probM;//probabilitatea de mutatie
        int etape;

        int l; //lungimea nr de biti pentru cromozomi
        double d; //descretizarea

        std::ostream& out;
        std::vector <Individ> generatie;

        //functii afisare
        void afisarePopulatieInitiala();
        void afisarePopulatie(std::vector <Individ> populatie);
        void afisareProbabilitati(std::vector<double> p, std::vector<double> q);
        void afisarePerformantaPopulatie(std::vector <Individ> populatie);


        Individ creazaIndividAleator();
        Individ creeazaIndividFromString(std::string s);
        int getIndiceElitist(std::vector <Individ> populatie);

    public:

        //constructor
        Populatie(int dimPopulatie, double intervSt, double intervDr, double coefX2, double coefX1, double coefX0,
            int precizie, double probCrossover, double probMutatie, int nrEtape, std::ostream& fout);

        void selectie(bool primaGeneratie);
        void crossover(bool primaGeneratie);
        void mutatie(bool primaGeneratie);

        void evolutie();

    

};

#endif //AA_LABORATOR_TEMA_POPULATIE_H






