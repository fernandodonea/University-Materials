package main

import (
	"fmt"
	"sync"
)

/*
1. Implementați algoritmul de Flooding pentru un inel unidirecțional.


Algoritm FloodingLCR():
	𝑀𝑖: - int id (token id local)
		- int send_id, recv_id (var auxiliare), inițial id
		- status ∈ {lider, non-lider}, inițial non-lider

Funcție transformare nod i ():
	1. send(send_id, dreapta);
	2. recv(recv_id, stânga);
	3. If (recv_id > id):
		1. send_id := recv_id;
	4. ElseIf (recv_id == id): status = leader;
	5. ElseIf (recv_id < id): send_id := NULL;



*/

type Msg struct {
	Value int
	Done  bool // liderul anunta ca a fost ales
}

func node(id int, in <-chan Msg, out chan<- Msg, isLeader *int, wg *sync.WaitGroup) {
	defer wg.Done()

	out <- Msg{Value: id, Done: false}

	for { //incep iteratiile
		msg := <-in

		if msg.Done == true { //ne oprim daca s-a gasit liderul
			if msg.Value != id {
				out <- msg
			}
			break

		} else {

			if msg.Value > id {
				//valoarea primita este mai mare deci o dam mai departe
				out <- Msg{Value: msg.Value, Done: false}
			} else if msg.Value == id { //este lider
				*isLeader = id
				out <- Msg{Value: id, Done: true}
			} else {
				//trimitem NULL adica nu facem nimic
			}
		}
	}

}

// returneaza id-ul liderului
func RingFlooding(ids []int) int {

	n := len(ids)

	//facem o lista de canale
	chs := make([]chan Msg, n)
	for i := range n {
		chs[i] = make(chan Msg, n)
	}

	isLeader := -1 //cand variabila asta nu e -1 am gasit liderul

	var wg sync.WaitGroup

	//incem sa facem leg intre noduri
	for i := range n {
		wg.Add(1)
		go node(ids[i], chs[i], chs[(i+1)%n], &isLeader, &wg)
	}
	wg.Wait()

	return isLeader

}

func main() {
	var ids []int = []int{7, 4, 9, 2, 5, 33, 10, 1}
	lider := RingFlooding(ids)

	fmt.Println(lider)

}
