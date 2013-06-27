--Funciones PL/SQL
--Ejemplos breves visto en clases 
--1.- Funcion que calcula el 19% + sobre un numero 
create or replace
function f_iva( p_valor in number)
  return number
is
  v_ValorIvaIncluido number(5,2);
begin
  v_ValorIvaIncluido := p_valor*1.19;
  return v_ValorIvaIncluido;
end f_iva;

--Llamando a la funcion donde se pasa com parametro el precio que se encuentra
--en una tabla.
select f_iva(precio) as iva_incluido, precio from productos;


--2.- Funcion la cual ocupa el calculo del iva anterior para clasificar en base 
-- a un rango.
create or replace function f_rango(p_precio in number) 
  return varchar2
is
  v_rango varchar2(50);
  v_ivaInc number;
begin
    v_ivaInc := f_iva(p_precio);--Llamada a la funcion f_iva
    if ( v_ivaInc <= 200) then
        v_rango := 'Rango bajo';
    elsif  (v_ivaInc > 200) and (v_ivaInc <= 600) then
        v_rango := 'Rango medio';    
    elsif (v_ivaInc > 600 ) then
        v_rango := 'Rango alto';
    end if;
    return v_rango;
end f_rango;

--llamado a la funcion anterior pasando como parametros los precios de los productos.
select p_valores(precio) from productos;
--Instruccion  select utilizando las dos funciones anteriores f_rango y f_iva
select 
    p_valores(precio) as rango , 
    f_iva(precio)as iva_Incluido,
    precio as precio_neto,nombre
from
    productos;




 