#include <stdio.h>
#include <string.h>

#define LUGARES 5
#define VACIO 0


#define SALIR 5 
#define INGRESAR 1
#define EGRESAR 2
#define MOSTRAR 3
#define RECAUDADO 4


struct Auto{
    char patente[6];
    int hora_llegada,
        minutos_llegada;
};

int menu(){
    int op;
    printf("OP1 INGRESAR\n");
    printf("OP2 EGRESAR\n");
    printf("OP3 MOSTRAR\n");
    printf("OP4 RECAUDADO\n");
    printf("OP5 SALIR\n");
    scanf("%d",&op);
    return op;
}
    
void inicializar(struct Auto Estacionamiento[ ]){
    int i;
    for(i = 0; i < LUGARES; ++i)
    {
        strcpy(Estacionamiento[i].patente,"VACIO");
        Estacionamiento[i].hora_llegada = VACIO;
        Estacionamiento[i].minutos_llegada = VACIO;
    }
}

void listar(struct Auto Estacionamiento[ ])
{
    int i;
    printf("LISTADO DE LUGARES:\n");
    printf("LUGAR\t PATENTE\t HORA\t \n");
    for(i = 0; i < LUGARES; ++i)
    {
        printf("%d\t",i);
        printf("%s\t",Estacionamiento[i].patente);
        printf("%d : %d \n",Estacionamiento[i].hora_llegada,Estacionamiento[i].minutos_llegada);
    }
}



int main(void){
    int op;
    struct Auto Estacionamiento[LUGARES] ;
    inicializar(Estacionamiento);
    
    do{
        op=menu();
        switch(op){
            case INGRESAR:
                break;
            case EGRESAR:
                break;
            case MOSTRAR:
                listar(Estacionamiento);
                break;
            case RECAUDADO:
                break;
            case SALIR:
            printf("GRACIAS POR USAR NUESTROS SERVICIOS\n");
                break;
            default:
            printf("OPCION NO VALIDA\n");
                break;
        }  
        
    }while(op !=SALIR);
    return 0;
}