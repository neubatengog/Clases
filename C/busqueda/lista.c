#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef struct moldenodo
       { int clave;
         struct moldenodo *proximo;
       } nodo, *pnodo;

pnodo CreaNodo(int dato)
{  
  pnodo pn=NULL; 
  if ( (pn= (pnodo) malloc(sizeof(nodo))) ==NULL) 
   {printf ("Memoria insuficiente para crear nodo\n"); exit(1);}
  else 
   {
      pn->clave=dato; pn->proximo=NULL; 
   }
   return(pn);
}
/*inserta nodo antes  */
pnodo InsertaNodoAntes(pnodo posicion, pnodo nuevo)
{
     if (nuevo == NULL) return (NULL);
     if (posicion!=NULL) nuevo->proximo=posicion;	//O(1)
     return nuevo; 
}

pnodo InsertaNodoDespues(pnodo posicion, pnodo nuevo)
{
      if (nuevo == NULL) return (NULL);
      if (posicion!=NULL) 
        {  nuevo->proximo=posicion->proximo; //enlaza con el resto de la lista
           posicion->proximo=nuevo;  //termina de enlazar el nuevo nodo
           return (posicion);
         }
     return nuevo; 
}
pnodo InsertaNodoalFinal(pnodo posicion, int dato)
{    pnodo temp=posicion;
     if(temp != NULL)
        {
          while (temp->proximo !=NULL) temp=temp->proximo;  //O(n)
          temp->proximo=CreaNodo(dato);
          return(posicion);
        }
    else
       return(CreaNodo(dato));
}

/*
Dada la dirección de un nodo de la lista
Retornar el número de nodos desde el apuntado hasta el final de la lista.
*/
int LargoLista(pnodo p) 
{      int numeroelementos = 0;

        while (p != NULL) {
           numeroelementos ++;
           p = p ->proximo;  //recorre la lista
        }
       return (numeroelementos);
}

int LargoListaFor(pnodo p) 
{      int numeroelementos = 0;
      for( ; p != NULL; p=p->proximo) numeroelementos ++;
       return (numeroelementos);
}

pnodo Buscar(pnodo p, int valor) 
{     
        while (p != NULL) {
           if(p->clave== valor) return (p);
           else p = p ->proximo;  //recorre la lista.  O(n)
        }
       return (p);
}
/*
pnodo BuscarAntes(pnodo p, int valor) 
{       pnodo q;
        while (p != NULL) {
           if(p->clave== valor) return (p);
           else p = p ->proximo;  //recorre la lista.  O(n)
        }
       return (p);
}

*/
pnodo SeleccionarMinimo(pnodo p) 
{   int min;
    pnodo t;
        if(p==NULL) return (NULL); 
        else 
            {min=p->clave;
             t=p; 
             p=p->proximo;
            }
        while (p != NULL) {
           if(p->clave <min ) {min=p->clave;t=p;}
           p = p ->proximo;  //recorre la lista.  O(n)
        }
       return (t);
}
//Buscar el último nodo.
pnodo ApuntarAlFinal(pnodo p) 
{    pnodo t;
       if(p==NULL) return (NULL); 
       else 
         { t=p;
           p=p->proximo;      
         }
       while (p != NULL) {
           t=p;
           p = p ->proximo;  //recorre la lista.  O(n)   
        }
       return (t);
}



pnodo Descartar(pnodo p) 
{  pnodo t = p;

   if (p==NULL) return (p);   // Lista vacía
   if ( p->proximo==NULL)
        {  free(p);
           return(NULL); // Último de la lista
        }
   else 
    {   t=p->proximo; 
        free(p); 
        return (t);  //Retorna enlace si borró el nodo.
    }
}


void PrtNodo(pnodo p)
{
  if(p!=NULL) printf(" Clave Nodo = %d \n", p->clave);
  else  printf(" No encontrado\n");
}


void PrintLista(pnodo p) 
{       pnodo t;
        if(p==NULL) printf(" lista vacía.");
        for(t =p; t != NULL;t=t->proximo) 
             printf(" %d, ", t->clave);
        putchar('\n');
}


pnodo listad=NULL;
pnodo listaa=NULL;

int main(void)
{  int i;
   pnodo q;
   
   for(i=0; i<10; i++)
     listad =InsertaNodoAntes(listad, CreaNodo(i));
   PrintLista(listad);
   printf(" largo lista = %d \n", LargoListaFor(listad) );
   
   for(i=0; i<10; i++)
     listaa =InsertaNodoDespues(listaa, CreaNodo(i));
   PrintLista(listaa);
   
   for(i=0; i<10; i++) 
      {listaa=Descartar(listaa);
       PrintLista(listaa);
       printf(" largo lista = %d \n", LargoLista(listaa) );
      } 
   
   for(i=0; i<10; i++)
     listaa =InsertaNodoalFinal(listaa, i);
   PrintLista(listaa);
   
   PrtNodo( SeleccionarMinimo(listaa));
   PrtNodo( SeleccionarMinimo(listad));
   
   PrtNodo( ApuntarAlFinal(listaa)); 
   PrtNodo( ApuntarAlFinal(listad));
   
   PrtNodo(Buscar(listaa,4));
   PrtNodo(Buscar(listaa,12));

   PrtNodo(InsertaNodoDespues(Buscar(listaa,4), CreaNodo(12))->proximo);
   PrintLista(listaa);
   
   q=Buscar(listaa,7);
   
   return(0);
}


