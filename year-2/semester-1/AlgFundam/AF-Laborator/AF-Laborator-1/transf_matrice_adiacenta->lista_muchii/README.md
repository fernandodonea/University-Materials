# From adjacency matrix to the list of edges

[basecamp](https://eolymp.com/en/problems/2471)

A simple undirected graph is given by its adjacency matrix. Output its representation as a list of edges.

## Input

The first line contains the number of vertices n (1≤n≤100). Each of the next n lines contains n elements describing the adjacency matrix.

## Output

Print the list of edges, ordered by the first vertex in each pair describing an edge.


## Examples

Input #1
```
3
0 1 1
1 0 1
1 1 0
```
Answer #1
```
1 2
1 3
2 3
```