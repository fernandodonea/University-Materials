package main

import (
	"fmt"
	"math/rand/v2"
	"sync"
)

/*
3. Implementați algoritmul de Flooding de medie pentru vot majoritar.

Algoritm Flooding(Maj, 𝑣):
𝑀𝑒𝑚𝑖: 	- int 𝑥_𝑖 (token) , inițial 𝑣𝑖
		- int d (grad intrare), integer
		- int t, integer, inițial 0

Funcție transformare nod i ():
1. Fie U mulțimea mesajelor v_j=x_j(t) primite la N_i-

2. x_i(t+1)=1/d+1 * (x_i(t)+suma mesajul primite)
3. if (cond oprire):
	1. Return 1/2*(1+sng(x(t)-1/2))
4. else send(x(t+1),N_i+)
5. t=t+1
*/

type Msg struct {
	Value float64
	Done  bool
}

func node3(id float64, in []chan Msg, out []chan Msg, votes chan<- float64, wg *sync.WaitGroup) {

	defer wg.Done()

	//in prima iteratie, nodul isi trimite valoarea vecinilor
	for _, ch := range out {
		ch <- Msg{Value: id, Done: false}
	}

	//facem iteratie de 100 pasi ig? nu stim conditia de oprire lol
	for _ = range 70 {

		var sum float64 = id
		var d uint = 0

		//primim valorile de la vecini si facemm suma
		for _, ch := range in {
			msg := <-ch
			sum += msg.Value
			d++
		}

		next_id := sum / float64(d+1) //calcualm media aritmetica dintre valoarea propriie si valorile de la vecini

		//actualizarea locala -> adik x(t) devine x(t+1)
		id = next_id

		//trimitem noul id la vecini
		for _, ch := range out {
			ch <- Msg{Value: id, Done: false}
		}

	}
	fmt.Println(id)
	votes <- id

}

func VotMajoritar(lista_adiacenta [][]int) int {

	n := len(lista_adiacenta)

	//facem o matrice de canale
	chs := make([][]chan Msg, n)
	for i := range n {
		chs[i] = make([]chan Msg, n)
		for j := range n {
			chs[i][j] = make(chan Msg, n)
		}
	}

	votes := make(chan float64, n)

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

		random_id := rand.Float64()
		wg.Add(1)
		go node3(random_id, in, out, votes, &wg)
	}

	wg.Wait()
	close(votes)

	var sum float64 = 0
	for v := range votes {
		sum += v
	}
	result := sum / float64(n)

	if result > 0.5 {
		return 1
	} else {
		return 0
	}

}

func main() {

	lista_adiacenta := [][]int{
		{5},    //1:[6]
		{0, 4}, //2:[1,5]
		{1, 5}, //3:[2,6]
		{2},    //4:[3]
		{3},    //5:[4]
		{4},    //6:[5]
	}

	fmt.Println("decizia votului majoritar: ", VotMajoritar(lista_adiacenta))

}
