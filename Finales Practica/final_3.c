#include <stdio.h>

void hallar_max_min(int array[], int n, int* max, int* min){
    int maximo = array[0];
    int minimo = array[0];
    for(int i = 0; i < n; i++) {
        if (maximo < array[i]){
            maximo = array[i];
        }
        if (array[i] < minimo){
            minimo = array[i];
        }
    }
    *max = maximo;
    *min = minimo;

}

int main(){
    int max,min;
    int array[5] = {1,2,3,45,6};
    int n = 5;
    hallar_max_min(array,n,&max,&min);
    printf("El maximo es el numero %i, y el minimo es el %i.",max,min);

    return 0;
}