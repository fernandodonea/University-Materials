package main

import "sync"

type Msg struct {
	//tokeni
	v map[int]int
}

func node(id int, token int, diam int, s int, i  in []chan Msg, out []chan Msg, wg *sync.WaitGroup) {
	defer wg.Done()

	var v map[int]int = make(map[int]int)
	v[id] = token

	//prima iteratie in care trimitem mesaje vecinilor
	for _, ch := range out {
		ch <- Msg{v: v}
	}

	
	for t:=0; t<(s+1)*diam; t++ {


	}



}


func FloodSetCrash(lista_adiacenta [][]int, tokens []int, diam int, s int){
	
	n := len(lista_adiacenta)


	//facem o matrice de canale
	chs := make([][]chan Msg, n)
	for i := range n {
		chs[i] = make([]chan Msg, n)
		for j := range n {
			chs[i][j] = make(chan Msg, n)
		}
	}

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

		go node(i, token[i], diam, s, in, out, &wg)
	
	}



}

func main() {

}
