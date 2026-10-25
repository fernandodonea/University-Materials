package main

import (
	"fmt"
	"time"
)

/*
4. Scrieți un program Go în care un goroutine să notifice funcția main() atunci când procesarea sa
se sfârșește, fără a folosi un wait group
*/

func procesare(ch chan bool) {
	time.Sleep(100 * time.Millisecond) //simulam un serviciu
	ch <- true                         //s-a terminat procesarea

}

func main() {

	ch := make(chan bool)

	go procesare(ch)

	notificare := <-ch //asteptam un raspuns
	if notificare == true {
		fmt.Println("Procesarea s-a terminat, inapoi in main")
	}

}
