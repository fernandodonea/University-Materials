package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"sort"
	"strconv"
	"strings"
	"sync"
)

/*

1. Implementați algoritmul FloodSet s-robust pentru un graf orientat tare conex și defecte de tip
crash. Pentru fiecare nod, Mi(0) = {(i, vi )}, unde vi este token-ul nodului. Listele de adia-
cență pot fi citite de la tastatură folosind un redirect dintr-un fișier (go run flood_sr.go <
input.txt). Puteți folosi atât implementarea de mai jos a funcției de calculare a diametrului
grafului cât și tipurile sugerate. Puteți decide random la fiecare iterație dacă va exista un nod
care va intra în crash, iar în caz afirmativ, puteți decide random și nodul respectiv.
 6p


Formatul inputului:
• linia 1: n (numărul de noduri) și s (numărul maxim de defecte);
• linia 2: n valori pentru token-uri: v0 , v1 , . . . , vn−1 ;
• următoarele n linii: lista de adiacență a nodului i, adică
Formatul outputului: diametrul grafului, iterația la care se oprește algoritmul și memoria
finală a unui nod corect, sub formă de perechi (id, v) sortate după id.


*/

/*
----------
helpere
----------
*/

func citire() (n int, s int, values []int, adj [][]int) {

	// file, err := os.Open("input2.txt")
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

	//citim valorile pentru tokene
	scanner.Scan()
	str = scanner.Text()
	cuv = strings.Split(str, " ")
	for i := range n {
		token, err := strconv.Atoi(cuv[i])
		if err != nil {
			fmt.Println("Eroare la conversie tokenilor")
		}
		values = append(values, token)
	}

	//citim lista de adiacenta
	adj = make([][]int, n)
	for i := range n {

		scanner.Scan()
		str = scanner.Text()
		cuv = strings.Split(str, " ")
		m := len(cuv)

		//adj[i] = make([]int, m)

		for j := range m {
			vecin, err := strconv.Atoi(cuv[j])
			if err != nil {
				fmt.Printf("Eroare la conversia listei de adiacenta a nodului %v\n", i)
			}

			adj[i] = append(adj[i], vecin)

		}
	}

	if scanner.Err() != nil {
		fmt.Println("yey am scapat de warning")
	}

	return n, s, values, adj
}

func diametru(adj [][]int) int {
	n := len(adj)
	diam := 0

	for src := 0; src < n; src++ {
		// BFS din nodul src
		dist := make([]int, n)
		for i := range dist {
			dist[i] = -1
		}

		dist[src] = 0
		queue := []int{src}

		for len(queue) > 0 {
			u := queue[0]
			queue = queue[1:]
			for _, v := range adj[u] {
				if dist[v] == -1 {
					dist[v] = dist[u] + 1
					queue = append(queue, v)
				}
			}
		}

		for _, d := range dist {
			if d == -1 {
				return -1 // avem un nod la care nu putem ajunge din src
			}
			if d > diam {
				diam = d
			}
		}
	}
	return diam
}

func ChanMatrix(n int) [][]chan Memory {

	var chs [][]chan Memory = make([][]chan Memory, n)
	for i := range n {
		chs[i] = make([]chan Memory, n)
		for j := range n {
			chs[i][j] = make(chan Memory, 1) //NU UITA DE BUFFER ALTFEL DEADLOCK
		}
	}
	return chs
}

/*
------------------
memory
-----------------
*/

// Info reprezinta o pereche (id, valoare) retinuta in memoria unui nod.
type Info struct {
	ID    int
	Value int
}

// Memory este o multime de token-uri (reuniunea se face prin inserare).
type Memory map[Info]struct{}

func (mem Memory) add(inf Info) {
	mem[inf] = struct{}{}
}
func (mem Memory) print() {

	var values []Info

	for key := range mem {
		values = append(values, key)
	}

	//sortam valorile din memorie dupa id
	sort.Slice(values, func(i, j int) bool {
		if values[i].ID == values[j].ID {
			return values[i].Value < values[j].Value
		}
		return values[i].ID < values[j].ID

	})

	fmt.Println(values)

}

