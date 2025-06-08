#sd 

#### Sintaxa


```c++
struct node
{
	int info;
	node *node;
}
```

#### Functii  

##### Adăugarea unui nou nod la început
- complexitate **O(1)**
- parametrii functiei de tip `node` au `&` (referinta) deoare modificam lista 

```c++
void adaugaInceput(node* &head, node* &last, int x)
{
	node *p=new node;
	p->info=x;
	p->next=NULL;

	//verificam daca lista este goala
	if(head==NULL)
	{
		head=p;
		last=p;
	}
	else
	{
		p->next=head;
		head=p;
	}
}
```


##### Adăugarea unui nod la final
- complexitate **O(1)**
```c++
void adaugaFinal(node* &head, node* &last, int x)
{
	node* p=new node;
	p->info=x;
	p->next=NULL;

	//verificam ca lista sa nu fie goala
	if(head==NULL)
	{
		head=p;
		last=p;
	}
	else
	{
		last->next=p;
		last=p;
	}
}
```


##### Parcurgere lista
* complexitate **O(n)**

``` c++
//nu avem nevoie de referinta intrucat nu modificam lista
void parcurgere(node *head)
{
	node *p=head;

	while(p->next!=NULL)
	{
		cout<<p->info<<" ";
		p=p->next;
	}
}
```


##### Adăugare unei nod la o anumită poziție
- complexitate **O(pos)**

```c++
void adaugaPos(node* &head, int pos, int x)
{
	node* p=new node;
	p->info=val;
	p->next=NULL;

	//presupunem ca pos este un numar diferit de 1 si de n

	//nod temporar pentru parcurgere
	node* t=head;
	for(int i=1;i<pos;i++)
	{
		t=t->next;
	}

	//linkuim nodul p la lista
	p->next=t->next;
	t->next=p;
}
```

Reprezentare grafica

```
							p->next=t->next;

[  ]->[  ]->....    ->[  ]->[ t ]->[  ]->....
                                     ^
                                    /
                                [ p ]  
```

```
							t->next=p;
							
[  ]->[  ]->....    ->[  ]->[ t ]      [  ]->....
                               \        ^
                                \      /
                                 -> [ p ]  
 
```


##### Ștergere primului nod
complexitate **O(1)**

```c++
void stergeFinal(node* &head)
{
	node *p=head;
	
	head=head->next;
	delete p;
}
```


##### Ștergerea ultimului nod
complexitate **O(n)**

```c++
void stergeFinal(node* &head, node* &last)
{
	node *p=head;

	//parcurgem pana la penultimul element
	while(p->next->next!=NULL)
	{
		p=p->next;
	}

	//eliminam zona de memorie
	node *t=p->next;
	delete t;

	last=p;
}
```



##### Stergerea unui element de pe o anumită poziție
complexitate **O(pos)**

```c++
void stergePos(node* &head, int pos)
{
	node* p=head;

	//parcurgem lista pana la pos-1
	for(int i=2;i<=pos-1;i++)
	{
		p=p->next;
	}

	node *q=p->next->next;

	//stergem nodul de pe pozitia p
	node* t=p->next;
	delete t;

	p->next=q;
}
```