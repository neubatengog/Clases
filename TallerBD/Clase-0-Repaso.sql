-- Clase 0 repaso de comandos ORACLE:
-----------------------------------

--------------SQLPLUS---------------------------
--Conexion:
--sqlplus usuario/password@servicio
------------------------------------------------
--Definir un editor
define _editor='mate w'
define _editor = "C:\ruta al editor\TextPad.exe"

--Login.sql comandos que se ejecutan en sqlplus (configuracion)
spool nombrefichero--Manda el buffer a u fichero que se define manda el resultado aun fichero
spool off--cierra el fichero
edit nombrefichero --Edita el fichero
start fichero --Ejecutar un fichero si no tine extension sql se indica 
@fichero--Ejecutar un fichero
clear buffer --Limpiar el buffer
list buffer --listar el buffer
list last --lista la ultima linea
list n --lista la n enesima linea

save --graba el fichero con opcion replace sobreescribe el fichero

connect --para conextarse con otro usuario
host --para ejecutar un comando en le sistema operativo
prompt --escribe un mensaje en pantalla
accept --pide un valor y lo almacena en una variable que se indique
pause --Para la ejecucion hasta que se da enter

--Ejemplo de prompt
prompt Bienvenido a mi susper fecha 1.0
pause
accept fecha prompt 
select sysdate from dual;
--fin ejemplo


--Definir variables de usuario
define tabla=dual
select 4*6 from &tabla;

--Exit al salir se cierra el fichero
exit


---Trabajando con sql PLUS

create table departamentos(
    cod_departamento number(3),
    nombre_departamento varchar2(20) not null,
    ubicacion varchar2(10),
    constraint dep_pk primary key(cod_departamento), ---Primary key
    constraint dep_ubi check (ubicacion in ('Curico','Talca', 'Santiago')) --Restriccion
)
--l6 lista la linea 6
--i añade a la linea en el buffer despues de la linea activa


--a añade a la linea activa
--del borra la linea
--c/texto1/texto2 modifica  la linea activa

--r ejecuta una vez modificado el buffer

---USO de SPOOL
spool nombreFichero.sql
spool on
spool off
spool --Muestra e fichero actual donde se guarda 


create table empleados(
  cod_empleado number(3),
  nombre varchar2(25),
  profesion varchar2(11),
  idJefe number(6),
  salario number(10),
  comision number(10),
  cod_departamento number(3),
  constraint emp_pk primary key (cod_empleado),
 constraint emp_chk check (salari0),
 constraint emp_fk foreign key(cod_departamento) references departamentos(cod_departamento)
 );






--Mostrar usuarios
select username from all_users;

SELECT TABLE_NAME FROM USER_TABLES;
select table_name from tabs;


--Mostrar todas la tablas del usuario actual
select * from user_tables;
-- siq ueremos ver la tabals de otro usuario se realiza sobre all_tables (vista)
select * from all_tables where owner = "HR"

--Alter modificando 
alter table empleados add(fecha_nacimiento date not null);

--Insercion de datos
insert into departamentos values(10,'Informatica','Curico');
insert into departamentos values(20,'Administracion','Talca');
insert into departamentos values(30,'Ventas','Santiago');  
 
--Ver constrains del usuario 
select constraint_name, constraint_type, search_condition from user_constraints where table_name='DEPARTAMENTOS'
    
insert into empleados values(001,'Garcia Juan','Electrico',001,2600000,null,10,'22-OCT-81'); 
insert into empleados values(002,'Nuñez Sergio','Ventas',001,160000,10,10,'12-SEP-81');
insert into empleados values(005,'Gonzales Sandra','Ventas',001,660000,10,10,'16-MAY-83');
--Modificar una columna
alter table empleados modify (nombre varchar2(30) not null);

--alias las columnas
select nombre_departamento "DEPARTAMENTO", ubicacion "En la ciudad" from departamentos;

--Operadoresd e comparacion
select * from empleados where cod_departamento = 10;
select * from empleados where cod_departamento !=10;
select * from empleados where cod_departamento in (10,20);
select * from empleados where cod_departamento not in (10);
select * from empleados where cod_departamento between 1 and 10;
select * from empleados where nombre like '_o%';

--Operaciones
select nombre, salario+comision from empleados;
select nombre, sysdate-fecha_nacimiento from empleados;
select nombre || ' trabaja en el departamento ' || profesion from empleados;

--Funciones basicas
---Aritmeticas
select abs(-15) from dual;
select ceil(15.7) from dual; --entero superior
select floor(15.7) from dual;
select mod(11,4) from dual;
select power(3,2) from dual;
select round(123.456,1) from dual;
select sqrt(4) from dual;
select trunc(123.456,1) from dual; --trunca a n decimales (puede ser negativo)
select sign(-12) from dual; --Calcula el signo

--Cadenas caracteres
select chr(65) from dual;
select ascii('A') from dual;
select concat(concat(nombre,' es '),profesion) from empleados;
select lower('MinUsCulAs') from dual;
select upper('maYuSCulAs') from dual;
select initcap('isabel') from dual;
select lpad('P',5,'*') from dual;
select rpad('P',5,'*') from dual;
select replace('digo','i','ie') from dual;
select substr('ABCDEFG',3,2) from dual;
select length('cadena') from dual;



--Fechas

