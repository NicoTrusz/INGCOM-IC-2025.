#include "juego.h"
#include "jugadores.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main() {
  srand(time(NULL)); // inicio del clk
  int tam = 8;
  int cantidad_jugadores = MAX_JUGADORES;

  char **jugador = crear_tablero(tam);
  char **computadora = crear_tablero(tam);
  bool **disparos_cpu = crear_matriz_bool(tam);

  // creacion / apertura del archivo jugador.txt
  // donde se guardan las jugadas del usuario
  FILE *log_jugador = fopen("jugador.txt", "w");

  // creacion / apertura del archivo computadora.txt donde se
  // guardan las jugadas del Computadora
  FILE *log_computadora = fopen("computadora.txt", "w");

  inicializar_tablero(jugador, tam);
  inicializar_tablero(computadora, tam);
  colocar_barcos(jugador, tam);
  colocar_barcos(computadora, tam);

  Jugador jugador_data;
  inicializar_jugador(&jugador_data);

  int score_jugador = 0, score_cpu = 0;
  jugador_data.score = 0;
  jugador_data.disparos = 0;
  char *mensaje_jugador = "";
  char *mensaje_cpu = "";
  while (true) {
    //system("cls"); // Limpia la terminal
    printf("\033[2J\033[H"); // este funca en Linux  =D

    printf("\nTu tablero: \n");
    imprimir_tablero(jugador, tam, false);
    printf("\n tablero enemigo:\n");
    imprimir_tablero(computadora, tam, false);
    printf("\n Leyenda: B = Barco   X = Impacto  O = Agua  ~ = no disparado\n");

    if (strlen(mensaje_jugador) > 0) {
      printf("\nResultado de tu disparo: %s\n", mensaje_jugador);
    }
    if (strlen(mensaje_cpu) > 0) {
      printf("Resultado del disparo de la computadora: %s\n", mensaje_cpu);
    }

    int f, c;
    do {
      printf("Disparo (fila columna): ");
      if (scanf("%d %d", &f, &c) != 2) {
        printf("\nEntrada invalida\n");
        exit (1);
      }
      if (f < 0 || f >= tam || c < 0 || c >= tam)
        printf("Coordenadas fuera de rango.\n");
      else if (computadora[f][c] == 'X' || computadora[f][c] == 'O')
        printf("Ya disparaste ahi.\n");

    } while (f < 0 || f >= tam || c < 0 || c >= tam ||
             computadora[f][c] == 'X' || computadora[f][c] == 'O');

    bool acierto = disparar(computadora, f, c);
    jugador_data.disparos++;
    if (acierto) {
      score_jugador++;
      jugador_data.score++;
      mensaje_jugador = "Impacto";
    } else {
      mensaje_jugador = "Agua.";
    }
    registrar_disparo(log_jugador, f, c, acierto);

    if (!quedan_barcos(computadora, tam)) {
      printf("Ganaste\n");
      break;
    }

    printf("\nTurno de la computadora...\n");
    bool acierto_cpu = disparo_computadora(jugador, disparos_cpu, tam,
                                           log_computadora, &score_cpu);
    mensaje_cpu = acierto_cpu ? "La COMPUTADORA IMPACTO" : "LA COMPUTADORA AGUA";

    if (!quedan_barcos(jugador, tam)) {
      printf("Perdiste. Todos tus barcos fueron hundidos.\n");
      break;
    }
  }
 /* printf("\n Puntaje Final :\n Jugador %d \n Computadora: %d\n", score_jugador,
         score_cpu);
  if (score_jugador > score_cpu) {
    printf("Tuviste mejor punteria\n");
  } else if (score_jugador < score_cpu) {
    printf("Te Gano la Computadora");
  }
    */
  mostrar_resultado_final(jugador_data, score_cpu);
  fclose(log_jugador);
  fclose(log_computadora);
  liberar_tablero(jugador, tam);
  liberar_tablero(computadora, tam);
  liberar_matriz_bool(disparos_cpu, tam);

  return 0;
}

/*
----------------------NOTAS PARA REPARAR------------------------
        * En las cordenadas si se colocan letras o caracteres
          se rompe y entra en bucle de llamada de cordenadas
          ** arreglo momentaneo si se agrega al gun valor que no sea numerico finaliza el programa

*/