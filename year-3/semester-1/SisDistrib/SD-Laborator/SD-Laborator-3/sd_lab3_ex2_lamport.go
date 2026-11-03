package main

import (
	"fmt"
	"math/rand"
	"sort"
	"sync"
)

/*
2. Trei goroutine își trimit mesaje între ele prin canale. Ele își trimit mesaje conform topologiei inel
P1 → P2 → P3 → P1. Fiecare dintre aceste evenimente este înregistrat folosind ceasuri logice
Lamport. Pornind de la șablonul de mai jos, implementați cele 3 metode ale ceasului și stocați în
main evenimentele ordonate crescător. Puteți folosi sort.Slice cu funcția less. Între evenimente,
contoarele ceasurilor sunt incrementate aleator.

*/

type LamportClock struct{ counter int }

// incrementeaza contorul
func (l *LamportClock) Tick() {
	l.counter += 1
}
func (l *LamportClock) Send() int {
	l.Tick()
	return l.counter
}
func (l *LamportClock) Receive(ts int) {
	if ts > l.counter {
		l.counter = ts
	}
	l.Tick()

}

type Message struct{ sender, ts int }
type Event struct {
	process          int
	internal_counter int
	kind             string // " internal ", " send ", " recv "
}

// TODO : retuneaza true daca a precede b
func less(a, b Event) bool {
	if a.internal_counter < b.internal_counter {
		return true
	} else if a.internal_counter > b.internal_counter {
		return false
	} else {
		if a.process < b.process {
			return true
		} else {
			return false
		}
	}
}

func proces(id int, in <-chan Message, out chan<- Message, chEvents chan<- Event, wg *sync.WaitGroup) {

	clock := LamportClock{counter: 0}

	//incepe procesul
	for i := 0; i < rand.Intn(5)+1; i++ {
		clock.Tick()
		chEvents <- Event{process: id, internal_counter: clock.counter, kind: "internal"}
	}

	//procesu 1 primeste mesaj la final
	if id == 1 {
		//trimitem mesajul catre urmatorul proces
		out <- Message{sender: id, ts: clock.Send()}
		chEvents <- Event{process: id, internal_counter: clock.counter, kind: "send"}

		//face chestii
		for i := 0; i < rand.Intn(5)+1; i++ {
			clock.Tick()
			chEvents <- Event{process: id, internal_counter: clock.counter, kind: "internal"}
		}

		//prim mesajul
		msg := <-in
		clock.Receive(msg.ts)
		chEvents <- Event{process: id, internal_counter: clock.counter, kind: "recv"}

	} else {
		//primim mesajul
		msg := <-in
		clock.Receive(msg.ts)
		chEvents <- Event{process: id, internal_counter: clock.counter, kind: "recv"}

		//procesam mesajul
		for i := 0; i < rand.Intn(5)+1; i++ {
			clock.Tick()
			chEvents <- Event{process: id, internal_counter: clock.counter, kind: "internal"}
		}

		//trimitem mesajul catre urmatorul proces
		out <- Message{sender: id, ts: clock.Send()}
		chEvents <- Event{process: id, internal_counter: clock.counter, kind: "send"}
	}

	defer wg.Done()
}

func main() {

	chp1_p2 := make(chan Message)
	chp2_p3 := make(chan Message)
	chp3_p1 := make(chan Message)

	//facem canal buffered in care adaugam inregistrarile de eventuri
	chEvents := make(chan Event, 100)

	var wg sync.WaitGroup
	wg.Add(3)

	go proces(1, chp3_p1, chp1_p2, chEvents, &wg)
	go proces(2, chp1_p2, chp2_p3, chEvents, &wg)
	go proces(3, chp2_p3, chp3_p1, chEvents, &wg)

	wg.Wait()
	close(chEvents)

	//scoatem eventurile din canal
	var events []Event
	for e := range chEvents {
		events = append(events, e)
	}

	//sortam
	sort.Slice(events, func(i, j int) bool {
		return less(events[i], events[j])
	})

	//afisam
	for _, e := range events {
		fmt.Printf("Proces %d / Timp: %2d / Tip: %s\n", e.process, e.internal_counter, e.kind)
	}
}
