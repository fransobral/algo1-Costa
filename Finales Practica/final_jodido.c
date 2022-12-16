/*eS pide desarrollar un programa en lenguaje C, que cumpla con este enunciado:
En el sector de calidad de nuestra industria se realizan mediciones de la concentración de un
contaminante en ciertas muestras. Los valores que se registran son enteros.
El sector nos pide que escribamos un programa que permita ingresar los valores de las mediciones
(máximo 50) y le informe:
1) Cantidad total de mediciones ingresadas.
2) Los valores de las mediciones que son mayores al valor generado por la fórmula:
Valor = (máximo - mínimo) / 2
Para esto nos brindan la función "asigna_max_min" que debemos utilizar para hallar el máximo y
el mínimo.
/*
Recibe un vector de enteros con su respectivo tope y asigna a max y min el valor máximo y
mínimo del vector.
*/
//void asigna_max_min(int vec[MAX],int tope, int *max, int *min)*/

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

void valoresMayoresPromedio(int medicamentos[],int cant){
    int max,min;
    asigna_max_min(medicamentos,cant,&max,&min);
    int promedio = ((max-min)/2);
    for(int i = 0; i < cant; i++) {
        if (medicamentos[i] > promedio){
            printf("\nEl valor de la medicacion es de %d.\n",medicamentos[i]);
        }
    }
}

int cargar_medicaciones(int medicaciones []){
    int cargar = 1;
    int i = 0;
    int valor;

    while (cargar == 1){ //AGREGAR NO MMAS DE 50
        if (i < 50){
            printf("Ingrese el valor de la medicacion: ");
            scanf(" %d", &valor);
            medicaciones[i] = valor;
            i++;
            printf("Desea seguir cargando medicamentos? (1 si/ 2 no): ");
            scanf(" %d",&cargar);
        }
        else{
            printf("Ya hay 50 valores ingresados.");
            break;
            }
    }

    return i;
}


int main(){

    int medicaciones[50] = {0};
    int len_medicaciones = cargar_medicaciones(medicaciones);
    printf("\nEl total de medicaciones ingresadas es de: %d\n",len_medicaciones);
    valoresMayoresPromedio(medicaciones,len_medicaciones);

    return 0;
}