select sysdate from dual;
select last_day('17-mar-10') from dual;
select add_months('21-04-04',2) from dual;
select months_between('17-MAR-61','21-MAR-62') from dual;
select next_day('01-FEB-04','MONDAY') from dual;
--

--Funciones (maximo,minimo,promedio,count)
select avg(valor)  from ventas;
select avg(valor) from ventas;
select min(valor) from ventas;
select max(valor) from ventas;
select count(*)from ventas; ---incluye valores nulos
select count(valor) from ventas; ---no incluye valores nulos

-- NVL(exprs1, expr2) 
select nvl(valor, 0) from ventas;--si valor es nulo aparecera un 0
--NVL2(expr1,expr2,expr3)
select nvl(valor, "No hay valor", "Hay un valor en la columna ") from ventas;--si valor es nulo aparecera un 0
select nvl2(valor, 'No hay valor' , 'Hay un valor en la columna') from ventas;--evalua los dos casos

--Decode
select valor, decode(idvendedor ,1,'Vendedor1',2,'Vendedor2') from ventas;

--order by
select apellidos,nombre from vendedores order by apellidos,nombre;
select apellidos,nombre from vendedores order by 1,2;

--select group by
select valor from ventas group by valor;

--distinct
select distinct nombre from vendedores;

--select (in,not in)
select valor from ventas where valor not in( 70,80,30);
select valor from ventas where valor in( 70,80);

--between
select valor from ventas where valor between 10 and 80;
select valor from ventas where valor not between 10 and 80;

--like
select nombre from vendedores where nombre like '%a%';
select nombre from vendedores where nombre like '_u%';





--Subselects con group by,insercion,having
select valor from ventas where valor >= ( select avg(valor)  from ventas);
select valor from ventas having valor >= ( select avg(valor)  from ventas) group by valor;
select valor from ventas  where valor >=(select min (valor) from ventas);
select valor from ventas having valor >= ( select avg(valor)  from ventas) group by valor;
select valor from ventas  where valor<=(select avg(valor) from ventas);
select valor  from ventas having valor >= ( select avg(valor)  from ventas) group by valor;
select valor from ventas  where valor >=(select min (valor) from ventas) and valor<=(select avg(valor) from ventas);

insert into ventas (id,valor,idvendedor) values (s_ventas.nextval,(select avg(valor) from ventas),1);


--Inner join, left join, cross join
--************************
-- Relaciones combinatoria
select ventas.valor , vendedores.nombre from ventas,vendedores;

--union (all)
select valor from ventas UNION all select idvendedor from vendedores;
select valor from ventas UNION  select idvendedor from vendedores;

---where combinacion interna WHERE
select 
      v.nombre,v.apellidos,vt.valor 
from 
      vendedores v,ventas vt
where 
      vt.idvendedor=v.idvendedor 
order by 
      v.nombre;



--inner join , left join ,right join,cross join
select 
      vendedores.nombre,vendedores.apellidos,ventas.valor 
from 
      vendedores 
inner join  Ventas on ventas.idvendedor=vendedores.idvendedor 
order by 
      vendedores.nombre;

--left
select 
      vendedores.nombre,vendedores.apellidos,ventas.valor 
from 
      vendedores 
left join  Ventas on ventas.idvendedor=vendedores.idvendedor  and vendedores.nombre= 'Juan'
order by 
      vendedores.nombre;

--right
select 
      vendedores.nombre,vendedores.apellidos,ventas.valor 
from 
      vendedores 
right join  Ventas on ventas.idvendedor=vendedores.idvendedor  and vendedores.nombre= 'Juan'
order by 
      vendedores.nombre;

--full
select 
      vendedores.nombre,vendedores.apellidos,ventas.valor 
from 
      vendedores 
full  join  Ventas on ventas.idvendedor=vendedores.idvendedor 
order by 
      vendedores.nombre;      

select * from ventas;
select * from vendedores;

--natural join
select 
      vendedores.nombre,vendedores.apellidos,ventas.valor 
from 
      vendedores 
natural join  Ventas;


select 
      v.nombre,v.apellidos,vt.valor 
from 
      vendedores v,ventas vt
where 
      vt.idvendedor=v.idvendedor 
order by 
      v.nombre;


--cross join (producto cartesiano)
select 
      vendedores.nombre,vendedores.apellidos,ventas.valor 
from 
      vendedores 
cross join  Ventas;

--Valores nulos is null / is not null
select * from ventas where valor is null;

--Vaciar una tabla
--No es posible recuperar los registros a diferencia con delete
truncate table ventas;



--***********************************************************************
--Vista : tabla virtual que representa el resultado de cierta consulta.
--formato
-- 
-- 


create view vista_vendedores as
    select 
        nombre || ' '  || apellidos AS VENDEDOR 
    from 
        vendedores;
        
--Trabajando sobre la vista como si fuera una tabla
--No se pueden crear vista si no existen las tablas referenciadas
--Una vista siempre esta actualizada.
select count(vendedor) from vista_vendedores;

--Borrando vista
drop view vista_vendedores;

--Creando cabecera de los campos (vendedores)
-- y que sea solo lectura
create view vista_vendedores (Vendedores) as
  select nombre || ' '  || apellidos  from vendedores 
 with read only;
  
 --Ver las vistas del usuario
 SELECT * FROM USER_CATALOG WHERE TABLE_TYPE='VIEW'
  

