package main

import "fmt"

/*
6. Fie un map de tipul string-int care stochează perechi de tipul nume-înălțime. Să se afișeze numele
persoanelor în ordinea descrescătoare a înălțimilor. Dacă două persoane au aceeași înălțime, nu
contează ordinea de afișare. (1p)
Exemplu de input:
		map[ string ]int{
		" Andrei ": 190 ,
		" Maria ": 165 ,
		"Ion": 182 ,
		" Elena ": 172 ,
		" George ": 178 ,
		"Ana": 165 ,
		}
*/

func main() {

	mymap := map[string]int{
		"Andrei ": 190,
		"Maria ":  165,
		"Ion":     182,
		"Elena":   172,
		"George":  178,
		"Ana":     165,
	}

	var nameArr []string

	//bagam cheile din map intr un slice
	for key := range mymap {
		nameArr = append(nameArr, key)
	}
	fmt.Println("Nume nesortate din map: ", nameArr)

	//sortam arrayu in functie de valorile din map
	var ok bool = false
	n := len(nameArr)
	for ok == false {
		ok = true

		for i := range n - 1 {
			name1 := nameArr[i]
			name2 := nameArr[i+1]
			if mymap[name1] < mymap[name2] { //sortam desc dupa inaltimea salvata in map
				var aux string = nameArr[i]
				nameArr[i] = nameArr[i+1]
				nameArr[i+1] = aux

				ok = false
			}
		}
	}
	fmt.Println("Nume sortate dupa inaltime: ", nameArr)
}
