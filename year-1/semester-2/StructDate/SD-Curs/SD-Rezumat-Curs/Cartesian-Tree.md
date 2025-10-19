
# Definiție

**Cartesian-Tree**
	un arbore binar derivat dintr-un array cu următoarele proprietăți:
	- daca array-ul e vid atunci si CT ul e vid
	- daca nu e vid:
		- radăcina stochează indicele minimului din vector
		- fiul stâng este un alt CT ce stocheaza cu subarray-ul din stânga minimului
		- fiul drept este un alt CT ce stocheaza cu subarray-ul din dreapta minimului

[[sd_Curs-7.pdf#page=80|Cartesian-Tree vizualizare]]

# Cartesian-Tree și RMQ

**TEOREMA**
	Fie B_1 și B_2 doua blocuri de lungime `b`
	Atunci B1 = B2 <==> B1 si B2 au acelasi CT

[[sd_Curs-7.pdf#page=97|Teorema CT-RMQ Vizualizare ]]

# Creare CT

complexitate **O(n)** 

##### Stack Based Algorithm
- ținem minte pe stiva nodurile din partea dreapta a arborelui
- ca să inseram un nod
	- pop de pe stiva până când
		- fie stiva e goală
		- fie vârful stivei are o valoarea mai mica decât valoarea curentă
	- setam copilul stâng al noului nod ultima valoare scoasă de pe stivă (sau null daca nu s a scos nimic)
	- setam parintele noului nod sa fie vârful stivei (sau null daca stiva e goală)
	- push la noul nod pe stivă
	
[[sd_Curs-7.pdf#page=124|Creare CT Stack Approach ]]

# CT Numbers

Numărul de CT-uri posibile pentru un array de lungime `b` este maxim 4^b

Astfel, folosind [[#Stack Based Algorithm]] , definim următorul număr binar
- 1 dacă s-a dat push pe stiva
- 0 dacă s-a dat pop de pe stiva

*Obs*
	Se efectuează cel mult `2*b` operatii pe stiva 
[[sd_Curs-7.pdf#page=160|Cartesian Tree Number construire ]]

**Consecință**
	doua blocuri B1 și B2 sunt "egale" daca au același Cartesian Tree Number