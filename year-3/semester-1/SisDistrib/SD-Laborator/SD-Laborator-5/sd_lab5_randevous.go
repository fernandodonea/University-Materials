package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
	"sync"
)

/*
1. Implementați algoritmul de averaging. Implementarea nu trebuie să aibă o performanță maximă,
luați în considerare un număr de maxim 50 de roboți. Lista inițială de poziții poate fi citită dintr-
un fișier. Pe prima linie se află numărul de roboți, iar pe următoarele perechi de numere float64
care reprezintă coordonatele inițiale ale roboților.

Exemplu de input:
6
0 0
10 0
20 5
20 20
5 15
0 10

*/

type Punct struct {
	x, y float64
}

type Robot struct {
	id  int
	poz Punct
}

func (rob *Robot) LookComputeMove(in []chan Punct, out []chan Punct, wg *sync.WaitGroup) {

	defer wg.Done()

	//LOOK

	//suma coordonatelor vecinolor
	var x_coords, y_coords float64 = rob.poz.x, rob.poz.y
	var n int = len(in)

	//send(pos)
	for _, ch := range out {
		ch <- rob.poz
	}

	//receive(vecini)
	for _, ch := range in {
		msg := <-ch
		x_coords += msg.x
		y_coords += msg.y
	}

	//COMPUTE
	new_pos := Punct{x: x_coords / float64(n+1),
		y: y_coords / float64(n+1)}

	//MOVE
	rob.poz = new_pos
	fmt.Printf("robot %v | new position: %v \n", rob.id, rob.poz)

}

func citire() (n int, robots []Robot) {

	file, err := os.Open("roboti.txt")
	if err != nil {
		fmt.Println("Eroare la deschiderea fisierului")
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	scanner.Scan()
	str := scanner.Text()
	n, err = strconv.Atoi(str)
	if err != nil {
		fmt.Print("Eroare la conversie")
	}

	for i := 0; i < n; i++ {

		scanner.Scan()
		str = scanner.Text()
		coord := strings.Split(str, " ")

		x, err := strconv.ParseFloat(coord[0], 64)
		if err != nil {
			fmt.Print("Eroare la conversie")
		}
		y, err := strconv.ParseFloat(coord[1], 64)
		if err != nil {
			fmt.Print("Eroare la conversie")
		}

		robi := Robot{id: i, poz: Punct{x: x, y: y}}

		robots = append(robots, robi)
	}
	return n, robots
}

// comprimam robotii cu aceeasi pozitie
func unify(robots []Robot) (int, []Robot) {
	var new_robots []Robot

	for i := range len(robots) {
		duplicat := false
		for j := range i {
			if distance(robots[i], robots[j]) < 0.000001 {
				duplicat = true
				break
			}
		}
		if duplicat == false {
			new_robots = append(new_robots, robots[i])
		}
	}
	n := len(new_robots)
	return n, new_robots

}

// distanta euclidiana
func distance(r1, r2 Robot) float64 {
	var x, y float64
	x = math.Pow(r1.poz.x-r2.poz.x, 2)
	y = math.Pow(r1.poz.y-r2.poz.y, 2)
	dist := math.Sqrt(x + y)

	return dist
}

func Randevous(n int, radius float64, robots []Robot) {

	var wg sync.WaitGroup

	//numar maxim de iteratii pentru a evita rularea la infinit in cazul clusterelor izolate
	max_iterations := 15

	for i := 0; i < max_iterations && n != 1; i++ { //trebuie sa refacem graful la fiecare iteratie

		n, robots = unify(robots) //ca sa comprimam robotii cu pozitii identice

		//matrice de canale
		var chs [][]chan Punct = make([][]chan Punct, n)
		for i := range n {
			chs[i] = make([]chan Punct, n)
			for j := range n {
				chs[i][j] = make(chan Punct, 1) //NU UITA DE BUFFER ALTFEL DEADLOCK
			}
		}

		for i := range n {
			var in []chan Punct
			var out []chan Punct

			for j := range n {
				if i != j {
					if distance(robots[i], robots[j]) <= radius {
						in = append(in, chs[i][j])
						out = append(out, chs[j][i])
					}
				}
			}
			wg.Add(1)
			go robots[i].LookComputeMove(in, out, &wg)
		}
		fmt.Println()
		wg.Wait()
	}

}

func main() {

	n, robots := citire()
	radius := float64(15)
	fmt.Println(n, radius, robots)
	Randevous(n, radius, robots)

}
