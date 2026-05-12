#include <fstream>
#include <iostream>
#include <string>

#include "Populatie.h"

int main(int argc, char* argv[]) {

    std::string inputFile = "data/input.txt";
    if (argc > 1) {
        inputFile = argv[1];
    }

    std::ifstream fin(inputFile);
    std::ofstream fout("data/evolutie.txt");


    int dimPopulatie;
    float intervalSt, intervalDr;
    float coefX2, coefX1, coefX0;
    int precizie;
    float probCrossover;
    float probMutatie;
    int nrEtape;

    fin>>dimPopulatie;
    fin>>intervalSt>>intervalDr;
    fin>>coefX2>>coefX1>>coefX0;
    fin>>precizie;
    fin>>probCrossover;
    fin>>probMutatie;
    fin>>nrEtape;


    Populatie pop(dimPopulatie, intervalSt, intervalDr, coefX2, coefX1, coefX0, precizie, probCrossover, probMutatie, nrEtape, fout);
    pop.evolutie();


    return 0;
}
