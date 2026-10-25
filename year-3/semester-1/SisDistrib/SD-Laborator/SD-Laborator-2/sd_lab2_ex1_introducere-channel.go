package main

import "fmt"

/*
1. Scrieți un program Go care să transfere cu succes un mesaj (de exemplu „salut”) de la o goroutină
(diferită de main()) la goroutina main() prin intermediul unui channel.
*/

func functie_send_channel(ch chan string) {
	ch <- "salut" //bagam in canal
}

func main() {

	var ch = make(chan string)
	go functie_send_channel(ch) //rulam functia ca go routine

	fmt.Println(<-ch) //scoatem din canal

}
