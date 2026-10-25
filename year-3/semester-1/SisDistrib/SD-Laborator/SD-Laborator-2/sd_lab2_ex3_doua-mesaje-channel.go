package main

import "fmt"

/*
3. Scrieți un program Go în care funcția main() primește două mesaje pe același canal de comuni-
care.
*/

func doua_mesaje(ch chan string) {
	ch <- "buna"
	ch <- "hello"

}

func main() {

	ch := make(chan string)

	go doua_mesaje(ch)

	mesaj1 := <-ch
	mesaj2 := <-ch

	fmt.Println(mesaj1, mesaj2)

}
