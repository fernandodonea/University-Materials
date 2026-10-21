package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

/*
1. Scrieți un program Go care citește un număr natural de la tastatură și verifică dacă este prim
sau nu.
*/

func main() {
	//citim de la tastatura
	scanner := bufio.NewScanner(os.Stdin)

	err := scanner.Err()
	if err != nil {
		fmt.Println(" Eroare la citire : ", err)
	}

	//Facem citirea
	//functia scanner.Scan() returneaza un bool
	scanner.Scan()

	// Conversia in string la ce am citit mai sus cu Scan
	v := scanner.Text()
	nr, err := strconv.Atoi(v)

	if err != nil {
		fmt.Print("Eroare la conversie")
	}

	if nr < 1 {
		fmt.Printf("Numarul %d NU este prim\n", nr)
	} else if nr == 2 {
		fmt.Printf("Numarul %d este prim\n", nr)
	} else if nr%2 == 0 {
		fmt.Printf("Numarul %d NU este prim\n", nr)
	} else {
		for i := 3; i*i <= nr; i++ {
			if nr%i == 0 {
				fmt.Printf("Numarul %d NU este prim\n", nr)
				return
			}
		}
		fmt.Printf("Numarul %d este prim\n", nr)

	}

}
