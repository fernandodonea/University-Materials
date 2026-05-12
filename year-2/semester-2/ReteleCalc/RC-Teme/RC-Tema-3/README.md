# RC Tema 3

### ex 1: Analiza fișierelor și construirea imaginii

Înainte de a deploya orice pe Kubernetes, avem nevoie de imaginea Docker a aplicației.

1. Deschideți fișierul `flask-app/app.py`. Identificați: ce informații returnează aplicația? De unde obține numele Pod-ului și al Node-ului?

R:
Aplicatia returneaza o pagina de HTML.
Numele podului este dat de variabila de mediu HOSTNAME.
Numele nodului este dat de variabila de mediu NODE_NAME.


2. Deschideți `flask-app/Dockerfile`. Ce comandă instalează dependențele Python?

Dependintele sunt date de comanda 
```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```



3. **Cerință:** Construiți imaginea Docker cu tag-ul `my-flask-app:v1`, apoi creați clusterul KinD `k8s-flask` și încărcați imaginea în el. Verificați că imaginea este disponibilă în nod rulând `docker exec -it k8s-flask-control-plane crictl images | grep flask`. Atasati screenshot. 

```bash
docker build -t my-flask-app:v1 .

kind create cluster --name k8s-flask --config kind-config.yaml

kubectl cluster-info --context kind-k8s-flask

kind load docker-image my-flask-app:v1 --name k8s-flask

docker exec -it k8s-flask-control-plane crictl images | grep flask
```




### ex 2: Deployment și inspecția Pod-urilor

Acum că imaginea este în cluster, vom deploya aplicația.

1. Aplicați manifestul `k8s/flask-app.yaml` cu `kubectl apply`.
2. **Cerință:** Așteptați până când ambele Pod-uri sunt în starea `Running`. Alegeți un Pod și rulați `kubectl describe pod <nume-pod>`. Identificați în output: pe ce Node rulează Pod-ul? Ce variabile de mediu sunt configurate?
3. Rulați `kubectl logs <nume-pod>` pentru a vedea output-ul serverului Flask la pornire.
Atasati screenshot

```bash
kubectl apply -f flask-app.yaml

kubectl get pods

kubectl describe pod <nume-pod>
```

### ex 3: Scalarea Deployment-ului

Kubernetes face scalarea trivială.

1. **Cerință:** Scalați Deployment-ul la **3 replici** folosind comanda `kubectl scale`. Verificați că există exact 3 Pod-uri în starea `Running`.
2. Folosind `kubectl port-forward deployment/flask-deployment 5000:5000`, accesați `http://localhost:5000` și reîmprospătați pagina de mai multe ori. Notați numele pod-urilor care apar.
3. **Cerință:** Scalați Deployment-ul înapoi la **2 replici** și observați cu `kubectl get pods -w` cum Kubernetes termină Pod-ul în exces.
Atasati screenshot cu 3 dovada ca replici ruleaza. 

```bash
kubectl scale deployment/flask-deployment --replicas=3

kubectl port-forward deployment/flask-deployment 5000:5000


kubectl get pods -w

kubectl scale deployment/flask-deployment --replicas=2
```



### ex 4: Experimentul de Auto-Vindecare (Self-Healing)

Vom simula un crash al unui container pentru a vedea Kubernetes în acțiune.

1. Obțineți lista curentă de Pod-uri cu `kubectl get pods` și rețineți numele lor.
2. **Cerință:** Ștergeți unul dintre Pod-uri cu `kubectl delete pod <nume-pod>`. Imediat după, rulați `kubectl get pods -w` și observați în timp real cum este creat un Pod de înlocuire.
3. Răspundeți in text: Cât timp aproximativ a durat crearea noului Pod? Ce ar fi necesitat această operațiune manual, fără Kubernetes?

```bash
kubectl get pods

kubectl delete pod <nume-pod>

kubectl get pods -w
```

Raspuns
```txt
Crearea unui nou pod a durat mai putin de 1 secunda. Fara kubernetes ar fi trebuit sa observam ca pod-ul a picat, sa ne logam pe server si sa pornim manual un nou pod cu aceleasi setari.
```

### ex 5: Explorare vizuală cu OpenLens

Uneltele CLI sunt esențiale, dar un dashboard vizual accelerează înțelegerea arhitecturii unui cluster.

1. Instalați **OpenLens** de pe [github.com/MuhammedKalkan/OpenLens/releases](https://github.com/MuhammedKalkan/OpenLens/releases) (sau `brew install --cask openlens` pe macOS).
2. Porniți aplicația. Clusterul `kind-k8s-flask` ar trebui să apară automat în lista de clustere (OpenLens citește `~/.kube/config`). Conectați-vă la el.
3. **Cerință:** Navigați la **Workloads → Pods**. Faceți screenshot: câte Pod-uri sunt afișate? Care este starea fiecăruia? Pe ce Node rulează?
4. Faceți click pe unul dintre Pod-uri și deschideți tab-ul **Logs**. Observați log-urile live ale serverului Flask.
5. **Cerință:** Folosind OpenLens (secțiunea **Workloads → Deployments**), editați Deployment-ul și schimbați `replicas` la `3`. Observați în panoul **Pods** cum apare un Pod nou. 
Atasati screenshot din openlens cand ati scalat la 3. 

### ex 6: Modificarea aplicației și re-deployarea (Rolling Update)

Vom face o schimbare în cod și vom vedea cum se face o actualizare (*rolling update*).

1. Modificați fișierul `flask-app/app.py`: schimbați textul din `<h1>` din `Hello from Kubernetes!` în `Hello from Kubernetes - v2!`.
2. Reconstruiți imaginea cu un tag nou: `docker build -t my-flask-app:v2 .`
3. Încărcați noua imagine în cluster: `kind load docker-image my-flask-app:v2 --name k8s-flask`
4. **Cerință:** Modificați câmpul `image` din `k8s/flask-app.yaml` de la `my-flask-app:v1` la `my-flask-app:v2` și aplicați din nou manifestul cu `kubectl apply -f flask-app.yaml`. Urmăriți cu `kubectl get pods -w` cum Kubernetes face un **rolling update** — înlocuiește Pod-urile vechi cu cele noi, câte unul, fără întreruperea serviciului. Verificați în browser că mesajul s-a schimbat. 
Atasati screenshot la terminal cu modificarile


```bash
docker build -t my-flask-app:v2 .

kind load docker-image my-flask-app:v2 --name k8s-flask

kubectl apply -f flask-app.yaml
```
