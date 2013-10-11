#!/usr/bin/python
import sqlite3 
import sys
import os


def menu():
	print "_______MENU PRINCIPAL__________"
	print "Op 1 .- Ingresar persona_______"
	print "Op 2 .- Listar personas________"
	print "Op 3 .- Borrar una persona_____"
	print "Op 4 .- Actualizar persona_____"
	print "Op 5 .- Buscar una persona_____"
	print "Op 6 .- Salir__________________"
	print "_" * 31
	op = raw_input ("ingrese opcion:")
	return op

def limpiar():
	os.system('clear')
	 #print('\n' * 50)
	
def ingresar():
	print "Opcion 1 : ingresar persona"
	nombre = raw_input("Nombre:")
	apellidos = raw_input("Apellidos:")
	bd_con = conectar()
	bd_cursor = bd_con.cursor()
	bd_cursor.execute("insert into persona values(null,?,?)", (nombre,apellidos) )
	bd_con.commit()
	print "Datos insertados"
	bd_con.close()

def listar():
	print "Opion 2 : listar personas"
	bd_con = conectar()
	bd_cursor = bd_con.cursor()
	filas = bd_cursor.execute("select id,nombre,apellidos from persona")
	for fila in filas:
		print "Per: %s %s %s" % (fila[0] , fila[1], fila[2])
	bd_con.close()

def actualizar():
	print "Opcion 4: actualizar datos"
	id = int(raw_input("id de persona:"))
	nombre = raw_input("Ingrese nombre:")
	apellidos = raw_input("Ingrese apellidos:")
	bd_con = conectar()
	bd_cursor = bd_con.cursor()
	bd_cursor.execute("update persona set nombre=? , apellidos=?   where id=?", (nombre,apellidos,id))
	bd_con.commit()	
	if bd_cursor.rowcount == 0:
		print "No se encontra el registro con id:%s" % (id)
	else:
		print("registro actualizado")
		listar()

def actualizar1():
	print "actualizar datos"
	buscar()
	
	id = int(raw_input("ingrese id de persona:"))
	
	bd_con = conectar()
	bd_cursor = bd_con.cursor()
	sql = "select id , nombre, apellidos from persona where id=%s" % (id)
	bd_cursor.execute(sql)
	existe = bd_cursor.fetchone()
	if existe is None:
		print "No se encontro el registro"
	else:
		filas = bd_cursor.execute(sql)
		for fila in filas:
			print "Nombre:", fila[1]
			print "Appellidos", fila[2]
		
	
def buscar():
	print "buscar persona"
	patron = raw_input("Ingrese patron a buscar:")
	bd_con = conectar()
	bd_cursor = bd_con.cursor()
	patron = '%'+patron+'%'
	sql = "select id , nombre, apellidos from persona where nombre like '%s' or apellidos  like '%s' " % (patron, patron)
	bd_cursor.execute(sql)
	existe = bd_cursor.fetchone()
	if existe is None:
		print "No se encontro el registro"
	else:
		filas = bd_cursor.execute(sql)
		for fila in filas:
			print "id:%d Persona:%s %s" % (fila[0], fila[1], fila[2])
	
def conectar():
	bd = "test.db"
	if not os.path.isfile(bd):
		print "la bd no existe!!, se va a crear"
		bd_con = sqlite3.connect(bd)
		bd_con.execute('''create table persona(
			id integer primary key,
			nombre text not null,
		   	apellidos text not null)''')
		bd_con.commit()
	else:
		bd_con = sqlite3.connect(bd)
	return bd_con

def borrar():
	print "borrar"
	
	
def conexion():
	con = lite.connect('test.db')
	return con
	
def main():
	while True:
		op = menu()
		if (op != '6'):
			operaciones = { '1':ingresar, '2':listar, '3':borrar, '4':actualizar , '5':buscar}
			#try:
			operaciones[op]()
			raw_input("<<presione ENTER para continuar>>")
			limpiar()
			#except:
			#	print "opcion no valida"
		else:
			print "Adios !!! ;-( "
			limpiar()
			break

if __name__ == "__main__":main()

