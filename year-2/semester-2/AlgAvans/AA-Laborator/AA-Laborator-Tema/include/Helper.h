//
// Created by Fernando-Emanuel Donea on 08.04.2026.
//

#ifndef AA_LABORATOR_TEMA_HELPER_H
#define AA_LABORATOR_TEMA_HELPER_H

#include <ostream>
#include <string>
#include <vector>
#include <cmath>
#include <random>



std::string fromIntToBinary(int x, int n);

int fromBinaryToInt(std::string s);

double functieGradulDoi(double a, double b, double c, double x);

int cautareBinara(int st, int dr, double x, std::vector<double> v);

double getNumarRandomReal(double a, double b);
int getNumarRandomIntreg(int a, int b);

std::string incrucisareString(std::string s1, std::string s2, int r);

void bigBreak(std::ostream& out);


#endif //AA_LABORATOR_TEMA_HELPER_H
