#include  <stdio.h>

#define EGRESO 1
#define INGRESO 2
#define SALIR 3 

int stock=0;
int trans_egreso = 0;
int trans_ingreso = 0;

void estadistica(){
    printf("Transacciones de egreso %d\n", trans_egreso);
    printf("Transacciones de Ingreso %d\n", trans_ingreso);
    printf("Transacciones realizadas %d\n", trans_egreso+trans_ingreso);
    printf("STOCK total %d", stock);
}

void egreso(){
    int unidades;
    printf("Ingrese numero de unidades a egresar\n");
    scanf("%d",&unidades);
    if (unidades > stock)
        printf("no hay stock");
    else{
        stock = stock - unidades;
        trans_egreso = trans_egreso + 1;
    }    
}

void ingreso(){
    int unidades;
    printf("Numero de unidades a ingresar\n");
    scanf("%d",&unidades);
    stock = stock + unidades;
    trans_ingreso = trans_ingreso + 1;
}

int menu();
void stock_inicial(){
    printf("Ingrese stock inicial\n");
    scanf("%d", &stock);
}

int main(void)
{
    int op;
    stock_inicial();
    do{
        op = menu();
        switch(op){
            case EGRESO:
                egreso();
                break;
            case INGRESO:
                ingreso();
                break;
            case SALIR:
                estadistica();
                break;                
            default:
                printf("Opcion invalida\n");
                break;
        }
    }while( op != SALIR);  
    
      
    return 0;    
}

int menu()
{
    int op;
    printf("Opcion 1 : egreso\n");
    printf("Opcion 2 : ingreso\n");
    printf("Opcion 3 : Salir\n");
    scanf("%d",&op);
    return op;
}