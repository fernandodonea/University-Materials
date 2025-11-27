--conectare ca sys
--definire role
create role C##sgbd_role;


--atribuire privilegii si role-uri noului role
grant connect to C##sgbd_role;
grant resource to C##sgbd_role;
grant create table to C##sgbd_role;
grant create view to C##sgbd_role;
grant create materialized view to C##sgbd_role;
grant create synonym to C##sgbd_role;
grant create procedure to C##sgbd_role;
grant create sequence to C##sgbd_role;
grant create trigger to C##sgbd_role;
grant create type to C##sgbd_role;
grant query rewrite to C##sgbd_role;
grant select_catalog_role to C##sgbd_role;
grant alter session to C##sgbd_role;
grant select any dictionary to C##sgbd_role;
grant create public database link to C##sgbd_role;
grant create public synonym to C##sgbd_role;



DROP USER  C##sgbd_homedb1

--definire utilizator
create user C##sgbd_homedb1 identified by oracle
profile default
default tablespace users
quota unlimited on users
account unlock;
--atribuire role nou definit utilizatorului
grant C##sgbd_role to C##sgbd_homedb1;
--atribuire privilegiu unlimited tablespace utilizatorului
grant unlimited tablespace to C##sgbd_homedb1;

