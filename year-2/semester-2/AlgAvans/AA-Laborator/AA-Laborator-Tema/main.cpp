#include <fstream>
#include <iostream>

#include "Populatie.h"

int main() {

    std::ifstream fin("data/input.txt");
    std::ofstream fout("data/evolutie.txt");

    if (!fin) {
        std::cout << "Nu pot deschide data/input.txt\n";
        return 1;
    }

    if (!fout) {
        std::cout << "Nu pot deschide data/evolutie.txt\n";
        return 1;
    }

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

    fin.close();
    fout.close();

    return 0;
}
