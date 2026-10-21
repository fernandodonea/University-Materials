package main

import "fmt"

/*
2. Scrieți un program Go care stochează un array în memorie. Programul trebuie să afișeze tabloul
sortat crescător folosind o metodă de sortare la alegere.
*/

func main() {

	var intArr [5]int32 = [5]int32{7, 2, 10, 3, 6}

	fmt.Println(intArr)

	//sortare for i for j basic duuh
	// for i := 0; i < 4; i++ {
	// 	for j := i + 1; j <= 4; j++ {
	// 		if intArr[i] > intArr[j] {
	// 			var aux int32 = intArr[i]
	// 			intArr[i] = intArr[j]
	// 			intArr[j] = aux
	// 		}
	// 	}
	// }

	//bubble sort
	var ok bool = false
	for ok == false {
		ok = true
		for i := range 4 {
			if intArr[i] > intArr[i+1] {
				aux := intArr[i]
				intArr[i] = intArr[i+1]
				intArr[i+1] = aux
				ok = false
			}
		}
	}
	fmt.Println(intArr)
}
