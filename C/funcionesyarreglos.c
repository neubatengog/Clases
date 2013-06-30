#include <stdio.h>
#define TAMANO 10 //Constante TAMANO de valor 10 (dimension del arreglo)
#define dimension 10

//Prototipo de procedimiento recibe como parametro un arreglo
void leer_arreglo(int arreglo[]){
	int i;
	for(i=0;i<=TAMANO;i++){
		printf("ingrese un numero \n");
		scanf("%d",&arreglo[i]);
	}
}
void mostrar(int arreglo[]){
	int i;
	printf("numero %d",arreglo[0]);
suma=arreglo[0]+arreglo[1]+arreg	
}
void buscar( int arreglo[], int x){
	int i,indice,sw=1;
	for(i=0;i<=TAMANO;i++){
		if (x == arreglo[i]){
			printf ("el valor se encuentra en %d",i);
			sw=0;
		}
	}
	if (sw==1)
		printf("el valor no se enecuentra");
}

void ordenar(int arreglo[]){
	int haycambios=1, intercambio;
	while(haycambios)
	{
		haycambios=0;
		for (i=0;i<=TAMANO;i++){
			if (arreglo[i]>arreglo[i+1]){
				intercambio=arreglo[i];
				arreglo[i]=arreglo[i+1];
				arreglo[i+1]=intercambio;
				haycambios=1;
			}		
		}		
	}
	for(i=0;i<=TAMANO;i++){
		printf("numero %d - posicion %d",arreglo[i],i);
	}
}

void pares( int numeros[]){
	int i;
	for (i=0;i<=TAMANO;i++){
		if ( numeros[i]%2==0)
			printf ("Numero %d es par",numeros[i] );
		else 
			printf ("Numero %d es impar",numeros[i] );
	}
}

int main (){
	int numeros[TAMANO],x, valor;
	leer_arreglo(numeros);//llamada a funcion pasando como parametro un arreglo
	mostrar(numeros);
	printf("ingrese numero a buscar");
	scanf("%d",&x);
	buscar(numeros,x);
	ordenar(numeros);
	pares(numeros);
	getch();
}

