cel mai ar fi sa fie rulat intr-un container



terminal 1
in container
```bash
docker compose up -d

docker exec -it [ID_CONTAINER]

apt update
apt install nano
```



terminal 2
in exterior
```bash
docker cp tema1.py rc-laborator-4-rt1-1:/tema1/tema1.py

docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 0a7c925cfcac



```