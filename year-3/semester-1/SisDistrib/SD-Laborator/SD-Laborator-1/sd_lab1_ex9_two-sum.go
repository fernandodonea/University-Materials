package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

/*

Scrieți un program Go care stochează în memorie un array cu numere naturale. Programul va
citi de la tastatură un număr s și va afișa în O(n) indicii elementelor care însumate au ca rezultat
s.
Exemplu:

6 15
2 7 11 8 4 9

Rezultatul va fi:
1 3
2 4
*/

func main() {

	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()

	//citim de la tast n si s
	str := strings.Split(scanner.Text(), " ")

	n, err := strconv.Atoi(str[0])
	if err != nil {
		fmt.Print("Eroare la conversie")
	}

	s, err := strconv.Atoi(str[1])
	if err != nil {
		fmt.Print("Eroare la conversie")
	}

	var intArr [6]int
	var mymap map[int]int = make(map[int]int)

	scanner.Scan()
	str = strings.Split(scanner.Text(), " ")

	for i := range n {
		intArr[i], err = strconv.Atoi(str[i])
		if err != nil {
			fmt.Print("Eroare la conversie")
		}
		//adaugam in map cu cheie=nr si valoare=indexu numarului
		mymap[intArr[i]] = i

	}

	for i := range n {
		valoare_cautata := s - intArr[i]
		j, ok := mymap[valoare_cautata]
		if ok {
			fmt.Println(i, j)

			//stergem din map valoarea indexul curent ca sa nu se afiseze
			//de doua ori gen 1 3 si dupa 3 1
			delete(mymap, intArr[i])
		}
	}

}
