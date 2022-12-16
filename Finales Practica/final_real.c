#include <stdio.h>

void productoria(int vector[], int* producto, int tam){
    int producto_final = 1;
    for (int i = 0; i < tam; i++) {
        producto_final = producto_final * vector[i];
    }
    *producto = producto_final;
}


int main(){
    int tam,producto;
    printf("Por favor ingrese la cantidad de valores que desea ingresar: ");
    scanf(" %i", &tam);
    int vector[100];

    for (int i = 0; i < tam; i++) {
        int ingreso;
        printf("Por favor ingrese el numero %i del vector: ", (i+1));
        scanf(" %i", &ingreso);
        vector[i] = ingreso;
    }

    productoria(vector,&producto,tam);
    printf("La multiplicacion total es de %d\n",producto);

    return 0;
}