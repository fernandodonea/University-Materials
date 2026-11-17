//
// Created by Fernando-Emanuel Donea on 08.04.2026.
//

#include "../include/Individ.h"


int Individ:: ct=0;

void Individ::afisare(std::ostream& out) const
{
    out<<"Individ: "<<id<<std::endl;
    out<<cromozomi<<std::endl;
    out<<"Valoare: "<<valoare<<std::endl;
    out<<"Fitness: "<<fitness<<std::endl;
    out<<std::endl;

}
