# Gid instalare Oracle Database MacOS

1. Instalare Docker Desktop 
Descarcă și instalează Docker:
👉 https://www.docker.com/products/docker-desktop
După instalare, verifică în terminal:
```bash
docker --version
```
2. Construirea imaginii Oracle Database 19c
Oracle nu oferă direct imaginea, trebuie construită.
Clonam repository-ul oficial Oracle:
```bash
git clone https://github.com/oracle/docker-images.git
cd docker-images/OracleDatabase/SingleInstance/dockerfiles
```
3. Descarcăm kitul oficial pentru Linux:
De la: https://www.oracle.com/database/technologies/oracle19c-linux-downloads.html
Fisierul: ```LINUX.X64_193000_db_home.zip
Pune-l în folderul 19.3.0```

4. Construim imaginea:
```bash
./buildContainerImage.sh -v 19.3.0 -e
```

5. Crearea containerului HOMEDB1
```bash
docker run -d --name homedb1 \
  -p 1521:1521 -p 5500:5500 \
  -e ORACLE_SID=HOMEDB1 \
  -e ORACLE_PDB=HOMEDB1PDB \
  -e ORACLE_PWD=Admin#DB1 \
  oracle/database:19.3.0-ee
```
`ORACLE_SID=HOMEDB1` = numele bazei principale
`ORACLE_PDB=HOMEDB1PDB` = pluggable DB (echivalent cubaza accesată de aplicații)
`ORACLE_PWD=Admin#DB1` = parolă identică cu tutorialul Windows

6. Verificare pornire
Monitorizam logurile:
```bash
docker logs -f homedb1
```
Așteaptăm mesajul:
```
DATABASE IS READY TO USE!
```
7. Conectare ca Administrator (SYS/SYSTEM)
Variante:
1️⃣ SQL*Plus în container:
```bash
docker exec -it homedb1 sqlplus sys/Admin#DB1@HOMEDB1 as sysdba
```
Din DataGrip sau SQL Developer:

Apasăm `Test Connection` -> trebuie să fie Success 

8.  Creare utilizator comun 
După conectare ca SYS:
```sql
CREATE ROLE sgbd_role;

GRANT CONNECT, RESOURCE, CREATE TABLE, CREATE VIEW, CREATE SYNONYM,
      CREATE PROCEDURE, CREATE SEQUENCE, CREATE TRIGGER, CREATE TYPE,
      QUERY REWRITE, SELECT_CATALOG_ROLE, ALTER SESSION, SELECT ANY DICTIONARY,
      CREATE PUBLIC DATABASE LINK, CREATE PUBLIC SYNONYM TO sgbd_role;
```
```sql
CREATE USER sgbd_homedb1 IDENTIFIED BY oracle
  PROFILE DEFAULT
  DEFAULT TABLESPACE users
  QUOTA UNLIMITED ON users
  ACCOUNT UNLOCK;
```
```sql
GRANT sgbd_role TO sgbd_homedb1;
GRANT UNLIMITED TABLESPACE TO sgbd_homedb1;
```
