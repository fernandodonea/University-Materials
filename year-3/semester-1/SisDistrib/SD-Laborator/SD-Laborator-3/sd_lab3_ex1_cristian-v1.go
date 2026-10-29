package main

import (
	"fmt"
	"time"
)

/*
Exercițiu 1 (Algoritmul lui Cristian) Un client cu ceasul decalat comunică cu un server de timp
printr-o rețea cu întârzieri simulate (time.Sleep). Notațiile T1, . . . , T4 sunt cele din Figura 1: T1 și
T4 sunt măsurate cu ceasul clientului, iar T2 și T3 cu cel al serverului.
Toate goroutinele rulează pe aceeași mașină și împart același ceas real, deci decalajul clientului
este simulat printr-un offset explicit. Pe lângă θ, vom folosi și durata round-trip-ului, fără timpul de
procesare al serverului:

δ = (T4− T1)− (T3− T2)


*/

type Clock struct{ offset time.Duration }

func (c *Clock) Now() time.Time { return time.Now().Add(c.offset) }

// TODO : calculeaza decalajul theta si intarzierea delta
func estimate(t1, t2, t3, t4 time.Time) (theta, delta time.Duration) {

	/*
		TEORIE
		theta = cu cat difera timpul clientului fata de timpul real al serverului
				->valoarea pe care trebuie sa o adauge clientului ca sa fie sincronizat
				-> offsetul fata de server

		delta = cat dureaza tot procesul de sincronizare
				-> round tripul mesajelor cum ar veni
	*/

	delta = (t4.Sub(t1)) - (t3.Sub(t2))
	theta = ((t2.Sub(t1)) + (t3.Sub(t4))) / 2
	return theta, delta

}

func simuleaza() {

	server := Clock{offset: 0}

	client := Clock{offset: 5}

	t1 := client.Now()

	//simulam cat dureaza ca mesajul sa ajunga de la client la server aka t1->t2
	time.Sleep(100 * time.Microsecond)

	t2 := server.Now()

	//simulat cat dureaza ca serverul sa proceseze mesaju ig? adica t2->t3
	time.Sleep(100 * time.Microsecond)

	t3 := server.Now()

	//simulam cat dureaza ca mesajul cu ora sa ajunga de la server la client gen t3->t4
	time.Sleep(30 * time.Microsecond)
	t4 := client.Now()

	theta, delta := estimate(t1, t2, t3, t4)

	fmt.Println(theta, delta)
}

func main() {
	simuleaza()

}
