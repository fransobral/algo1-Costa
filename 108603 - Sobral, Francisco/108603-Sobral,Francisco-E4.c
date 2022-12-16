#include <stdio.h>
#include <stdbool.h>

bool ksum(int vector[], int n, int k){

    bool suma = false;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (vector[j] != vector[i]){
                if ((vector[j] + vector[i]) == k){
                    return true;
                }
            }
        }
    }
    return false;
}

int main(){
    int n,k;
    int vector[100];
    bool retorno  = 0;

    printf("Por favor ingrese el numero k: ");
    scanf(" %i", &k);

    printf("Por favor ingrese el tamanio del vector que desea ingresar: ");
    scanf(" %i", &n);
    
    for (int i = 0; i < n; i++) {
        int ingreso;
        printf("Por favor ingrese el numero %i del vector: ", (i+1));
        scanf(" %i", &ingreso);
        vector[i] = ingreso;
    }

    ksum(vector,n,k);
    retorno = ksum(vector,n,k);


    if(retorno==true){
        printf("Si exsisten dos indices que al sumarlos den k.\n");
    }
    else {
        printf("No hay dos indices que al sumarlos den k.\n");
    };

    return 0;
}

