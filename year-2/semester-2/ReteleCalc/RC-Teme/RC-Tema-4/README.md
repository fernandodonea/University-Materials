# RC Tema 4

## Capitolul X8

### Exercițiul 1: Deploy complet și verificare

Reporniți de la zero: creați clusterul, construiți și încărcați imaginea, aplicați toate manifestele în ordine.

1. Creați clusterul `k8s-flask` și încărcați `flask-redis-app:v1`.

    ```bash
    kind create cluster --name k8s-flask

    cd capitolulX8/flask-redis
    docker build -t flask-redis-app:v1 .

    kind load docker-image flask-redis-app:v1 --name k8s-flask

    ```


2. **Cerință:** Aplicați manifestele în ordine numerică (`00-` → `04-`) și verificați cu `kubectl get all -n seminar` că toate resursele sunt create (2 Deployments, 2 Services, 3 Pod-uri Flask + 1 Pod Redis). Cât timp a durat până toate pod-urile Flask au ajuns în starea `1/1 READY`?

    ```bash
    cd ../k8s
    kubectl apply -f 00-namespace.yaml

    kubectl apply -f 01-configmap.yaml
    kubectl apply -f 02-secret.yaml
    kubectl apply -f 03-redis.yaml
    kubectl apply -f 04-flask.yaml

    ```


3. Accesați aplicația în browser și faceți 10 reîmprospătări. Notați câte pod-uri diferite au servit cererile.

    ```bash
    NODE_IP=$(kubectl get nodes -o jsonpath='{.items[0].status.addresses[0].address}')
    echo "Accesați: http://$NODE_IP:30501"

    #sau

    kubectl port-forward service/flask-service 5000:5000 -n seminar
    # Deschideți http://localhost:5000

    ```


>R: Toate cererile au fost servite de un singur pod.


### Exercițiul 2: Modificarea configurației prin ConfigMap

Una dintre valorile ConfigMap-ului este `APP_TITLE` — titlul afișat în pagina web.

1. **Cerință:** Editați `01-configmap.yaml` și schimbați `APP_TITLE` la `"Rețele de Calculatoare 2025 — Laborator K8s"`. Aplicați din nou cu `kubectl apply -f 01-configmap.yaml`.
    ```bash
    kubectl apply -f 01-configmap.yaml
    ```

2. Observați că pagina web **nu s-a schimbat** imediat — pod-urile existente nu sunt repornite automat când un ConfigMap se modifică. **Cerință:** Forțați repornirea pod-urilor Flask fără să modificați YAML-ul Deployment-ului:
    ```bash
    kubectl rollout restart deployment/flask-deployment -n seminar
    ```
3. Accesați din nou pagina și verificați că titlul s-a actualizat.





### Exercițiul 3: Inspecția Secretelor și discuție de securitate

1. Rulați: `kubectl get secret flask-secret -n seminar -o yaml` și copiați valoarea din câmpul `REDIS_PASSWORD`.
    ```bash
    kubectl get secret flask-secret -n seminar -o yaml
    ```
2. **Cerință:** Decodificați valoarea folosind comanda `echo "<valoarea copiată>" | base64 --decode`. Ce parolă vedeți?
    ```bash 
    echo "cGFyb2xhLXJlZGlzLTEyMw==" | base64 --decode
    ```
>**R**:parola-redis-123    

3. Acum intrați într-un pod Flask cu `kubectl exec` și rulați `env | grep REDIS_PASSWORD`. Parola apare în clar?
    ```bash
    kubectl exec -it deployment/flask-deployment -n seminar -- bash

    env | grep REDIS_PASSWORD
    #REDIS_PASSWORD=parola-redis-123
    ```
>**R:** Da, parola apare clar   


