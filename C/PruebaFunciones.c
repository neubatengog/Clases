#include <stdio.h>

#define INGRESO 1
#define EGRESO 2
//#define STOCK_ACTUAL 3
#define SALIR 3


int menu()
{
    int op;
    printf("Ingrese una opcion\n");
    printf("1) ingresar elementos\n");
    printf("2) Egreso de elementos\n");
    printf("3) Salir\n");
    scanf("%d",&op);
    return op;
}

int ingresar(int stock,int *ingre_cant){
    int numero;
    printf("stock inicial %d\n", stock);
    printf("Numero de ingreso de elementos\n");
    scanf("%d",&numero);
    *ingre_cant = *ingre_cant + 1;
    stock += numero;
    return stock;
}

int egresar(int stock,int *egre_cant){
    int numero;
    printf("stock inicial %d\n", stock);
    printf("Numero de egreso de elementos\n");
    scanf("%d",&numero);
    if (stock >= numero ){
         stock -=numero;
         *egre_cant++;
    }
    else
        printf("No se puede realizar la operacion");
    return stock;
}

int main (void)
{
    int op,
        stock=0,
        egre_cant =0,
        ingre_cant=0;
    printf("Ingrese stock inicial\n");
    scanf("%d",&stock);
    do{
        op=menu(); 
        switch(op)
        {
            case INGRESO:
                stock=ingresar(stock,&ingre_cant);
                break;
            case EGRESO:
                stock=egresar(stock,&egre_cant);
                break;
            default:
                printf("Opcion no valida\n");
                break;            
        }
    }while( op!=SALIR );
    printf("Stock al finalizar %d \n", stock);
    printf("Cantidad de egresos %d\n",egre_cant);
    printf("Cantidad de ingresos %d\n",ingre_cant);
	return 0;
}

