package main

import (
	"fmt"
	"sync"
)

/*
7. Fie un sistem distribuit format din doi roboți identici. Ei sunt porniți de către un observer,
reprezentat de funcția main(). Fiecare robot va parcurge un traseu și va trimite periodic printr-
un canal coordonatele sale 2D către celălalt robot, în timp ce se deplasează. Când un robot
își termină de parcurs traseul, îl va notifica pe celălalt că s-a oprit. Acesta trebuie să citească
toate pozițiile primite până la oprire, iar apoi ambii vor raporta observer-ului că și-au terminat
sarcina. Simulați, folosind un program Go, comportamentul roboților.

*/

type Punct struct {
	x int
	y int
}

func robot(id int, send chan<- Punct, receive <-chan Punct, gata chan<- bool, _wg *sync.WaitGroup) {

	defer _wg.Done()

	//canal pe care il folosim ca sa stim cand am terminat de citit
	seen := make(chan bool)

	//parcugem prin coordonatele primite de la celalat robot
	go func() {
		for coord := range receive {
			fmt.Printf("Robotul %d a primit coordonatele (x=%d, y=%d)\n", id, coord.x, coord.y)
		}
		close(seen) //am terminat de citit de la celalalt robot
	}()

	//traseul parcus de robot
	for i := 0; i <= 4; i++ {
		p := Punct{x: id * i, y: id * i}
		send <- p
	}

	fmt.Printf("Robotul %d s a oprit\n", id)

	//notificam celalat robot ca ne-am oprit
	close(send)

	//asteptam sa citim toate pos de la celalat robot
	<-seen

	gata <- true //trimitem la observer

}

func main() {

	ch1 := make(chan Punct, 5)
	ch2 := make(chan Punct, 5)

	gata := make(chan bool, 2)

	wg := sync.WaitGroup{}
	wg.Add(2)

	go robot(1, ch1, ch2, gata, &wg) //robot1 trimite si robot2 primeste
	go robot(2, ch2, ch1, gata, &wg)

	<-gata
	<-gata

	wg.Wait()
}