4. **Discuție:** Dacă un atacator obține acces la cluster (sau la fișierul `~/.kube/config`), poate citi toate Secretele. Cercetați ce este [Sealed Secrets](https://github.com/bitnami-labs/sealed-secrets) și explicați în 2-3 propoziții cum rezolvă această problemă.

>R: Developerii cripteaza secretele folosind o cheie publica pe propriul pc (creand deci un Sealed Secret) iar acest fisier criptat poate fi stocat direct pe un repo public, neputand fi descifrat. Cand fisierul este aplicat in cluster, doar controller-ul Sealed Secret, care detine cheia privata corespunzatoare, poate sa il decripteze si sa genereze un secret kubernetes standard.





### Exercițiul 4: DNS intern și debugging cu `kubectl exec`

Kubernetes oferă un sistem DNS intern — fiecare Service primește automat un nume DNS rezolvabil din orice Pod.

1. Intrați într-un shell interactiv în unul dintre pod-urile Flask:
    ```bash
    kubectl exec -it deployment/flask-deployment -n seminar -- bash
    ```
2. **Cerință:** Din interiorul containerului, verificați că puteți rezolva DNS-ul intern:
    ```bash
    # Forma scurtă
    curl http://redis-service:6379
    # Forma completă (FQDN)
    curl http://redis-service.seminar.svc.cluster.local:6379
    ```
   Redis va răspunde cu `-ERR wrong number of arguments` — este normal! Înseamnă că conexiunea TCP a reușit.
3. Verificați variabilele de mediu injectate: `env | grep -E "REDIS|APP_TITLE|NODE"`. Identificați care variabile vin din ConfigMap, care din Secret și care din `fieldRef`.

- din ConfigMap vin: `REDIS_HOST`, `REDIS_PORT` si `APP_TITLE` (introduse via envFrom: - configMapRef).
- din Secret vine: `REDIS_PASSWORD` (introdusă via env.valueFrom.secretKeyRef).
- din fieldRef vine: `NODE_NAME` (care obține dinamic numele nodului Kubernetes, via spec.nodeName).

4. **Cerință:** Fără a ieși din container, rulați `curl http://localhost:5000/health/ready`. Ce răspuns primiți? Ce înseamnă?

>**R:** Am primit un json {"redis":"ok","status":"ready"}. Acest json este returnat de ruta /health/ready din flask.py si reprezinta un Readiness probe, adica verifica daca procesul Flask ruleaza. Cu alte cuvinte, aplicatia a reusit conectarea la backend si este gata sa serveasca cereri. 

---

### Exercițiul 5: IP-urile pod-urilor — subnetting, comunicare directă și de ce există Service-urile

În Kubernetes, **fiecare pod primește o adresă IP unică** din blocul de adrese al clusterului (Pod CIDR). Aceasta este o adresă IP reală, rutabilă în interiorul clusterului — nu o adresă virtuală. Există trei categorii distincte de adrese IP în cluster, cu roluri complet diferite.

**Pasul 1:** Listați toate adresele IP din namespace-ul `seminar`:

```bash
# IP-urile pod-urilor (Pod CIDR, ex: 10.244.x.x)
kubectl get pods -o wide -n seminar

# IP-urile Service-urilor (Service CIDR / ClusterIP, ex: 10.96.x.x)
kubectl get services -n seminar

# IP-ul nodului (adresa nodului Docker, ex: 172.18.0.x)
kubectl get nodes -o wide
```

Notați cele trei tipuri de adrese și observați că aparțin unor **subrețele diferite** (uitati-va la al doilea octet, ar trebui sa fie diferit). Completați tabelul:

| Resursă | Adresă IP | Subnet (CIDR) | Tip |
|---|---|---|---|
| Pod `flask-deployment-xxx` | 10.244.0.6 | 10.244.0.0/24 | Pod IP (efemer) |
| Pod `redis-deployment-xxx` | 10.244.0.5 | 10.244.0.0/24 | Pod IP (efemer) |
| Service `redis-service` | 10.96.174.77 | 10.96.0.0/16 | ClusterIP (virtual, stabil) |
| Service `flask-service` | 10.96.174.94 | 10.96.0.0/16 | ClusterIP (virtual, stabil) |
| Node `k8s-flask-control-plane` | 172.22.0.3 | 172.22.0.0/16 | Node IP |


```bash
kubectl get nodes k8s-flask-control-plane -o jsonpath='{.spec.podCIDR}'
```

Eu obtin subnetul: 10.244.0.0/24

Faceti screenshot cu tabelul. 

**Pasul 2:** Lansați un pod de debugging cu `nicolaka/netshoot` — o imagine specializată pentru diagnosticarea rețelei, care conține `ip`, `ping`, `tcpdump`, `curl`, `nslookup` și alte unelte:

```bash
kubectl run netshoot --image=nicolaka/netshoot -it --rm -n seminar --restart=Never -- bash
```

Din interiorul acestui pod, investigați interfețele de rețea și tabela de rutare:

```bash
# Adresa IP a pod-ului curent și interfața de rețea
ip addr show eth0

# Tabela de rutare
ip route

# Observați:
# - adresa IP a pod-ului (din Pod CIDR, ex: 10.244.x.y)
# - gateway-ul implicit (adresa bridge-ului de pe nod, ex: 10.244.x.1)
# - ruta pentru întregul Pod CIDR (ex: 10.244.0.0/16 via 10.244.x.1)
```

> **De ce traficul trece prin gateway chiar și între pod-uri de pe același nod?**
> Fiecare pod este izolat într-un network namespace propriu — practic o "cutie" separată cu propria interfață `eth0`, ca și cum ar fi o mașină distinctă. Pod-urile nu se "văd" direct între ele la nivel de interfață, deci orice pachet care iese din pod urmează singura rută disponibilă: spre gateway-ul de pe nod (un bridge virtual). Nodul preia pachetul și îl livrează la destinație — fie local, fie pe alt nod — aplicând pe drum regulile `iptables` pentru traducerea Service IP → Pod IP. Efectul secundar util este că tot traficul inter-pod trece printr-un singur punct de control. 

**Pasul 3:** Comunicare directă pod-to-pod prin IP, fără Service și fără DNS.

Obțineți IP-ul pod-ului Redis:

```bash
# Rulat din afara containerului (un alt terminal)
REDIS_POD_IP=$(kubectl get pod -l app=redis -n seminar -o jsonpath='{.items[0].status.podIP}')
echo "Redis Pod IP: $REDIS_POD_IP"
```

Din interiorul pod-ului `netshoot`, conectați-vă direct la IP-ul Redis, ocolind complet Service-ul și DNS-ul:

```bash
# Înlocuiți <REDIS_POD_IP> cu valoarea obținută mai sus
curl <REDIS_POD_IP>:6379

# Răspunsul așteptat este una din variantele:
#   curl: (52) Empty reply from server   → conexiune TCP reușită, Redis a închis-o (nu vorbește HTTP)
#   -ERR wrong number of arguments       → Redis a procesat cererea ca o comandă invalidă
# Ambele confirmă că traficul IP direct pod-to-pod funcționează.
# Dacă Redis nu ar fi accesibil, ai primi: "Connection refused" sau timeout.
```

**Pasul 4:** Demonstrarea instabilității IP-urilor de pod.

Forțați repornirea pod-ului Redis — pod-ul va fi șters și recreat, primind un **nou IP**:

```bash
kubectl rollout restart deployment/redis-deployment -n seminar
kubectl get pods -o wide -n seminar -w
# Urmăriți: IP-ul noului pod Redis este diferit față de cel vechi
```

Verificați că Service-ul `redis-service` (ClusterIP) **nu s-a schimbat**:

```bash
kubectl get service redis-service -n seminar
```

**Cerință:** Acesta este motivul pentru care Service-urile există. Scrieți un scurt paragraf care explică: de ce o arhitectură care s-ar baza pe IP-urile directe ale pod-urilor în loc de Service-uri ar fi fragilă în producție?

>**R:** Ip-urile podurilor sunt efemere. Daca un pod pica sau se actualizeaza, Kubernets il recreeaza cu un IP complet nou, deci aplicatia (de exemplu Flask) ar pierde definitv conexiunea cu el. Service-urile rezolva aceasta problema oferind un IP virtual si un nume DNS fix, garantand ca traficul ajunge mereu unde trebuie

---


## Capitolul X9

### Exercițiul 1: Deploy complet și verificarea arhitecturii

Deployați întreaga aplicație de la zero și verificați că toate componentele comunică corect.

1. **Cerință:** Construiți imaginile, creați clusterul, încărcați imaginile, aplicați manifestele în ordine. Verificați cu `kubectl get all -n laborator` că aveți 3 Deployments, 3 Services, 1 PVC și că toate pod-urile sunt `Running` și `1/1 READY`.

    ```bash
    kind create cluster --name k8s-notes

    cd frontend
    docker build -t notes-frontend:v1 .

    cd ../api
    docker build -t notes-api:v1 .

    kind load docker-image notes-frontend:v1 --name k8s-notes
    kind load docker-image notes-api:v1 --name k8s-notes


    cd ../k8s
    kubectl apply -f 00-namespace.yaml
    kubectl apply -f 01-configmap.yaml
    kubectl apply -f 02-secret.yaml
    kubectl apply -f 03-postgres.yaml

    kubectl apply -f 04-api.yaml
    kubectl apply -f 05-frontend.yaml

    kubectl get all -n laborator


    ```


2. Accesați aplicația în browser și adăugați 3 note cu titluri diferite. Reîmprospătați pagina de mai multe ori.
Atasati screenshot.

    ```bash
    kubectl port-forward service/frontend-service 5000:5000 -n laborator
    ```



### Exercițiul 2a: Investigarea Init Container-ului

Init container-ul din `04-api.yaml` implementează un pattern clasic de *dependency waiting*.

1. Scalați PostgreSQL la 0 replici: `kubectl scale deployment/postgres-deployment --replicas=0 -n laborator`
2. Scalați API-ul la 0, apoi înapoi la 2: `kubectl scale deployment/api-deployment --replicas=0 -n laborator && kubectl scale deployment/api-deployment --replicas=2 -n laborator`
3. **Cerință:** Urmăriți cu `kubectl get pods -n laborator -w` tranziția prin stările `Init:0/1` → `PodInitializing` → `Running`. Cât timp a stat pod-ul în starea de Init?
4. Reporniți PostgreSQL (`replicas=1`) și observați că pod-urile API trec automat în `Running`.
Atasati screenshot cu terminalul.


    ```bash
    kubectl scale deployment/postgres-deployment --replicas=0 -n laborator

    kubectl scale deployment/api-deployment --replicas=0 -n laborator && kubectl scale deployment/api-deployment --replicas=2 -n laborator


    kubectl get pods -n laborator -w


    kubectl scale deployment/postgres-deployment --replicas=1 -n laborator

    ```

### Exercițiul 2b: Investigarea Init Container-ului
5. **Discuție:** Ce alternativă la init containers există? Cercetați conceptul de [readiness gates](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate). 
Descrieti ce este si diferentele principale. 

>**R:** Readiness Gates sunt conditii suplimentare definite intr-un pod pentru a evalua daca acesta este cu adevarat pregatit sau nu sa primeasca trafic. 
>
>Init Containers ruleaza si trebuie sa se termine complet inainte ca aplicatia principala sa porneasca. 
>
>Readniess Gates sunt evaluate in timpul rularii containerului principal. Aplicatia principala e deja pornita, dar Kubernetes nu i permite sa primeasca trafic pana cand controllerul extern nu i spune ca condiintile sunt indeplinite.

### Exercițiul 3: Demonstrarea persistenței datelor cu PVC

PersistentVolumeClaim este ceea ce separă o bază de date funcțională de una care pierde datele la orice repornire.

1. Adăugați minimum 5 note prin interfață.
2. **Cerință:** Ștergeți pod-ul PostgreSQL: `kubectl delete pod -l app=postgres -n laborator`. Urmăriți cu `kubectl get pods -n laborator -w` cum Kubernetes recreează pod-ul.
3. Accesați aplicația — notele sunt intacte?
4. **Cerință:** Acum ștergeți **PVC-ul**: `kubectl delete pvc postgres-pvc -n laborator`. Ce se întâmplă cu pod-ul PostgreSQL? (PostgreSQL nu va mai porni fără volum.) Recreați PVC-ul: `kubectl apply -f k8s/03-postgres.yaml`. Sunt notele recuperate?
5. **Discuție:** De ce datele s-au pierdut la ștergerea PVC-ului dar nu la ștergerea pod-ului? Ce este un `ReclaimPolicy` și cum ar ajuta în producție?
Raspundeti la intrebari in text. 

>**R**: Dupa stergerea podurilor, datele sunt intacte. Dupa stergerea pvc-ului, notele nu mai sunt recuperate.
>
>Aplicatia (pod-ul de PostgreSQL) si stocarea sunt complet separate. Pod-ul in sine e ca un fel de pointer care arata catre note. Daca acesta este sters, un alt pod va point catre acelasi volum. Daca sterg PVC-ul, Kubernets crede ca nu mai am nevoie de el si sterge automat si discul fizic din spate (PV-ul) pierzand astfel toate notele.

### Exercițiul 4: Scalarea independentă a microserviciilor

Un avantaj cheie al arhitecturii microservicii este că fiecare componentă se scalează independent.

1. Deschideți un terminal cu `kubectl get pods -n laborator -w` pentru a urmări în timp real.
2. **Cerință:** Scalați **doar frontend-ul** la 5 replici. Câte pod-uri API și PostgreSQL există? (Răspunsul așteptat: numărul rămâne neschimbat — fiecare nivel se scalează independent.)
```bash
kubectl scale deployment/frontend-deployment --replicas=5 -n laborator
```
3. Folosiți `kubectl exec -it <pod-frontend> -n laborator -- bash` și din interiorul containerului, apelați API-ul direct: `curl http://api-service:5001/notes | python3 -m json.tool`. Ce vedeți?
    ```json
    [
        {
            "content": "detalii nota",
            "created_at": "Mon, 25 May 2026 22:13:41 GMT",
            "id": 1,
            "title": "titlu nota"
        }
    ]
    ```
4. **Cerință:** Acum scalați **doar API-ul** la 4 replici și generați trafic din browser (adăugați/ștergeți note rapid).
    ```bash
    kubectl scale deployment/frontend-deployment --replicas=4 -n laborator
    ```
Adaugati screenshot. 

### Exercițiul 5a: HPA în acțiune cu OpenLens

Scalarea automată bazată pe trafic este una dintre cele mai valoroase funcționalități Kubernetes.

1. Asigurați-vă că Metrics Server este instalat și funcționează (`kubectl top pods -n laborator`).

    ```bash
    kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml


    kubectl patch deployment metrics-server -n kube-system \
    --type='json' \
    -p='[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]'


    kubectl rollout status deployment/metrics-server -n kube-system
    ```

2. Aplicați `06-hpa.yaml` și verificați cu `kubectl get hpa -n laborator`.
    ```bash
    kubectl apply -f 06-hpa.yaml
    kubectl get hpa -n laborator
    ```

3. **Cerință:** Deschideți OpenLens → namespace `laborator` → Workloads → HPA (`api-hpa`). Porniți load generator-ul din Pasul 7 al ghidului. Urmăriți în OpenLens cum cresc `Current Replicas` pe măsură ce CPU urcă. Faceți screenshot la HPA-ul cu mai mult de 2 replici.
Atasati screenshot. 

    ```bash
    kubectl top pods -n laborator

    kubectl run load-generator --image=busybox:1.36 -n laborator --rm -it -- /bin/sh -c \
    "while true; do wget -q -O- http://api-service:5001/notes > /dev/null; done"
    ```

### Exercițiul 5b: HPA în acțiune cu OpenLens
4. Opriți load generator-ul. Așteptați 5-10 minute. **Cerință:** Observați HPA-ul scalând **înapoi** la 2 replici (scale-down cooldown). Cât timp a durat?
5. **Discuție:** HPA-ul nu scalează automat PostgreSQL — de ce? Ce soluții există pentru scalarea orizontală a bazelor de date relaționale în Kubernetes? *(Indiciu: cercetați `CockroachDB`, `Vitess`, sau `CloudNativePG`.)*
Descrieti ce este si diferentele principale. 

>**R**:Scale-down a durat cam 5 minute. HPA functioneaza prin crearea de clone identice. API-ul nu salveaza date, deci merge. Totusi, PostgreSQL salveaza date. Daca HPA ar crea 5 clone de Postgres pe acelasi volum, ar incerca sa scrie simultan, iar baza de date s-ar corupe. Exista cateva solutii pentru sclarea bazelor de date.
>
>CockroachDB si Vitess sunt baze de date special facute pentru Kubernetes permit sharding-ul (impartirea datelor) si suporta scrieri simultane din mai multe poduri. 
>
>CloudNativePG creeaza o arhitectura in care doar un pod scrie, iar restul citesc. 
