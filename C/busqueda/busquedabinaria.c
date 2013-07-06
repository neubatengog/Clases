#include <stdio.h>	// printf
#include <stdlib.h>     //rand srand

typedef int Tipo;        /* tipo de item del arreglo */
typedef int Indice;      /* tipo del índice */
#define noencontrado  -1
#define MaxEntradas  10
#define forever  1

Tipo Arreglo[MaxEntradas];

void llenar(Tipo *a, Indice inferior, Indice superior)
{
    Indice i;
    for (i = inferior; i <= superior; i++) a[i] = (Tipo) i;
}


int BinarySearch (Tipo A[], Indice Inf, Indice Sup, Tipo Clave)
{
  Indice M;
  while (forever)
   {
    M = (Inf + Sup)/2;
    if (Clave < A[M]) 
      Sup = M - 1;
    else if (Clave > A[M]) 
      Inf = M + 1;
    else
      return M;
    if (Inf > Sup) return (noencontrado) ;
   }
}
 



int main(void) 
{
    Indice Inf, Sup, Result;
    Tipo Clave;
    Inf = 0; Sup = MaxEntradas - 1;

    llenar(Arreglo, Inf, Sup);
    Clave=Arreglo[5];
    
    Result=BinarySearch( Arreglo, Inf, Sup, Clave);
    
    if (Result == noencontrado) 
       printf(" No se encontró clave %d\n", Clave);
    else
       printf(" En posición %d se encontró %d \n", Result, Clave);
    return (0);
    system("pause");
}
