//Escribir una función int area_rectangulo(int base, int altura) que permita calcular el área de un rectángulo dada su base y altura.
#include <stdio.h>

int area_rectangulo(int base, int altura) {
    int i,area = 0;
    
    for (i=1;i<=base;i++)
    {
        area += altura;
        }
    return area;
}

int main(){
    int base,altura;

    printf("Ingrese la base del rectangulo: ");
    scanf(" %d", &base);

    printf("\nIngrese la altura del rectangulo: ");
    scanf(" %d", &altura);

    int area = area_rectangulo(base,altura);
    printf("El area del rectangulo es de %d\n",area);
    return 0;
}