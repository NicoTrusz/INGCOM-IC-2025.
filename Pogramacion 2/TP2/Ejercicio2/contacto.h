#ifndef CONTACTO_H
#define CONTACTO_H

#include <string>
#include <iostream>

class Contacto {
    private: 
        std:: string nombre;
        std:: string apellido;
        std:: string telefono;
        std:: string email;

        bool validarTelefono (const std:: string& tel);
    public:
        Contacto();
        Contacto(const std::string& n, const std:: string& a, const std::string& t="", const std::string& e="");

        //Getters
        std:: string getNombre() const;
        std:: string getapellido() const;
        std:: string gettelefono() const;
        std:: string getemail() const;

        //setters
        void setTelefono(const std:: string& t);
        void setEmail(const std::string& e);

        // operadores de entrada/salida
         friend std::ostream& operator<<(std::ostream& os, const Contacto& c);
         friend std::istream& operator>>(std::istream& is, Contacto& c);

};

#endif