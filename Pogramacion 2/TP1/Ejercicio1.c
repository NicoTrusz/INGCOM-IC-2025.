#include <stdio.h>
#include <math.h>

void costo_infraestructura(double x, double y){
    const double costo_del_borde = 10 * (x + y);
    const double costo_de_diagonal = 18 * sqrt(x * x + y * y);

    printf("Borde : $%2.f\n", costo_del_borde);
    printf("Diagonal : $%2.f\n", costo_de_diagonal);

    if (costo_del_borde < costo_de_diagonal){
        printf("Comviene cablear por el borde");
    }
    else if (costo_de_diagonal < costo_del_borde){
        printf("conviene cablear por diagonal");
    }
    else {
        printf("Ambas opciones cuestan lo mismo");
    }
}

int main (){
    double x, y;
    printf("Ingrese el valor de X: ");
    scanf("%lf",&x);

    printf("Ingrese el valor de Y: ");
    scanf("%lf",&y);

    costo_infraestructura(x,y);
    return 0;
}