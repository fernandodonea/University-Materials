package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"sync"
)

/*
1. Implementați algoritmul ByzFlood pentru un sistem distribuit sincron cu n noduri și cel mult s
defecte bizantine (n > 4s), reprezentat printr-un graf complet. Pentru fiecare nod i ∈ {0, . . . , n −
1}, starea inițială este xi (0) = vi ∈ {0, 1}. Datele de intrare pot fi citite de la tastatură folosind
un redirect dintr-un fișier (go run byzflood.go < input.txt).
 7p


Formatul inputului:
• linia 1: n (numărul de noduri) și s (numărul maxim de defecte bizantine);
• linia 2: n valori binare pentru stările inițiale: v0 , v1 , . . . , vn−1 ∈ {0, 1}.

Formatul outputului: valoarea finală de consens a nodurilor corecte.


Funcțiile de broadcast malițios:
• În Runda 1 (MaliciousBcastState), în locul difuzării valorii reale xi (t), un nod malițios
transmite către fiecare nod j o valoare binară aleatorie (sau opusă stării sale, 1 − xi (t)).
• În Runda 2 (MaliciousBcastTie), dacă liderul fazei (i == t) este malițios, acesta trimite
valori Tie contradictorii (alese aleatoriu din {0, 1} pentru fiecare destinatar) în locul valorii
M ajority(t).


Exemplu de input:
11 2
0 0 0 0 0 0 0 0 0 0 1
Output:
0

*/

func citire() (n int, s int, values []int) {

	// file, err := os.Open("input.txt")
	// if err != nil {
	// 	fmt.Println("Eroare la deschiderea fisierului")
	// }
	// defer file.Close()
	//scanner := bufio.NewScanner(file)

	scanner := bufio.NewScanner(os.Stdin)

	//citim n si s
	scanner.Scan()
	str := scanner.Text()
	cuv := strings.Split(str, " ")
	n, err := strconv.Atoi(cuv[0])
	if err != nil {
		fmt.Print("Eroare la conversie variabilei n")
	}
	s, err = strconv.Atoi(cuv[1])
	if err != nil {
		fmt.Print("Eroare la conversie variabilei s")
	}

	//citim valorile binare initiale
	values = make([]int, n)
	scanner.Scan()
	str = scanner.Text()
	cuv = strings.Split(str, " ")
	for i := range n {
		v, err := strconv.Atoi(cuv[i])
		if err != nil {
			fmt.Println("eroare la conversie")
		}
		values[i] = v
	}

	if scanner.Err() != nil {
		fmt.Println("yey am scapat de warning")
	}

	return n, s, values
}

func makeNodes(n int, s int, values []int) []Node {

	var nodes []Node = make([]Node, n)
	for i := range n {
		newNode := Node{
			id:          i,
			x:           values[i],
			s:           s,
			n:           n,
			isByzantine: false,
			inbox:       make(chan Message, n)}

		nodes[i] = newNode
	}

	//cream nodurile bizantine
	for i := 0; i < s; {

		randByz := rand.Intn(n)
		//fmt.Println(randByz)

		if nodes[randByz].isByzantine == false {
			nodes[randByz].isByzantine = true
			i++
		}
	}
	return nodes

}

// Message reprezinta un mesaj transmis intre noduri in Runda 1 sau Runda 2.
type Message struct {
	SenderID int
	Round    int // 1 pentru starea curenta , 2 pentru valoarea Tie
	Value    int // 0 sau 1
}

type Node struct {
	id          int
	x           int // starea curenta x_i(t)
	s           int
	n           int  // numarul de noduri din sistem
	isByzantine bool // comportamentul la iteratia curenta
	inbox       chan Message
	maj         int
	mult        int
}

// functie care trimite un mesaj catre celalalte noduri
func (node *Node) send(nodes []Node, mesaj Message) {

	//trimitem vecinilor mesajul nodului
	for i := range node.n {
		if i != node.id {
			nodes[i].inbox <- mesaj
		}
	}
}

// functie care returneaza mesajele primite de la vecini
func (node *Node) recv(m int) []Message {

	var U []Message
	for range m {
		U = append(U, <-node.inbox)
	}
	return U
}

// functie care calculeaza valoarea majoritara din mesajele primite si de frecventa acestuia (mult)
func (node *Node) calculateMajorityMult(U []Message) {

	var onesCt int = node.x
	//calculam de cate ori apare 1 in mesajele de la vecini
	for _, msg := range U {
		if msg.Value == 1 {
			onesCt++
		}
	}

	if onesCt >= (node.n/2 + 1) {
		node.maj = 1
		node.mult = onesCt
	} else {
		node.maj = 0
		node.mult = node.n - onesCt
	}

}

// broadcast state = agregarea voturilor
func (node *Node) BcastState(nodes []Node, wg *sync.WaitGroup) {

	defer wg.Done()

	var msg Message = Message{SenderID: node.id, Round: 1, Value: node.x}

	//daca nodul e malicios, trimitem opusul
	if node.isByzantine == true {
		msg.Value = 1 - node.x
	}

	//nodul isi difuzeaza valoarea curenta
	node.send(nodes, msg)

	//nodul primeste mesajele de la vecini
	var U []Message = node.recv(node.n - 1)

	//calculeaza valoarea majoritara si frecventa sa
	node.calculateMajorityMult(U)

}

// broadcast tie = spargerea simetriei prin king
func (node *Node) BcastTie(nodes []Node, wg *sync.WaitGroup) {
	defer wg.Done()

	var msg Message = Message{SenderID: node.id, Round: 2, Value: node.maj}

	//caz lider malicious
	if node.isByzantine == true {
		for j := range node.n {
			if node.id != j {
				//trimiem o valoarea aleator fiecarui nod
				maliciousValue := rand.Intn(2)
				msg.Value = int(maliciousValue)

				nodes[j].inbox <- msg

			}

		}
	} else {
		node.send(nodes, msg)
	}
}

func ByzFlood(n int, s int, values []int) {

	var nodes []Node = makeNodes(n, s, values)

	var wg sync.WaitGroup

	for t := 0; t < s+2; t++ {

		//prima runda
		for i := range n {

			wg.Add(1)
			go nodes[i].BcastState(nodes, &wg)

		}
		wg.Wait()

		//runda doi
		tie := make([]int, n)

		wg.Add(1)
		//king trimite votul sau majoriar
		go nodes[t].BcastTie(nodes, &wg)
		wg.Wait()

		//nodurile primesc raspunsul de la king
		for i := range n {
			if t == i { //king
				tie[i] = nodes[i].maj
			} else {
				U := nodes[i].recv(1)
				tie[i] = U[0].Value
			}
		}

		//actualizarea starilor
		for i := range n {
			if nodes[i].mult > (n/2 + s) {
				nodes[i].x = nodes[i].maj
			} else {
				nodes[i].x = tie[i]
			}

		}

	}

	consenseValue := 0
	for i := range n {
		if nodes[i].isByzantine == false {
			consenseValue = nodes[i].x
			break
		}
	}
	fmt.Println(consenseValue)

}

func main() {
	n, s, values := citire()
	ByzFlood(n, s, values)

}
