[[sd_Curs-4.pdf#page=2|Referinta Curs]]

# Definitie

**Min/Max Heap** = arbore binar plin în care fiecare nod are valoarea mai mica/mare decât toate nodurile din subarborele său

# Declarare

```c++
int H[1001];
int sz;
```
# Reprezentarea în memorie

Un heap se reprezintă în memorie ca un vector în care fiecare nod al arborelui corespunde cu element din vector. Construirea se face altfel:
- pentru fiecare nod `i`, pe poziția `2*i` se afla fiul stâng iar pe poziția `2*i+1` se află fiul drept

[[sd_Curs-4.pdf#page=5|Transformarea din arbore in vector]]
##### Parinte
```c++
int parinte(int pos)
{
	return pos/2;
}
```

##### Fiu stang
```c++
int fiu_stang(int pos)
{
	return 2*i;
}
```

##### Fiu drept
```c++
int fiu_drept(int pos)
{
	return 2*i; 
}
```
# Operații
## Inserție

[[sd_Curs-4.pdf#page=3|Exemplu insertie heap]]

complexitate:**O(logn)**

Pentru a insera o noua valoare în heap:
- mai întâi adăugam valoarea la finalul array-ului
- apoi începem să urcam și să verificăm daca noul nod este mai mic decât parintele său
	- daca nodul este mai mic decât parintele, interschimbăm valorile și urcăm în arbore
	- altfel ne oprim întrucât nodul a fost inserat cu succes
	
```c++
void urcare(int pos)
{
	while(pos>1 && H[pos]<H[parinte(pos)]
	{
		swap(H[pos],H[parinte(pos)]);
		pos=parinte(pos);
	}
}
void inserare(int val)
{
	H[++sz]=x;
	urcare(sz);
}
```

## Aflarea minimului/maximului

complexitate: O(1)

Având in vederea modul în care inserăm valorile în Heap, minimul/maximul se va afla mereu pe prima poziție.
```c++
int minim()
{
	return H[1];
}
```

## Extragerea Rădăcinii

[[sd_Curs-4.pdf#page=3|Exemplu extragere radacina]]

complexitate: **O(log n)**

Pentru a extrage rădăcina:
- interschimbăm radăcina cu ultimul nod (să i spunem  `x`)
- începem să coborâm în arbore
- daca `x` este mai mare decât cel mai mic dintre fiii săi, interschimbăm și continuam coborârea până când:
	- fie `x `devine frunză (nu mai are niciun fiu)
	- fie `x` este mai mic decât ambii fii
	
```c++
void coborare(int pos)
{
	while(true)
	{
		//daca nu are fiu stang -> ultimul nivel -> stop 
		if(fiu_stang(pos)>sz)
			break;

		//nodul poate avea unul sau 2 fii
		//sigur are nod stang
		int next_pos=fiu_stang(pos);

		//selectam cel mai mic fiu
		if(fiu_drept(pos)<=sz && H[fiu_drept(pos)] < H[next_pos])
		{
			next_pos=fiu_drept(pos);
		}

		if(H[pos]>H[next_pos])
		{
			swap(H[pos],H[next_pos]);
			pos=next_pos;
		}
	}
}
```

```c++
void stergereRadacina()
{
	swap(H[1],H[sz]);
	hz--;
	coborare(1)
}
```

# HeapSort

complexitate: **O(n log n)**

## Explicatie algoritm
N inserări intr-un heap și N extrageri
### Cod
```c++
void HeapSort(int v[])
{
	for(int i=1;i<=n;i++)
		inserare(v[i]);

	while(sz>0)
	{
		cout<<minim()<<" ";
		stergeRadacina();
	}
}
```