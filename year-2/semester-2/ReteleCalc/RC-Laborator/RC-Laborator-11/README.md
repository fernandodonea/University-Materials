

# RC Laborator 11
capitolul X8

```bash
kind delete cluster --name k8s-flask
kind create cluster --name k8s-flask-redis

docker build -t flask-redis-app:v1 .

kind load docker-image flask-redis-app:v1 --name k8s-flask-redis

```


```bash
cd ../k8s
kubectl apply -f 00-namespace.yaml
```

configmapu=explicam cam ce serivicii avem noi si cum se mapeaza el prin cluster

```

```