package main

import "fmt"

/*

5. Scrieți un program Go în care un goroutine(send) trimite un mesaj unui alt goroutine(receive)
printr-un canal. Receive va returna mesajul primit, iar funcția main() îl va afișa pe ecran.

*/

// receive only channel
func receive(ch <-chan string) string {
	return <-ch
}

// send only channel
func send(ch chan<- string) {

	ch <- "Mesaj trimis de sender catre reciver"
}

func main() {

	var ch = make(chan string)

	go send(ch)

	fmt.Println(receive(ch))

}
