package main

import "fmt"

/*
2. Scrieți un program Go care să transfere cu success un mesaj (de exemplu „salut”) de la goroutina
main la alta (diferită de main()) prin intermediul unui channel.
*/

func functie_receive_channel(ch chan string) {
	var s = <-ch
	fmt.Println(s)

}

func main() {

	var ch = make(chan string)
	go functie_receive_channel(ch)

	ch <- "salut"

}
