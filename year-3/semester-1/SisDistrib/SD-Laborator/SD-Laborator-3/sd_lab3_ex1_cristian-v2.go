package main

import (
	"fmt"
	"math/rand"
	"time"
)

/*

1. Un client cu ceasul decalat cere de un server timpul corect printr-o rețea cu întârzieri simulate
cu time.Sleep. Pe lângă θ, vom folosi și durata round-trip-ului, fără timpul de procesare al
serverului: 2p
δ = (T4− T1)− (T3− T2).


(a) Completați funcția estimate folosind Algoritmul lui Cristian. Simulați apoi în main o
cerere și un răspuns folosind funcția measure și verificați dacă offset-ul inițial a scăzut.


(b) Repetați simularea de 10 ori ( cu același offset inițial) și calculați δ și θ minime. Comparați
rezultatele cu cele obținute la punctul a).

*/

// stocheaza deviatia fata de timpul real
type Clock struct{ offset time.Duration }

func (c *Clock) Now() time.Time { return time.Now().Add(c.offset) }

// TODO :
// Calculeaza decalajul theta si round -trip -ul delta
func estimate(t1, t2, t3, t4 time.Time) (theta, delta time.Duration) {

	theta = (t2.Sub(t1) + t3.Sub(t4)) / 2 //decalajul=cu cat difera timpul clientului fata de timpul real al serverului
	delta = t4.Sub(t1) - t3.Sub(t2)       //round tripu=cat dureaza tot procesul de sincronizare
	return theta, delta
}

func measure(c_clock, s_clock *Clock) (theta, delta time.Duration) {

	// Request
	t1 := c_clock.Now()
	time.Sleep(3*time.Millisecond + time.Duration(rand.Intn(10))*time.Millisecond)

	t2 := s_clock.Now()
	// Procesare intre 5 si 20 ms
	time.Sleep(5*time.Millisecond + time.Duration(rand.Intn(20))*time.Millisecond)

	t3 := s_clock.Now()
	// Response
	time.Sleep(3*time.Millisecond + time.Duration(rand.Intn(10))*time.Millisecond)

	t4 := c_clock.Now()

	return estimate(t1, t2, t3, t4)

}

func main() {

	client := Clock{offset: 5 * time.Millisecond}
	server := Clock{offset: 0}

	//ex a
	fmt.Println("ex a)")
	theta, delta := measure(&client, &server)
	fmt.Println("offset initial:", client.offset)
	//ajustam ceasul clientului
	client.offset += theta

	fmt.Println("offeset dupa cristian:", client.offset)
	fmt.Println("theta ", theta)
	fmt.Println("delta: ", delta)

	//ex b

	theta_min, delta_min := theta, delta
	for i := 0; i < 10; i++ {
		t, d := measure(&client, &server)
		if t < theta_min {
			theta_min = t
		}
		if d < delta_min {
			delta_min = d
		}
	}

	fmt.Println()
	fmt.Println("ex b)")
	fmt.Println("thetas: ", theta, theta_min)
	fmt.Println("deltas: ", delta, delta_min)

}
