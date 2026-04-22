//
// Created by Fernando-Emanuel Donea on 08.04.2026.
//

#ifndef AA_LABORATOR_TEMA_INDIVID_H
#define AA_LABORATOR_TEMA_INDIVID_H


#include <ostream>

#include "Helper.h"


class Individ
{
    protected:
        std::string cromozomi;//cromozomii individului
        double valoare;//valoarea din intervalul domeniului de definitie
        double fitness;

        static int ct;
        int id;

        bool crossover=false;

    public:
        //constructori
        Individ()=default;
        Individ(std::string cromozomi, double valoare, double fitness, int index)
            :cromozomi(cromozomi),valoare(valoare),fitness(fitness) {
            ct++;
            id=ct;
        }



        //getteri
        std::string getCromozomi(){return cromozomi;}
        double getFitness(){return fitness;}
        double getValoare(){return valoare;}
        int getId(){return id;}

        //setteri
        void setCromozomi(std::string s){this->cromozomi=s;}
        void setValoare(double v){this->valoare=v;}
        void setFitness(double f){this->fitness=f;}
        void setCrossover(bool c){this->crossover=c;}

        void afisare(std::ostream& out) const;
};


#endif //AA_LABORATOR_TEMA_INDIVID_H