#include <stdio.h>	// printf
#include <stdlib.h>     //rand srand

typedef int Tipo;        /* tipo de item del arreglo */
typedef int Indice;      /* tipo del índice */
#define compGT(a,b) (a > b)
#define MaxEntradas  10

Tipo Arreglo[MaxEntradas];

void llenarAscendente(Tipo *a, Indice inferior, Indice superior)
{
    Indice i;
    for (i = inferior; i <= superior; i++) a[i] = (Tipo) i;
}
void llenarDescendente(Tipo *a, Indice inferior, Indice superior)
{
    Indice i;
    for (i = inferior; i <= superior; i++) a[i] = (Tipo) superior-i;
}

void llenarRandom(Tipo *a, Indice inferior, Indice superior)
{
    Indice i;
    srand(1);
    for (i = inferior; i <= superior; i++) a[i] = rand(); 
}


void mostrar(Tipo *a, Indice inferior, Indice superior)
{
    Indice i;
    for (i = inferior; i <= superior; i++) printf(" %d ", a[i]);
    putchar('\n');
}

/* Bubble sort for integers */
#define SWAP(a,b)   { t=a; a=b; b=t; }

void bubbleSort( Tipo a[], Indice Inf, Indice Sup )
/* Ordena ascendente. Desde Inf hasta Sup */
    {
    Indice i, j;
    Tipo t;  //temporal
    /* Recorre con i el arreglo desde Inf hasta Sup */
    for(i=Inf ;i<= Sup; i++)
        {
        /* Recorre con j, desde el siguiente a i hasta 
           el final de la zona no ordenada */
        for(j=Inf+1; j<=(Sup-(i-Inf)); j++)
           {
           /* Ordena elementos adyacentes, intercambiándolos */
           if( a[j-1]> a[j] ) SWAP(a[j-1], a[j]);
           }
        }
    }    

int main(void) 
{
    Indice Inf, Sup;
    Inf = 0; Sup = MaxEntradas - 1;

    llenarAscendente(Arreglo, Inf, Sup);
    mostrar(Arreglo, Inf, Sup);
       
    bubbleSort( Arreglo, Inf, Sup);
    
    mostrar(Arreglo, Inf, Sup);

    llenarDescendente(Arreglo, Inf, Sup);
    mostrar(Arreglo, Inf, Sup);
       
    bubbleSort( Arreglo, Inf, Sup);
    
    mostrar(Arreglo, Inf, Sup);

    llenarRandom(Arreglo, Inf, Sup);
    mostrar(Arreglo, Inf, Sup);
       
    bubbleSort( Arreglo, Inf, Sup);
    
    mostrar(Arreglo, Inf, Sup);
    system("pause");
    return (0);
}
