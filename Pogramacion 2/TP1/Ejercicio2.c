#include <stdio.h>
#include <math.h>

// Constante de Gravedad
#define G 9.81
#define PI 3.14159265358979323846

// Función que evalua la trayectoria 
// retorna 0 = no llega, 1 = impacto, 2 = Supera 
int evaluarTrayectoria(double Vinicial, double angulo, double altura, double distancia){
    int Estado;
    double rad = angulo * PI / 180.0; // conversion a radianes
    double y = distancia * tan(rad) - (G * distancia * distancia) / (2 * Vinicial * Vinicial *  pow(cos(rad), 2));

    if (y<0){
        Estado = 0; // No llega
    }
    else if (y< altura){
        Estado = 1; // Impacta
    }
    else{
        Estado = 2; // Se pasa
    }
    return Estado;
}

int main(){
    double V_inicial, angulo, altura, distancia;

    printf("Velocidad Inicial: ");
    scanf("%lf",&V_inicial);

    printf("Angulo: ");
    scanf("%lf",&angulo);

    printf("Altura: ");
    scanf("%lf",&altura);

    printf("Distancia: ");
    scanf("%lf",&distancia);

    int resultado = evaluarTrayectoria(V_inicial,angulo,altura,distancia);
    switch(resultado){
        case 0: printf("No llega");break;
        case 1: printf("Impacta");break;
        case 2: printf("Se pasa");break;
    }
    return 0;
}