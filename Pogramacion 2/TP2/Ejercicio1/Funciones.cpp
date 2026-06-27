#include <iostream>
#include "Clases.h"
using namespace std;

// Construcor
Intervalo::Intervalo(double inf, double sup, bool ci, bool cs){
    inferior = inf;
    superior = sup;
    cerradoInferior = ci;
    cerrradoSuperior = cs;
}

// Mostrar los limites
void Intervalo::mostrar(){
    cout << (cerradoInferior ? "[":"(")
         << inferior << ", " << superior
         << (cerrradoSuperior ? "]":")") << endl;

}
//Consultar si un numero esta dentro 
bool Intervalo::contiene(double x){
    bool dentroInf = cerradoInferior ? (x>= inferior) : (x > inferior);
    bool dentroSup = cerrradoSuperior ? (x<= superior) : (x < superior);
    return dentroInf && dentroSup ;
}

// Ver si se superpone con intervalo superior
bool Intervalo::seSuperpone(Intervalo otro){
    return !(superior < otro.inferior || otro.superior < inferior);
}

// Ver si esta contenido en intervalo inferior
bool Intervalo::contenidoEn(Intervalo otro){
    return inferior >= otro.inferior && superior <= otro.superior;
}