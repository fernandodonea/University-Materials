package main

import "fmt"

/*
8. Angajații unei firme sunt stocați într-un dicționar map[string]int cu perechi de forma nume-
id_departament. Creați un nou map[int][]string care să stocheze perechi de tipul id_departament-
slice cu numele angajaților din departament. (1p)
Exemplu:
		map[ string ]int{
		"Ana Popescu ": 1,
		" Mihai Ionescu ": 2,
		" Bogdan Radu ": 1,
		" Elena Dumitrescu ": 3,
		" Cristian Vasile ": 2,
		" Ioana Enache ": 1,
		9
		}

Rezultatul va fi:
Departamentul 1: [Ana Popescu, Bogdan Radu, Ioana Enache]
Departamentul 2: [Mihai Ionescu, Cristian Vasile]
Departamentul 3: [Elena Dumitrescu]
*/

func main() {

	departamente := make(map[int][]string)

	angajati := map[string]int{
		"Ana Popescu":      1,
		"Mihai Ionescu":    2,
		"Bogdan Radu":      1,
		"Elena Dumitrescu": 3,
		"Cristian Vasile":  2,
		"Ioana Enache":     1,
	}

	//adaugam angajatii in departamente
	for nume, dep := range angajati {
		departamente[dep] = append(departamente[dep], nume)
	}

	//afisarea departamentelor
	for dep, ang := range departamente {
		fmt.Printf("Departament %v : %v\n", dep, ang)
	}

}
