

# Laborator 1

### Liste Simplu Înlănțuite

```c++
struct node
{
	int info;
	node *next;
};
```

**Funcții**
- adăugare nod la final --> complexitate `O(1)`
- adăugare nod la început --> complexitate `O(1)`
- parcurgere -> `O(n)`
- adăgarea unui nod la o anumită poziție --> `O(pos)`
- ștergerea primului nod
- ștergerea ultimului nod
- ștergerea unui nod de pe o anumita poziție

# Laborator 2
### Stivă
```c++
struct node
{
	int info;
	node *next;
};
```
**Funcții**
- push
- pop

**Exerciții**
- Problema Parantezelor


# Laborator 3
### Heap

```c++
int heap[1001];
int sz;
```

**Funcții**
- fiu stâng
- fiu drep
- părinte
- urcare
- inserare
- coborâre
- minim/maxim
- ștergere minim

**Exerciții**
- #2746 [Heap Sort](https://www.pbinfo.ro/probleme/2746/heap-sort)
- #3011 [lastk](https://www.pbinfo.ro/probleme/3011/lastk)
- [Interclasari](https://www.infoarena.ro/monitor?user=fernandodonea)

# Laborator 4

### Arbore binar de căutare

```c++
struct ABC
{
	int info;
	
	ABC* left;
	ABC* right;
};
```
**Functii**
- inserare
- afisare 
- cautare
# Laborator 5

### RMQ
```c++
int v[int(1e5) + 1]; 
int rmq[int(1e5)+1][18]; 
int Log[int(1e5) + 1];
```
nu pica la colocviu ig?

**Exercitii**
- [Range Minimum Query](https://infoarena.ro/problema/rmq)
- #3860 [consecutive1](https://www.pbinfo.ro/probleme/3860/consecutive1)




