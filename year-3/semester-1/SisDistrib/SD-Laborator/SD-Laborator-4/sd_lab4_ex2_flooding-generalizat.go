package main

import (
	"fmt"
	"sync"
)

/*
2. Implementați algoritmul de Flooding pentru grafuri tare conexe.


Algoritm Flooding_Gen(max()):

𝑀𝑖: - int id (token id)
  - int max_id (var auxiliară), inițial id
  - status ∈ {lider, non-lider}, inițial non-lider
  - int rounds, integer, inițial 0
  - int diam (estimare diametru graf)

Funcție transformare nod i ():
1. 𝑡 := 𝑡+ 1
2. Fie U mulțimea ID-urilor primite de la vecinii de intrare
3. max_id:=max({max_id} ∪ U)
4. If (rounds == diam):
 1. If (max_id == id): status = leader;
 2. Else: status = non-leader;

5. Else: send(max_id, vecini ieșire)
*/

type Msg struct {
	Value int
	Done  bool
}

// nodul primeste de acum o lista de canale
func node2(id int, diam int, in []chan Msg, out []chan Msg, isLeader *int, wg *sync.WaitGroup) {
	defer wg.Done()

	max_id := id

	//in prima iteratie trimitem vecinilor propriul id
	for _, ch := range out {
		ch <- Msg{Value: max_id, Done: false}
	}

	//e garantat ca se afla intr-un numar maxim de iteratii egal cu diametrul
	for rounds := 1; rounds <= diam; rounds++ {

		//aflam maximul de la vecini
		for _, ch := range in {
			msg := <-ch
			if msg.Value > max_id {
				max_id = msg.Value
			}
		}

		if rounds == diam { //ultima iteratie
			if max_id == id {
				*isLeader = id
			}
		} else {
			//trimitem maximul nostru la vecini
			for _, ch := range out {
				ch <- Msg{Value: max_id}
			}
		}
	}

}

// returneaza id-ul liderului
func GeneralFlooding(ids []int, lista_adiacenta [][]int) int {

	//n=diametrul grafului
	n := len(ids)

	//matrice de canale
	chs := make([][]chan Msg, n)
	for i := range n {
		chs[i] = make([]chan Msg, n)
		for j := range n {
			chs[i][j] = make(chan Msg, n)
		}
	}

	//cand variabila asta nu e -1 am gasit liderul
	isLeader := -1

	var wg sync.WaitGroup

	//incem sa facem leg intre noduri
	for i := range n {

		var in []chan Msg
		var out []chan Msg

		//preluam canalele de iesire din lista de adiacenta a nodului i
		for _, j := range lista_adiacenta[i] {
			out = append(out, chs[i][j])
		}

		//cautam ce noduri k au in lista de adiacenta nodul i
		for k := range n {
			for _, j := range lista_adiacenta[k] {
				if j == i {
					in = append(in, chs[k][i])
				}
			}
		}

		wg.Add(1)
		//for some reason nu ma lasa lista de canale send/receive only??????
		go node2(ids[i], n, in, out, &isLeader, &wg)

	}
	wg.Wait()

	return isLeader

}

func main() {
	// 					  0  1  2  3   4  5   6  7   8   9
	var ids []int = []int{9, 2, 6, 14, 4, 3, 17, 8, 22, 19}
	var lista_adiacenta [][]int = [][]int{
		{1, 3}, //9: [2,14]
		{2, 4}, //2:[6,4]
		{3},    //6:[14]
		{4, 6}, //14:[4,17]
		{5, 7}, //4:[3,8]
		{6},    //3:[17]
		{7},    //17:[8]
		{0, 8}, //8[9,22]
		{1, 9}, //22:[2,19]
		{2, 0}, //19:[6,9]

	}
	lider := GeneralFlooding(ids, lista_adiacenta)
	fmt.Println(lider)

}
