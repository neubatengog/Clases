--Atributos de un cursor
--%FOUND: retorna TRUE si el resgistro es encontrado
--%NOTFOUND: Retorna TRUE si el registro no ha sido encontrado
--%ROWCOUNT: Retorna el numero de registos afectados por le cursor en un punto 
--%ISOPEN : Retorna TRUE 
--%BULK_ROWCOUNT : Retorna el numero de registros modificados por FORALL(FOR EACH)
--%BULK_EXCEPTIONS


--Declarat el cursor
--Abrir el cursor instruccion OPEN
--Leer los datos con la instruccion FETCH
--Cerrar el cursor y liberar recursos con CLOSE
DECLARE 
  CURSOR C1 IS SELECT codasig, numsec FROM SECCION WHERE CEDPROF = '4567890';
  V_CODASIG CHAR(6);
  V_NUMSEC CHAR(2);
BEGIN
  IF NOT C1%ISOPEN THEN
    OPEN C1;
  END IF;
  LOOP
    FETCH C1 INTO v_codasig, v_numsec;
    EXIT WHEN C1%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE('CODIGO :' || v_codasig || ' SECCION:' || v_numsec);
  END LOOP;
     DBMS_OUTPUT.PUT_LINE('Filas afectadas:' || C1%ROWCOUNT);
  CLOSE C1;
END;

--Procedimiento almacenado con pasaje de parametro
create or replace procedure p_listar_secciones(p_cedprof in char)
IS
  V_CEDULA char(8); --Variable de acoplamiento
  CURSOR C1 IS SELECT codasig, numsec FROM SECCION WHERE CEDPROF = V_CEDULA;
  V_CODASIG CHAR(6);
  V_NUMSEC CHAR(2);
BEGIN
  V_CEDULA := p_cedprof;
  IF NOT C1%ISOPEN THEN
    OPEN C1;
  END IF;
  LOOP
    FETCH C1 INTO v_codasig, v_numsec;
    EXIT WHEN C1%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE('CODIGO :' || v_codasig || ' SECCION:' || v_numsec);
  END LOOP;
     DBMS_OUTPUT.PUT_LINE('Filas afectadas:' || C1%ROWCOUNT);
  CLOSE C1;
END p_listar_secciones;


--PROCEDIMINETO CON VARIABLES TIPO ROWTYPE
create or replace
procedure p_listar_seccion(p_cedprof in char)
IS
  V_CEDULA char(8);
  CURSOR C1 IS SELECT * FROM SECCION WHERE CEDPROF = V_CEDULA;
  v_seccion_reg SECCION%ROWTYPE;
BEGIN
  V_CEDULA := p_cedprof;
  IF NOT C1%ISOPEN THEN
    OPEN C1;
  END IF;
  LOOP
    FETCH C1 INTO V_SECCION_REG;
    EXIT WHEN C1%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE('CODIGO :' || V_SECCION_REG.codasig || ' SECCION:' || V_SECCION_REG.numsec);
  END LOOP;
     DBMS_OUTPUT.PUT_LINE('Filas afectadas:' || C1%ROWCOUNT);
  CLOSE C1;
  EXCEPTION
    WHEN 
END p_listar_seccion;

--FOR
create or replace
procedure p_listar_seccion_FOR(p_cedprof in char)
IS
  V_CEDULA char(8);
  CURSOR C1 IS SELECT * FROM SECCION WHERE CEDPROF = V_CEDULA;
  v_seccion_reg SECCION%ROWTYPE;
BEGIN
  V_CEDULA := p_cedprof;
  FOR V_SECCION_REG IN C1
  LOOP     
    DBMS_OUTPUT.PUT_LINE('CODIGO :' || V_SECCION_REG.codasig || ' SECCION:' || V_SECCION_REG.numsec);
  END LOOP;
     DBMS_OUTPUT.PUT_LINE('Filas afectadas:' || C1%ROWCOUNT);
END p_listar_seccion_FOR;

-- cursor Parametrizado
create or replace
procedure p_listar_seccion_FOR(p_cedprof in char)
IS
  V_CEDULA char(8);
  CURSOR C1(P_CED CHAR) IS SELECT * FROM SECCION WHERE CEDPROF = P_CED;
BEGIN
  
  FOR REC IN C1(p_cedprof)
  LOOP     
    DBMS_OUTPUT.PUT_LINE('CODIGO :' || REC.codasig || ' SECCION:' || REC.numsec);
  END LOOP;
END p_listar_seccion_FOR;

<
--CURSOR CON PASAJE DE PARAMETROS ANIDADO
create or replace
procedure p_listar_carrera
IS
   CURSOR c_car IS SELECT * FROM carrera;
   CURSOR c_est(P_IDCARRERA CHAR) IS SELECT * FROM ESTUDIANTE WHERE IDCARRERA = P_IDCARrERA;
BEGIN
  --V_CEDULA := p_cedprof;
  FOR reg1 IN c_car
  LOOP     
    DBMS_OUTPUT.PUT_LINE('Carrera :' || reg1.nombre);
    FOR reg2 in c_est(reg1.idcarrera)
    loop
      DBMS_OUTPUT.PUT_LINE('Rut:' || reg2.rut || ' Nombre: ' || reg2.apynombre);
    end loop;
  END LOOP;
END p_listar_carrera;

declare
begin
  p_listar_carrera;
end;


DECLARE
   CURSOR C_CREDITOS IS  SELECT CREDINS,RUT FROM ESTUDIANTE WHERE IDCARRERA = '101';  
BEGIN
    FOR REG IN C_CREDITOS
    LOOP
        IF REG.CREDINS > 7 THEN
            UPDATE ESTUDIANTE SET CREDINS=12 WHERE RUT = REG.RUT AND IDCARRERA ='101';
        END IF;
    END LOOP; 
END;
--Todos los estudiantes de arte que esten sobre los 12 creditos deberan de quedar en 8 creditos.
--Todas las carreras de 1 semestre deberan ser actualizadas a 2 semestres y las de tres semestres a 2.
--Guardar en una tabla temporal los datos y los creditos faltantes de los alumnos que esten bajo 
--el promedio en su indice.
--

