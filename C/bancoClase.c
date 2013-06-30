#include <stdio.h>
#include <stdlib.h>


//Protottipos de funciones
int menu();
int agregarmonto( int valor);
int retirarmonto(int valor);
int consultarmonto(int valor);
int lineadecredito(int valor);


int main ()
{
	//Variable local con el monto incial
	int saldo=150000;
	int op = 0;
	do{		
		op=menu();
		switch (op){
			case 1:{
				//funcion agregar un monto ingresado al saldo, que es pasado como parametro (saldo)
				saldo=agregarmonto(saldo);
				break;
			}
			case 2:{
				//funcion resta un monto ingresaado al saldo, que es pasado por parametro
				saldo=retirarmonto(saldo);
				break;
			}
			case 3:{
				//Procedimiento que muestra el valor del saldo
				consultarmonto(saldo);
				break;
			}
			case 4:{
				//Funcion que retorna el nuevo saldo, si el usuario deseas pedir un prestamo
				saldo=lineadecredito(saldo);
				break;
			}
			case 5:{
				//Salida del programa
				printf("Adios!!!!\n");
				break;
			}
			default:{
				// si no encuentra en ninguna de las opciones
				printf("Opcion no valida\n");
				break;
			}		
		}
	}
	while (op !=5 );
	
	return 0;
}

int lineadecredito(int valor){
	//system("clear");
	int monto;
	printf("Monto que desea pedir\n" );
	scanf("%d",&monto);
	valor = valor + monto;
	printf ("su nuevo saldo actual es: $%d \n",valor);
	return valor;
	
}

int consultarmonto(int valor){
	//system("clear");
	printf ("su nuevo saldo actual es: $%d \n",valor);
	
}

int agregarmonto(int valor){
	//system("clear");
	int monto;
	printf("Monto que desea ingresar?\n");
	scanf("%d",&monto);
	valor = valor + monto;
	printf ("su nuevo saldo actual es: $%d \n",valor);
	return valor;
}

int retirarmonto(int valor){
	//system("clear");
	int monto;
	char op;
	if (valor > 0){
		printf("Monto que desea retirar?\n");
		scanf("%d",&monto); 

		if (monto <= valor)
			valor = valor - monto;
		else{
			printf("saldo insuficiente\n");
			printf("desea ud pedir un credito s/n \n");
			scanf("%c",&op);
			
			if (( op=='S') || (op=='s'))
				valor=lineadecredito(valor);	
		}
	}
	printf ("su nuevo saldo actual es: $%d \n",valor);
	return valor;
}

int menu(){
	int opcion = 0;
	//system("clear");
	printf("MENU PRINCIPAL\n");
	printf("Ingrese una opcion:\n");
	printf("Agregar monto......(1)\n");
	printf("Retirar monto......(2)\n");
	printf("Consultar saldo....(3)\n");
	printf("Pedir credito......(4)\n");
	printf("Salir..............(5)\n");
	printf("Opcion:");
	scanf("%d",&opcion);
	return opcion;	
}