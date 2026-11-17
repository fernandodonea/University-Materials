```bash
kind create cluster --name k8s-flask --config kind-config.yaml



kubectl cluster-info --context kind-k8s-flask


kubectl get nodes


kind load docker-image my-flask-app:v1 --name k8s-flask

kubectl apply -f flask-app.yaml

kubectl get pods
```


terminal cu poduri in watch
```bash
kubectl get pods -w
```


```bash
kubectl describe pod flask-deployment-69d6dc56d9-gxlqn


kubectl port-forward deployment/flask-deployment 5000:5000

kubectl scale deployment/flask-deployment --replicas=4
```