import pygame
import thorpy
import os
from Game import Game


def dibujar_tablero(elementos):
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


def empezar_onclick():
    if input_n.get_value().isdigit() and input_N.get_value().isdigit():
        n = int(input_n.get_value())
        N = int(input_N.get_value())
        if n > 1 and N < n * n:
            if n <= 300:
                pass
            else:
                thorpy.launch_blocking_alert(title='Error',
                                             text='¡Lo sentimos! El tamaño del tablero no puede ser mayor a 300.',
                                             parent=None)
        else:
            thorpy.launch_blocking_alert(title='Error',
                                         text='Los valores intruducidos deben ser positivos mayores a 1.'
                                              ' Además, el número de células iniciales (N) debe ser menor a n^2.',
                                         parent=None)
    else:
        thorpy.launch_blocking_alert(title='Error',
                                     text='Los valores introducidos deben ser numéricos.',
                                     parent=None)


# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Establecemos un tamaño del tablero n*n (max = 300)
n = 10
# Establecemos un número de células iniciales
N = 30

# Establecemos el LARGO y ALTO de la pantalla
DIMENSION_VENTANA = [900, 601]

# Establecemos el margen entre las celdas.
MARGEN = 1

# Establecemos el LARGO y ALTO de cada celda de la retícula.
LARGO = ALTO = (DIMENSION_VENTANA[1] - (n + 1)) // n
print(n * LARGO + (n + 1) * MARGEN)

# Se actualiza la dimension de la ventana a la necesaria.
DIMENSION_VENTANA = [900, n * LARGO + (n + 1) * MARGEN]

generaciones = Game(n, N)

# Inicializamos pygame
pygame.init()

# Centramos la ventana
os.environ['SDL_VIDEO_CENTERED'] = '1'

pantalla = pygame.display.set_mode(DIMENSION_VENTANA)

# Establecemos el título de la ventana.
pygame.display.set_caption('Juego de la vida de Conway')

# Iteramos hasta que el usuario pulse el botón de salir.
hecho = False

# Lo usamos para establecer cuán rápido se refresca la pantalla.
reloj = pygame.time.Clock()

# Establecemos el fondo de pantalla.
pantalla.fill(NEGRO)

# Creamos imagen (convert_alpha: fondo transparente)
pause_play = pygame.image.load('img/play.png').convert_alpha()
rect_pause_play = pantalla.blit(pause_play, (650, 260))
nextt = pygame.image.load('img/next.png').convert_alpha()
rect_next = pantalla.blit(nextt, (700, 260))

is_paused = True

# ThorPy elements
text = thorpy.make_text('Digite los valores de entrada:')
input_n = thorpy.Inserter(name='Tamaño de tablero (n):     ', value=str(n))
input_N = thorpy.Inserter(name='Núm. células iniciales (N): ', value=str(N))
button = thorpy.make_button('Empezar', func=empezar_onclick)
box = thorpy.Box(elements=[text, input_n, input_N, button])
# we regroup all elements on a menu, even if we do not launch the menu
menu = thorpy.Menu(box)
# important : set the screen as surface for all elements
for element in menu.get_population():
    element.surface = pantalla
# use the elements normally...
box.set_topleft((620, 40))
box.blit()
box.update()

iterator = iter(generaciones)

try:
    generacion = next(iterator)
    dibujar_tablero(generacion.vivos())
except StopIteration:
    pass

pygame.display.flip()

# -------- Bucle Principal del Programa-----------
while not hecho:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hecho = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # El usuario presiona el ratón. Se obtiene su posición.
            pos = pygame.mouse.get_pos()
            if rect_pause_play.collidepoint(pos):
                if is_paused:
                    pause_play = pygame.image.load('img/pause.png').convert_alpha()
                else:
                    pause_play = pygame.image.load('img/play.png').convert_alpha()
                    pause_play = pygame.image.load('img/play.png').convert_alpha()
                is_paused = not is_paused
            elif rect_next.collidepoint(pos):
                pass

        menu.react(event)  # the menu automatically integrate your elements

    pantalla.fill(NEGRO)

    if not is_paused:
        try:
            generacion = next(iterator)
        except StopIteration:
            pass

    dibujar_tablero(generacion.vivos())

    rect_pause_play = pantalla.blit(pause_play, (650, 260))
    rect_next = pantalla.blit(nextt, (700, 260))

    box.blit()
    box.update()

    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # Limitamos a 10 fotogramas por segundo.
    reloj.tick(10)

# Cerramos la ventana y salimos.
pygame.quit()
