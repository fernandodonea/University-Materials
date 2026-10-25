package main

import (
	"fmt"
	"math/rand"
	"time"
)

/*
6. Fie un sistem distribuit format din doi roboți identici. Ei sunt porniți de către un observer,
reprezentat de funcția main(). Cei doi roboți pornesc în același timp și se întrec în linie dreaptă
până la un finish. Scrieți un program Go în care simulați acest sistem, unde funcția main() va
afișa care robot a ajuns primul la finish. Hint: folosiți select
*/

/*
RandomIntegerwithinRange: To generate the number within the range where max is the upper bound and min is the lower bound.

RandomIntegerwithinRange := rand.Intn(max-min) + min    // range is min to max

*/

func robot(id int, finish chan<- int) {

	randomInt := rand.Intn(10-2) + 2
	time.Sleep(time.Duration(100*randomInt) * time.Microsecond)
	finish <- id

}

func main() {

	ch1 := make(chan int) //facem un canal pentru fiecare robot
	ch2 := make(chan int)

	go robot(1, ch1)
	go robot(2, ch2)

	select { //selectam gorutina care se termina prima
	case msg := <-ch1:
		fmt.Println("A castigat robotul cu id-ul", msg)
	case msg := <-ch2:
		fmt.Println("A castigat robotul cu id-ul", msg)
	}

}
