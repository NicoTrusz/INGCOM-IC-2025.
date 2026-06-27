#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;
// estructura con legajo, materia y fecha
struct Inscripcion {
    int legajo;
    string materia;
    string fecha;
};

class TADInscripciones {
private:
    vector<Inscripcion> inscripciones;

public:
// registro de inscripcion nueva
    void RegistrarInscripcion(int legajo, string materia, string fecha) {
        Inscripcion nueva{legajo, materia, fecha};
        inscripciones.push_back(nueva);
    }
// consulta inscripcion de materia
    void ConsultarPorMateria(string materia) {
        for (int i = 0; i < inscripciones.size(); i++) {
            if (inscripciones[i].materia == materia) {
                cout << "Legajo: " << inscripciones[i].legajo
                     << " Fecha: " << inscripciones[i].fecha << endl;
            }
        }
    }
// elimina inscripcion por legajo y materia
    void EliminarInscripcion(int legajo, string materia) {
        for (int i = 0; i < inscripciones.size(); i++) {
            if (inscripciones[i].legajo == legajo && inscripciones[i].materia == materia) {
                inscripciones.erase(inscripciones.begin() + i);
                break;
            }
        }
    }
    // muestra la cantidad pero en una sola materia
    int CantidadPorMateria(string materia) {
        int contador = 0;
        for (int i = 0; i < inscripciones.size(); i++) {
            if (inscripciones[i].materia == materia) {
                contador++;
            }
        }
        return contador;
    }
// por aclaracion de julieta....
    // cantidad de inscriptos por cada materia
     void MostrarCantidadPorMateria() {
        map<string, int> conteo;
        for (int i = 0; i < inscripciones.size(); i++) {
            conteo[inscripciones[i].materia]++;
        }

        map<string,int>::iterator it;
        for (it = conteo.begin(); it != conteo.end(); ++it) {
            cout << "Materia: " << it->first 
                 << " - Cantidad de inscriptos: " << it->second << endl;
        }
    }

    // materia con mas incriptos
    string MateriaConMasInscriptosDos(){
        map<string,int>conteo;
        for (int i = 0; i < inscripciones.size(); i++) {
            conteo[inscripciones[i].materia]++;
        }

        string materiaMax;
        int max=0;
        map<string,int>::iterator it;
        for(it =conteo.begin(); it != conteo.end();++it){
            if (it->second>max){
                max = it->second;
                materiaMax = it->first;
            }
        }
        return materiaMax;
        
    }

// OPCION 1
    string MateriaConMasInscriptos() {
        string materiaMax;
        int max = 0;
        for (int i = 0; i < inscripciones.size(); i++) {
            int cantidad = CantidadPorMateria(inscripciones[i].materia);
            if (cantidad > max) {
                max = cantidad;
                materiaMax = inscripciones[i].materia; 
            }
        }
        return materiaMax;
    }
// OPCION 2
    string FechaConMasInscriptorPorMateria(string materia){
        map<string, int> conteoPorFecha;

        // reccoro toda las inscripciones
        for (int i = 0; i < inscripciones.size(); i++) {
            if (inscripciones[i].materia == materia){
                conteoPorFecha[inscripciones[i].fecha]++;
            }
        }

        //Busco la fecha con mayor cantidad
        string fechaMax;
        int max = 0;
        map<string,int>::iterator it;
        for (it = conteoPorFecha.begin(); it != conteoPorFecha.end(); ++it) {
            if (it->second > max) {
                max = it->second;
                fechaMax = it->first;
            }
        }
        return fechaMax;
    }

};

// Ejemplo de uso en main
int main() {
    TADInscripciones sistema;

    sistema.RegistrarInscripcion(1, "Matematica", "2026-04-20");
    sistema.RegistrarInscripcion(2, "Matematica", "2026-04-21");
    sistema.RegistrarInscripcion(3, "Fisica", "2026-04-20");
    sistema.RegistrarInscripcion(4, "Fisica", "2026-04-22");
    sistema.RegistrarInscripcion(5, "Programacion", "2026-04-21");

    cout << " Consultar inscriptos en Matematica:" << endl;
    sistema.ConsultarPorMateria("Matematica");

    cout << "\n Cantidad de inscriptos por materia:" << endl;
    sistema.MostrarCantidadPorMateria();

    cout << "\n Materia con mas inscriptos (DOS): " 
         << sistema.MateriaConMasInscriptosDos() << endl; // lo que se pedia 

    cout << "\n Materia con mas inscriptos: "
         << sistema.MateriaConMasInscriptos() << endl; // lo que entendi en principio

    cout << "\n Fecha con mas inscriptos en Fisica: " 
         << sistema.FechaConMasInscriptorPorMateria("Fisica") << endl;

    return 0;
}