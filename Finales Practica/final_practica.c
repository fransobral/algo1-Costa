#include <stdio.h>

void asigna_max_min(int vec[],int tope, int *max, int *min){

    int maximo,minimo = vec[0];

    for(int i = 0; i < tope; i++) {
        if (maximo   < vec[i]){
            maximo = vec[i];
        }
    }

    for(int i = 0; i < tope; i++) {
        if (minimo  > vec[i]){
            minimo = vec[i];
        }
    }
    *max = maximo;
    *min = minimo;
}


int main(){
    int tam,producto,max,min;
    char palabra;

    printf("Por favor ingrese la cantidad de valores que desea ingresar: ");
    scanf(" %i", &tam);
    int vector[100];

    for (int i = 0; i < tam; i++) {
        int ingreso;
        printf("Por favor ingrese el numero %i del vector: ", (i+1));
        scanf(" %i", &ingreso);
        vector[i] = ingreso;
    }


    asigna_max_min(vector,tam,&max,&min);
    
    printf("El vector");

    for (int i = 0; i < tam; i++) {
        printf(" %d",vector[i]);
    }

    printf(" tiene como maximo %i y como minimo %i\n",max,min);

    return 0;
}