#include <stdio.h>	// printf
#include <stdlib.h>     //rand srand

typedef int Tipo;        /* tipo de item del arreglo */
typedef int Indice;     /* tipo del índice */
#define noencontrado  -1
#define MaxEntradas  10

void llenar(Tipo *a, Indice inferior, Indice superior)
{
    Indice i;
    srand(1);
    for (i = inferior; i <= superior; i++) a[i] = rand();
}

Indice BusquedaSecuencial(Tipo A[], Indice Inf, Indice Sup, Tipo Clave)
{
  Indice i;
  for(i = Inf; i<=Sup; i++)
       if (A[i] ==  Clave) return(i);
  return (noencontrado) ;
  
}

Tipo Arreglo[MaxEntradas];

int main(void) 
{
    Indice Inf, Sup, Result;
    Tipo Clave;
    Inf = 0; Sup = MaxEntradas - 1;

    llenar(Arreglo, Inf, Sup);
    Clave=Arreglo[5];
    
    Result=BusquedaSecuencial( Arreglo, Inf, Sup, Clave);
    
    if (Result == noencontrado) 
       printf(" No se encontró clave %d\n", Clave);
    else
       printf(" En posición %d se encontró %d \n", Result, Clave);
    
    return (0);
}
