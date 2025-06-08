

Fie un vector cu `n` elemente `a` și doi indici `i` și `j` cu i≤j .
Care este cel mai mic element din intervalul `a[i],a[i+1],...a[j-1],a[j]` ?

*Notatie*:
	**RMQ(I,J)**= minimul dintre indicii i si j 
*Denumire*:
	**Range Minimum Query** 

Exista un total de O(n^2) valori posibile pentru RMQ.

*Notație*
	 **`<p,q>`**
	`p` -> timp de preprocesare
	`q`-> timp de query

# Fară procesare

< O(1), O(n)>

Fara procesare, cautare naiva

# Preprocesare totală

 **<O(n^2),O(1)>**

Timp de procesare O(n^2) -> **Programare dinamica**

In loc sa construim toate matricea de querry, vom folosi doar o jumatate de matrice.

- `rmq[i][i]=a[i]`, i=0,n-1
- `rmq[i][j]=min(rmq[i-1][j],rmq[i][j-1])` parcurs in semdiagonale

[[sd_Curs-6.pdf#page=63|Vizualizare procesare PD]]



# Block approach

 Idee: împărțim inputul in `blocuri de dimensiune b`

[[sd_Curs-6.pdf#page=95 | Vizualizare Block approach]]
 
#### Preprocesare
 - O(b) work on O(n / b) blocks to Mnd minima. 
 - Total work: **O(n)**.
#### Querry Time
- O(1) work to find block indices (divide by block size). 
- O(b) work to scan inside i and j's blocks. 
- O(n / b) work looking at block minima between i and j. 
- Total work: **O(b + n / b)**.
#### Valoare optima pt `b`

derivam `b+n/b` -> **b=sqrt(n);**

#### Total: **<O(n),O(sqrt(n))>**

# Sparse table

Pt fiecare index `i`, procesam RMQ de lungime 1, 2, 4, 8, 2^k 
- doar log_n procesari pentru fiecare element

#### Preprocesare:
Programare dinamica: n log n
[[sd_Curs-6.pdf#page=184|Vizualizare sparse table]]

#### Querry Time
To answer RMQA(i, j): 
- Find the largest k such that 2k ≤ j – i + 1.
- The range [i, j] can be formed as the overlap of the ranges [i, i + 2k – 1] and [j – 2k + 1, j].
Total query -> O(1)

#### Total: <O(n log_n),O(1)>


# Hibrid

- spargem array uri in blocuri -> `Sumar RMQ`
- facem rmq pentru a cauta in blocuri singulare

sparse table -> **<O(n log_n),O(1)>**

[[sd_Curs-6.pdf#page=199|Strategie hybrida]]

[[sd_Curs-6.pdf#page=215|hybrid 1]] <O(n),O(log n)>
- bloc de dimensiune `log n`
- sparse table pentru `Sumar RMQ`
- cautare liniara pentru blocuri

[[sd_Curs-6.pdf#page=226|hybrid 2]] <O(n log log n),O(1)>
- bloc de dimensiune `log n`
- sparse table pentru `Sumar RMQ`
- sparse table pentru blocuri
- 
[[sd_Curs-6.pdf#page=236|hybrid 3]] <O(n),O(log log n)>
- sparse table pentru `Sumar rmq`
- hibridul 1 cu <O(n),O(n log n)> pentru blocuri

