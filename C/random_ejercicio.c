#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void){
	unsigned int i;
    srand ( time(NULL) );
    
    printf(" numeros generados aleatoriamente: \n \n");
    for(i=1 ; i<20; i++)
    {
        int random_numero = rand();
     	printf("%d \n",(random_numero % 3)+1);   
    }
	
	return 0;
}
// 1.- Realizar un juego que permita al usuario elegir entre 1 o 2 el computador 
//    debera de generar un numero que sera la opcion seleccionada por el computador.
//       si saca mayoria el numero seleccionado por el usuario gana el usuario.
//       Si ambos elegieron el mismo numero debera de generar nuevamente la maquina el numero.    

// 2.- tarea generar el juego del cachipun contra la maquina 
//           1 = piedra
//           2 = papel
//           3 = tijera 
// gana el que llega primero a las 3 partidas ganadas.