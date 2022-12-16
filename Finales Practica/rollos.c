/*
 * Se pide hacer un programa en lenguaje C, que permita:
a- Crear una función para la registración de rollos de tela a una fábrica textil, cada rollo posee
un nro de rollo y un peso en kg.
Se pide:
- Calcular el peso promedio de los rollos que han ingresado a la fábrica.
- Determinar nro de rollo cuyo peso sea el mayor de entre todos los rollos
ingresados.
b- Sabiendo que la encimadora de tela utiliza rollos mayores a 12kg, crear una función que sea
llamada por la del pto a, que valide el peso del rollo y en caso que el mismo sea menor a
12kg imprima un mensaje “Error fuera de norma”
 */
#include <stdio.h>

void pesoPromedio(int peso_rollo[],int cant){
    int suma = 0;
    for(int i = 0; i < cant; i++) {
        suma += peso_rollo[i];
    }
    float suma_f = suma;
    float cant_f = cant;
    float promedio = (suma_f/cant_f);
    printf("El promedio de peso de los pollos es de %f kg.",promedio);
}

void mayorPeso(int peso[],int cant){
    int maximo = peso[0];
    for(int i = 0; i < cant; i++) {
        if (maximo   < peso[i]){
            maximo = peso[i];
        }
    }
    printf("\nEl peso maximo es: %d",maximo);
}

void validar_peso_rollo(int *peso_rollo){
    int peso_rollo_nuevo;
    while ((*peso_rollo) <= 12){
        printf("\nError, fuera de norma. Ingrese un nuevo valor mayor a 12: ");
        scanf(" %d",&peso_rollo_nuevo);
        *peso_rollo = peso_rollo_nuevo;
    }
}

int main(){
    int num_rollo,peso_rollo;
    int i = 0;
    int repeticion = 1;
    int rollo[100]={};
    int peso[100]={};

    while (repeticion == 1){

        printf("\nPor favor ingrese el numero de rollo: ");
        scanf(" %d",&num_rollo);

        printf("\nPor favor ingrese el peso del rollo: ");
        scanf(" %d",&peso_rollo);
        validar_peso_rollo(&peso_rollo);
        printf("peso_rollo: %d",peso_rollo);
        rollo[i] = num_rollo;
        peso[i] = peso_rollo;
        i++;
        printf("\nDesea seguir agregando datos? (1si/2no): ");
        scanf(" %i",&repeticion);

    }
    pesoPromedio(peso,i);
    mayorPeso(peso,i);
    return 0;
