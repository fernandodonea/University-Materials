package main

//daca nu avem un package "main" nu putem rula, o putem compila tho ca si cum ar fi o librarie

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

//daca importam mai multe chestii punem in paranteze rotunde
//daca nu folosim ceva importat primim eroare

/*
1. Scrieți un program Go care citește un număr natural de la tastatură și verifică dacă este prim
sau nu.
*/

func lab1_ex1() {

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
		fmt.Printf("Numarul %d NU este prim", nr)
	} else if nr == 2 {
		fmt.Printf("Numarul %d este prim", nr)
	} else if nr%2 == 0 {
		fmt.Printf("Numarul %d NU este prim", nr)
	} else {
		for i := 3; i*i <= nr; i++ {
			if nr%i == 0 {
				fmt.Printf("Numarul %d NU este prim", nr)
				return
			}
		}
		fmt.Printf("Numarul %d este prim", nr)

	}

}

/*
2. Scrieți un program Go care stochează un array în memorie. Programul trebuie să afișeze tabloul
sortat crescător folosind o metodă de sortare la alegere.
*/
func lab1_ex2() {

	var intArr [5]int32 = [5]int32{7, 2, 10, 3, 1}

	fmt.Println(intArr)
	//sortare for i for j basic duuh
	for i := 0; i < 4; i++ {
		for j := i + 1; j <= 4; j++ {
			if intArr[i] > intArr[j] {
				var aux int32 = intArr[i]
				intArr[i] = intArr[j]
				intArr[j] = aux
			}
		}
	}
	fmt.Println(intArr)

}

func main() {
	//lab1_ex1()
	lab1_ex2()
}
