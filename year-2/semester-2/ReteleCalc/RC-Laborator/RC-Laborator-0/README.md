# RC Laborator 0 - Teorie

## Docker

**Dockerfile**
- blueprint, template pentru sistemul rulat in container
- defineste sistemul de operare, ce tool-uri trebuie instalate si userii



```bash
docker build -t retele:latest -f ./docker/Dockerfile .
```
- `-t retele:latest` tagul imaginii (nume:versiune)
- `-f ./docker/Dockerfile` = calea catre fisierul docker
- `.` contextul in care se executa docker build


**Imagine** = creata in baza fisierelor dockerfile

*docker-compose.yml*
```yml
version: '3.8'

services:
    rt1:
        image: snisioi/retele:2021
        volumes:
            - .:/elocal
        tty: true
        networks:
            - dmz
        sysctls:
          - net.ipv4.icmp_echo_ignore_broadcasts=0
    rt2:
        image: snisioi/retele:2021
        volumes:
            - .:/elocal
        tty: true
        networks:
            - dmz
        sysctls:
          - net.ipv4.icmp_echo_ignore_broadcasts=0
    rt3:
        image: snisioi/retele:2021
        volumes:
            - .:/elocal
        tty: true
        networks:
            - dmz
        sysctls:
          - net.ipv4.icmp_echo_ignore_broadcasts=0
networks:
    dmz: {}
```



rt1, rt2, rt3 = sunt servicille
- ele folosesc volume, adica au persistenta (tin minte ce fisiere cream etc)
- sunt lipite la networkul `dmz`
- networkurile trebuie si ele definte (trebuie instantiate)

```bash
docker compose up -d
```


```bash
docker ps
```
- informatii despre containere


```bash
docker compose down
```
- le descompune, le da remove efectiv (trebuie sa dam din nou compose)

compose = se activeaza engine-ul de compose => au nevoie de ajutorul lui pentru a sti pe ce container sa puna mana efectiv


pentru a evita sa tot dam `docker compose down` putem folosi
```bash
docker kill [id]
```

kill = taie resursele efectiv
stop = incearca sa opreasca frumos

---
fara composer, engine-ul docker poate vedea doar id-ul containterlor
```bash
docker exec -it $CONTAINER_ID bash
```
daca vrem sa folosim numele, folosim compose








# RC Laborator Teorie

## Networking Fundamentals

### Adresa MAC vs Adresa IP

adresa MAC
- legata de componenta fizica
- 6 octeti
- folosit doar in reteaua locala
- nu se schimba (fiecare placa are mac-ul ei)
- este legat de ether 
- ca o "serie de sasiu"


adresa IP
- legata de componenta software (adresa logica)
- 4 octeti
- poate fi atribuita si schimbata oricand
- ca un "numar de inmatriculare"
- folosit pentru a ne muta/ruta intre retele

Internet= o retea de retele locale interconectate


Good practice cand cumperi un router
Router 
- denumesti reteaua
- schimbi parola
- poti schimba si IP-ul 

### Newtork Interface Protocol (Placa de retea)

NIC
- componenta fizica care conecteaza o masina la retea

localhost = 127.0.0.1 
127 = clasa de adrese locala


eth0
- placa de retea Ehernet virtuala - folosita pentru comunicarea cu alte containere si exteriorul


 brd = broadcast -> toate hosturile for prima pachetele trimise la ea

 # Netmask si notatia prefix CIDR

 /n = in masca inseamna cati bytes sunt 1 (cati din ei sunt setati)
 cand setam o masca ramanem cu ce este zero


179.82.0.0./16

255.255.0.0.
255 , 255 (aceste doua calupuri sunt luate)


11111111.11111111.11111111.11111100

 00 ->0 => adresa retelei (pointerul la retea)
 01 ->1 => loopback (ce trimiti in retea se reintoarce)
 10 ->2
 11 ->3



179.111.111.0/16
nu e corect => trebuiau 2 liberi
111 ce cauti in octetul 3

## Maximum Transmission Unit (MTU)
= marimea maxima pe care o putem trimite deodata pe o retea

bytes - Ethernet (eth0) maxim 1500 de bytes pe cablul fizic

bytes - Loopback (Io) 65536 in software

## ip link show - Nivlul Data Link



Adress Resolution Protocol (ARP) -> transforma IP in MAC




# RC Laborator 0 - Exercitii


### Exercițiul 1

Modificați docker compose.yml pentru a adaugă încă o rețea și încă 3 containere atașate la rețeaua respectivă. Modificați definiția container-ului rt1 pentru a face parte din ambele rețele. Exemplu de rețele:
```yml
networks:
    dmz:
        ipam:
            driver: default
            config:
                - subnet: 172.111.111.0/16 
                  gateway: 172.111.111.1
    net:
        ipam:
            driver: default
            config:
                - subnet: 198.13.13.0/16
                  gateway: 198.13.13.1
```                  

Ce se intamplă dacă constrângeți subnet-ul definit pentru a nu putea permite mai mult de 4 ip-uri într-o rețea.

Este corect să definim subrețele cu IP-uri: `172.111.111.0/16` și `198.13.13.0/16`?


#### Rezolvare
```yml
version: '3.8'

services:
    rt1:
        image: snisioi/retele:2021
        volumes:
            - .:/elocal
        tty: true
        networks:
            - dmz
        sysctls:
          - net.ipv4.icmp_echo_ignore_broadcasts=0
          - net.ipv4.icmp_echo_ignore_broadcasts=0
    rt2:
        image: snisioi/retele:2021
        volumes:
            - .:/elocal
        tty: true
        networks:
            - dmz
        sysctls:
          - net.ipv4.icmp_echo_ignore_broadcasts=0
    rt3:
        image: snisioi/retele:2021
        volumes:
            - .:/elocal
        tty: true
        networks:
            - dmz
            - net
        sysctls:
          - net.ipv4.icmp_echo_ignore_broadcasts=0
    rt4:
        image: snisioi/retele:2021
        volumes:
            - .:/elocal
        tty: true
        networks:
            - net
        sysctls:
            - net.ipv4.icmp_echo_ignore_broadcasts=0
    rt5:
        image: snisioi/retele:2021
        volumes:
            - .:/elocal
        tty: true
        networks:
            - net
        sysctls:
            - net.ipv4.icmp_echo_ignore_broadcasts=0
    rt6:
        image: snisioi/retele:2021
        volumes:
            - .:/elocal
        tty: true
        networks:
            - net
        sysctls:
            - net.ipv4.icmp_echo_ignore_broadcasts=0


networks:
    dmz:
        ipam:
            driver: default
            config:
                - subnet: 172.111.0.0/16
                  gateway: 172.111.111.1
    net:
        ipam:
            driver: default
            config:
                - subnet: 198.13.0.0/16
                  gateway: 198.13.13.1
```
