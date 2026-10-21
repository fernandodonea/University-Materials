package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

/*
4. Scrieți un program care stochează în memorie un slice de float32 și citește de la tastatură un
index. Programul trebuie să elimine elementul de la poziția index, păstrând ordinea celorlalte
elemente.
*/

func main() {

	floatSlice := []float32{1.2, 3.14, 67.67, 69.420, -2.3}
	fmt.Println(floatSlice)
	fmt.Print("index:")

	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	var str string = scanner.Text()
	index, err := strconv.Atoi(str)
	if err != nil {
		fmt.Println("Eroare de conversie")
	}

	// ... = operatorul de despachetare
	n := len(floatSlice)
	//apenduim slice-uri [0,index] cu [index+1,n]
	floatSlice = append(floatSlice[0:index], floatSlice[index+1:n]...)
	fmt.Println(floatSlice)

}