/*
----------
node
--------
*/

type Node struct {
	ID        int
	Neighbors []int
	M         Memory
	Crashed   bool
}

// functie care trimite memoria unui nod vecinilor
func (nod *Node) send(out []chan Memory) {

	//trimitem memoria catre vecini
	for _, ch := range out {

		//daca nodul este picat inchidem canalele
		if nod.Crashed == true {
			close(ch)
		} else {
			//copie a memoriei pentru CA MAPURILE SUNR REFERINTE FFS
			var memCopy Memory = make(Memory)

			for key := range nod.M {
				memCopy.add(key)
			}

			ch <- memCopy

		}

	}
}

// functie care primeste reuniunea memoriilor primite de la vecini
func (nod *Node) recv(in []chan Memory) Memory {

	//reuniunea multimilor
	var U Memory = make(Memory)

	//iteram prin canalele primite de la vecini
	for _, ch := range in {

		//verificam daca canalul este inchis
		msgMem, ok := <-ch
		if ok != false { //canalul nu este inchis de un nod crashed

			//iteram prin memoria mesajului
			for key := range msgMem {
				U.add(key)
			}
		}

	}

	return U
}

func (nod *Node) transform(in []chan Memory, out []chan Memory, wg *sync.WaitGroup) {

	defer wg.Done()

	//trimitem propria memorie
	nod.send(out)

	//primim memoriile de la vecini
	var U Memory = nod.recv(in)

	//reunim U cu memoria proprie
	for key := range U {
		nod.M[key] = struct{}{}
	}

	//fmt.Println(*nod) //pentru testing
}

func crash(nodes []Node, s, probability int) {

	randomNumber := rand.Intn(100)
	if randomNumber <= probability {

		var healthyNodes []int
		for i, nod := range nodes {
			if nod.Crashed == false {
				healthyNodes = append(healthyNodes, i)
			}
		}

		//putem avea maxim S
		if len(nodes)-len(healthyNodes) < s {

			//selectam o vitctima din cele healthy
			victima := rand.Intn(len(healthyNodes))

			id_victima := healthyNodes[victima]
			nodes[id_victima].Crashed = true
		}

	}
}

func FloodSet_s_robust(n int, s int, values []int, adj [][]int) Memory {

	//cream nodurile
	nodes := make([]Node, n)
	for i := range n {
		mem := make(Memory)
		v := Info{i, values[i]}
		mem[v] = struct{}{}
		nodes[i] = Node{ID: i, Neighbors: adj[i], M: mem, Crashed: false}
	}

	var wg sync.WaitGroup

	for t := 0; t <= (s+1)*diametru(adj); t++ {

		//fmt.Print("\n\n") //pentur testing
		chs := ChanMatrix(n)

		crash(nodes, s, 50)

		//matricea de canale dupa lista de adiacenta
		for i := range adj {

			var in []chan Memory
			var out []chan Memory

			//preluam canalele de iesire din lista de adiacenta a nodului i
			for _, j := range adj[i] {
				out = append(out, chs[i][j])
			}

			//cautam ce noduri k au in lista de adiacenta nodul i
			for k := range len(adj) {
				for _, j := range adj[k] {
					if j == i {
						in = append(in, chs[k][i])
					}
				}
			}

			wg.Add(1)
			go nodes[i].transform(in, out, &wg)

		}

		wg.Wait()

	}
	for i := range n {
		if nodes[i].Crashed == false {
			return nodes[i].M
		}
	}
	return Memory{}

}

func main() {
	n, s, ids, adj := citire()
	// fmt.Println(n, s, ids, adj) //pt testing

	m := FloodSet_s_robust(n, s, ids, adj)
	m.print()
}
