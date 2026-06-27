#include <iostream>
#include "Clases.h"
using namespace std;

int main(){
    Intervalo a(1,5,true,false); //[1,5) inferior//superior//CotaInferior//CotaSuperior
    Intervalo b(3,7,true,true); // [3,7]

    cout << "Intervalo a: "; a.mostrar();
    cout << "Intervalo b: "; b.mostrar();

    cout << "4 esta en a?" << (a.contiene(4) ? "Si" : "No") << endl ;
    cout << "a se superpone con b?" <<(a.seSuperpone(b) ? "Si" : "No") ;
    cout << "a esta contenido en b?" << (a.contenidoEn(b) ? "Si" : "No");

    return 0;
}
