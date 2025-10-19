[[sd_Curs-5.pdf#page=3|Referinta curs]]

Fie `n` numere care pot lua `k` valori distincte
Sortati cele n numere

complexitate **O(n+k)**

#### Exemplu:

n=11
k=3
```
v:       0 1 1 0 2 1 2 0 1 1 2
```

```
		 0  1  2
fr:		[3][5][3]
```
-> 0 0 0
-> 1 1 1 1 1
-> 2 2 2
```
0 0 0 1 1 1 1 1 2 2 2
```

### cod
```c++
void CountSort(int v[], int n, int k)
{
	int fr[k+1];
	for(int i=1;i<=k;i++)
		fr[i]=0;

	for(int i=1;i<=n;i++)
	{
		int x=v[i];
		fr[x]++;
	}

	for(int i-1;i<=k;i++)
	{
		while(fr[i]!=0)
		{
			cout<<i<<" ";
			fr[i]--;
		}
	}
}
```