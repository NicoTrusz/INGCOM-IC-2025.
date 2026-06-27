#ifndef INTERVALO_H
#define INTERVALO_H

class Intervalo{
    private:
    double inferior;
    double superior;
    bool cerradoInferior;
    bool cerrradoSuperior;

    public:
    Intervalo (double inf, double sup, bool ci, bool cs);

    void mostrar();
    bool contiene(double x);
    bool seSuperpone(Intervalo otro);
    bool contenidoEn(Intervalo otro);

};

#endif // INTERVALO_H