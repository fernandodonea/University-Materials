[[sd_Curs-3.pdf#page=5|Referinta Curs]]
# Explicația algoritmului

**QuickSort** sau **Sortarea rapidă** este o metodă eficientă de sortare a unui tablou, descoperită în 1960 de programatorul britanic **C.A.R. Hoare**. Pentru un set de `n` valori oarecare algoritmul efectuează  comparații, dar în cazul cel mai nefavorabil se efectuează  comparații.

Algoritmul este de tip `divide et imperta`; el sortează o secvență a tabloului (inițial întreg tabloul), astfel:

- se alege un element special al listei, numit **pivot**;
- se ordonează elementele listei, astfel încât toate elementele din stânga pivotului să fie mai mici sau egale cu acesta, și toate elementele din dreapta pivotului să fie mai mari sau egale cu acesta;
- se continuă recursiv cu secvența din stânga pivotului și cu cea din dreapta lui.

## Cod  

```c++
void pivot(int v[], int st, int dr)
{
	int p,q,x;
	p=st;
	q=dr;

	x=v[p];
	while(p<q)
	{
		while(p<q && v[q]>=x)
			q--;
		v[p]=v[q];

		while(p<q && v[p]<=x)
			p++;
		v[q]=v[p];
	}
	v[p]=x;
	return p;
}
```
```c++
void QuickSort(int v[], int st, int dr)
{
	if(st<dr)
	{
		int m=pivot(v,st,dr);
		QuickSort(v,st,m-1);
		QuickSort(v,m+1,dr);
	}
}
```

## Complexitate : 
- O(n log_n) - caz favorabil
- O(n^2) - worst case
## Formular Recurență

```
	T(n)=2*T(n/2)+O(n)  ->   O(nlog_n)
```

Pivotul pe ultima pozitie
```
	T(n)=T(n-1)+O(n)   ->   O(n^2)
```

#### Explicații

`2T(n/2)`-> impartitirea problemei in 2 subprobleme de dimensiune `n/2`

`O(n)`-> asezarea pivotlui
