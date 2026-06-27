#include "contacto.h"
#include <cctype>
#include <algorithm>

Contacto::Contacto() : nombre(""), apellido(""), telefono(""), email("") {}
Contacto::Contacto(const std::string& n, const std::string& a, const std::string& t, const std::string& e) : nombre(n), apellido(a), telefono(""), email(e){setTelefono(t);
}

bool Contacto:: validarTelefono(const std::string& tel) {
    for (size_t i = 0; i < tel.size(); i++){
        char c = tel[i];
        if (!isdigit(c) && c != ' ' && c != '+'){
            return false ;
        }
    }
    return true; // vacio tambien se considera valido
}
//Gets
std::string Contacto::getNombre() const {return nombre;}
std::string Contacto::getapellido() const {return apellido;}
std::string Contacto::gettelefono() const {return telefono;}
std::string Contacto::getemail() const {return email;}

void Contacto::setTelefono(const std::string& t){
    if (validarTelefono(t)) telefono = t;
}

void Contacto::setEmail(const std::string& e){
    email = e;
}

// Operadores
std::ostream& operator<<(std::ostream& os, const Contacto& c) {
    os << c.nombre << ";" << c.apellido << ";"
       << c.telefono << ";" << c.email;
    return os;
}

std::istream& operator>>(std::istream& is, Contacto& c) {
    std::getline(is, c.nombre, ';');
    std::getline(is, c.apellido, ';');
    std::getline(is, c.telefono, ';');
    std::getline(is, c.email);
    return is;
}
