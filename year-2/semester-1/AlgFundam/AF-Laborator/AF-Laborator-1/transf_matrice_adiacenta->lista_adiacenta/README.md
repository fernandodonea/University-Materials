# From adjacency matrix to adjacency list

[basecamp](https://eolymp.com/en/problems/3981)
A simple directed graph is given by its adjacency matrix. Print its representation as adjacency list.

## Input

The first line contains the number n (1≤n≤100) of vertices in the graph. Each of the following n lines contains n integers — the adjacency matrix. It is guaranteed that the graph has no self-loops.

## Output

Print n lines — the adjacency list of the graph. In the i-th line, first print the number of edges going out from vertex i, followed by the numbers of the vertices they point to, in ascending order.


## Examples

Input #1
```
5
0 0 1 0 0
1 0 1 0 0
0 0 0 0 1
1 1 0 0 0
1 1 0 0 0
```
Answer #1
```
1 3
2 1 3
1 5
2 1 2
2 1 2
```