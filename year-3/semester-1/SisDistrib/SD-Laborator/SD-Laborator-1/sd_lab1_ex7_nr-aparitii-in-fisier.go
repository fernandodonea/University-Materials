package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

/*
7. Scrieți un program Go care citește un slice de string-uri formate numai din litere mici dintr-un
fișier. Programul trebuie să afișeze de câte ori apare fiecare cuvânt în slice-ul de string-uri. (1p)

Exemplu de input: mar para mar strugure banana para mar strugure portocala
*/

func main() {

	file, err := os.Open("aparitii_cuvinte.txt")
	if err != nil {
		fmt.Println(err)
	}

	defer file.Close() //inchidem fisierul

	scanner := bufio.NewScanner(file)

	mymap := make(map[string]uint)

	for scanner.Scan() {
		var str string = scanner.Text()    //citim o linie
		cuvinte := strings.Split(str, " ") //scoatem cuvintele din linie
		for _, cuv := range cuvinte {
			mymap[cuv] += 1
		}
	}

	//afisam map-ul
	for cheie, val := range mymap {
		fmt.Printf("%v:%d \n", cheie, val)
	}

	err = scanner.Err()
	if err != nil {
		fmt.Println("Eroare la citire : ", err)
	}

}
