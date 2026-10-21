package main

import "fmt"

/*
3. Scrieți un program Go care stochează în memorie un șir de numere și care afișează un slice cu
numerele pare din acel șir.
*/

func main() {

	var intArr [5]int32 = [5]int32{7, 2, 10, 3, 6}
	sliceNrPare := make([]int32, 0, 5)

	for _, val := range intArr {
		if val%2 == 0 {
			sliceNrPare = append(sliceNrPare, val)
		}
	}
	fmt.Println(sliceNrPare)

}
