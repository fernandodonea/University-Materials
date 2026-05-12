# RC Tema 1





### ex 1 

Schimbați codul astfel încât serverul http://localhost:8001/ să returneze numele dvs și nr. matricol. 


```bash
docker build -t retele:latest -f Dockerfile .

docker compose up -d


docker cp tema1.py rc-tema-1-rt1-1:/tema1/tema1.py


docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' [ID-CONTAINER-RT1]

```


```bash
docker exec -it [ID-CONTAINER-RT1]

mkdir tema1

python3 tema1.py

```










### ex 1 

Schimbați codul astfel încât serverul http://localhost:8001/ să returneze numele dvs și nr. matricol. 


```bash
curl http://localhost:8001/
```

### ex 2

Faceti un apel cu curl către serverul de flask astfel încât să obțineți un json de tipul:
{"item_id":"5"}


```bash

curl -X POST http://localhost:8001/id  -d '{"value": 10}' -H 'Content-Type: application/json'
```

### ex 3

Faceti un apel cu curl către serverul de flask astfel încât să obtineti un json de tipul: 
{"ip":"ip-containerului unde ruleaza serverul"}

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' [Id-Container]

curl http://localhost:8001/idContainer
```

### ex 4

Construiți un o imagine de docker și dați push în docker registry cu imaginea voastră. Containerul trebuie să ruleze pe portul 8001. 

```bash
docker build -t fernandodonea/rc-tema1:latest .
```

### ex 5

Faceți un endpoint care, pentru un IP de rețea dat și un număr de noduri cerut, returnează un subnet mask minimal care acoperă numărul de noduri. 


Input:
```json
{
"ip":"192.168.1.0",
"noduri": 250
}
```
Output:
```
255.255.255.0
```
sau output prin notația CIDR

```bash
curl -X POST http://localhost:8001/submaskmin -d '{ "ip":"192.168.1.0", "noduri": 250 }' -H 'Content-Type: application/json'
```
