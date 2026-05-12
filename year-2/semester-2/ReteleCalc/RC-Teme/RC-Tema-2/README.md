# RC Tema 2

### ex 1

Construiti o imagine docker pornind de la o imagine de baza python, la care sa adaugati doar pachetele flask si curl. Cand o construiti numiti-o tema_2. Atasati un screenshot in care sa se vada Dockerfile-ul pe care l-ati folosit. Doar 2 pachete, nu mai multe. 


### ex 2
Faceti un screenshot cu imaginea dupa ce ati listat-o in terminal si i-ati dat push pe hubul vostru.


### ex 3
Creati un fisier docker compose in care sa orchestrati 2 containere. Porniti de la o imagine care sa aiba pachetele necesare ca sa rulam client.py si server.py. Pe primul numiti-l server si pe al doilea numiti-l client. Faceti mount la folderul app din capitolulX4. Puneti-le in aceeasi retea. Apoi intrati in aceste 2 containere, in server porniti server.py si in client porniti client.py. Trimiteti un pachet din client catre server. Rezultatul de la server trebuie sa fie "Primit mesaj: Salut de la <numele vostru> de la <o adresa>". Faceti screenshot. 

```bash
docker compose up -d
```

```bash
docker exec -it server bash

cd app
python3 server.py 
```

```bash
docker exec -it client bash

cd app
python3 client.py server
```

### ex 4
La construirea pachetului, pe stratul UDP, adaugă sport=12345 (sau alt număr la alegere, fix).
Exemplu: UDP(sport=12345, dport=SERVER_PORT). Trimite un pachet. Ce observi (raspuns scurt)?

Raspuns: Clientul nu mai trimite pachete de pe un port aletor, ci ramane mereu cel specificat in sport, indiferent de cate ori rulez scriptul.

### ex 5
Află IP-ul clientului din rețeaua ta. Pune in pachet IP(src="IP-ul aflat", dst=SERVER_IP) + același sport ca la pasul anterior. Trimite un pachet. Apoi schimba IPul din IP(src="" cu unul ales de tine, fictiv. Trimite un pachet. Vedeti ca addr e sursa declarata in pachet, nu neaparat adevarul? Atasati screenshot cu cele 2 requesturi.