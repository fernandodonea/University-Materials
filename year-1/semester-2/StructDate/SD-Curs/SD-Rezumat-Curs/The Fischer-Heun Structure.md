
complexitate **<O(n),O(1)>**

# Idee

- Abordare hibrida cu blocuri de dimensiune `b`
- sparse table ca structura RMQ predominanta
- urmatoarele modificări
		- facem un table de lungime `4^b` ce stocheaza pointeri catre structuri RMQ
			- indexul corespunde [[Cartesian-Tree#CT Numbers|Cartesian Tree Number]]
		- cand procesam un RMQ pentru un anumit bloc, mai întâi cream CT-number-ul (să i spunem `t`)
			- daca exista o structura RMQ pentru `t` o folosim
			- daca nu procesăm un RMQ pentru blocul curent, stochează-o în array și indexează cu T

[[sd_Curs-7.pdf#page=247|Fischer-Heun vizualizare]]
