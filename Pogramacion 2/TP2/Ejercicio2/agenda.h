#ifndef AGENDADECONTACTOS_H
#define AGENDADECONTACTOS_H

#include<iostream>
#include "contacto.h"

const int MAX_CONTATCOS = 100;

class AgendaDeContactos {
    private: 
        Contacto contactos[MAX_CONTATCOS];
        int cantidad;
    public:
        AgendaDeContactos();

        void agregarContacto(const Contacto& c);
        void editarContacto(const std::string& nombre, const std::string& apellido, const Contacto& nuevo);
        void borrarContacto(const std::string& nombre, const std::string& apellido);
        const Contacto* consultarContacto(const std::string& nombre, const std::string& apellido) const;
        int cantidadContactos() const;

        // Operadores de entrada/salida
        friend std::ostream& operator<<(std::ostream& os, const AgendaDeContactos& a);
        friend std::istream& operator>>(std::istream& is, AgendaDeContactos& a);

};

#endif