package main

import "fmt"

/*
5. Scrieți un program Go care ia elementele unui slice de string-uri și îl modifică astfel încât ele-
mentele să apară în ordine inversă. Nu folosiți un alt slice pentru această operațiune.


Exemplu: slice := []string"Laboratorul", "de", "sisteme", "distribuite".
Rezultatul va fi: ["distribuite" "sisteme" "de" "Laboratorul"]

*/

func main() {

	slice := []string{"Laboratorul", "de", "sisteme", "distribuite"}
	fmt.Println(slice)

	n := len(slice)

	for i := 0; i < n/2; i++ {
		var aux string = slice[i]
		slice[i] = slice[n-i-1]
		slice[n-i-1] = aux
	}

	fmt.Println(slice)

}
