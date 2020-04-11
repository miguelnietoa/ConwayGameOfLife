import pygame
import os
from Game import Game


def dibujarTablero(elementos):
    for row in range(n):
        for col in range(n):
            pygame.draw.rect(pantalla,
                             BLANCO,
                             [MARGEN + (MARGEN + LARGO) * col,
                              MARGEN + (MARGEN + ALTO) * row,
                              LARGO,
                              ALTO])
    for element in elementos:
        fila, columna = element
        pygame.draw.rect(pantalla,
                         ROJO,
                         [MARGEN + (MARGEN + LARGO) * columna,
                          MARGEN + (MARGEN + ALTO) * fila,
                          LARGO,
                          ALTO])


# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Establecemos el tamaño del tablero n*n (max = 300)
n = 30
N = 300
# Establecemos el LARGO y ALTO de la pantalla
DIMENSION_VENTANA = [601, 601]

# Establecemos el margen entre las celdas.
MARGEN = 1

# Establecemos el LARGO y ALTO de cada celda de la retícula.
LARGO = ALTO = (DIMENSION_VENTANA[0] - (n + 1)) // n
print(n * LARGO + (n + 1) * MARGEN)

coord_inicial = (DIMENSION_VENTANA[0] - (n * LARGO + (n + 1) * MARGEN)) // 2

# Se actualiza la dimension de la ventana a la necesaria.
DIMENSION_VENTANA = [n * LARGO + (n + 1) * MARGEN, n * LARGO + (n + 1) * MARGEN]

generaciones = Game(n, N)

# Inicializamos pygame
pygame.init()

# Centramos la ventana
os.environ['SDL_VIDEO_CENTERED'] = '1'

pantalla = pygame.display.set_mode(DIMENSION_VENTANA)

# Establecemos el título de la ventana.
pygame.display.set_caption("Tablero")

# Iteramos hasta que el usuario pulse el botón de salir.
hecho = False

# Lo usamos para establecer cuán rápido se refresca la pantalla.
reloj = pygame.time.Clock()

# Establecemos el fondo de pantalla.
pantalla.fill(NEGRO)
# dibujarTablero()

iter = iter(generaciones)
# -------- Bucle Principal del Programa-----------
while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # El usuario presiona el ratón. Obtiene su posición.
            pos = pygame.mouse.get_pos()
            # Cambia las coordenadas x/y de la pantalla por coordenadas reticulares
            columna = (pos[0]) // (LARGO + MARGEN)
            fila = (pos[1]) // (ALTO + MARGEN)
            # Establece esa ubicación a uno
            if 0 <= fila < n and 0 <= columna < n:  # and (fila, columna) not in juego.elementos: CORREGIR
                # juego.elementos.append((fila, columna))
                pygame.draw.rect(pantalla,
                                 ROJO,
                                 [MARGEN + (MARGEN + LARGO) * columna,
                                  MARGEN + (MARGEN + ALTO) * fila,
                                  LARGO,
                                  ALTO])
                print('Agregado por click')
            print("Click ", pos, "Coordenadas de la retícula: ", fila, columna)

    try:
        generacion = next(iter)
        dibujarTablero(generacion.vivos())
    except StopIteration:
        pass

    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # Limitamos a 10 fotogramas por segundo.
    reloj.tick(30)

# Cerramos la ventana y salimos.
pygame.quit()
