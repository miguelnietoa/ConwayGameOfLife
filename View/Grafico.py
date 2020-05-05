import os
import numpy as np
import pygame
import thorpy
from matplotlib import pyplot as plt
from View import Menu
from Model.Game import Game


def start():
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pantalla = pygame.display.set_mode([850, 400])
    pygame.display.set_caption('Análisis gráfico - Juego de la Vida de Conway')
    reloj = pygame.time.Clock()
    # Valores por defecto
    n = 10
    N = 30
    m = 15

    pantalla.fill((0, 0, 0))

    def graficar():
        if input_n.get_value().isdigit() and input_N.get_value().isdigit() \
                and input_m.get_value().isdigit():
            n = int(input_n.get_value())
            N = int(input_N.get_value())
            m = int(input_m.get_value())
            if n > 1 and N < n * n and m > 1:
                if n <= 300:
                    num_gens = np.arange(1, m + 1)
                    num_vivos = np.zeros(m, dtype=int)
                    num_nacim = np.zeros(m, dtype=int)
                    num_muertes = np.zeros(m, dtype=int)

                    juego = Game(n, N)
                    iterador = iter(juego)
                    num_vivos[0] = len(juego.inicio.vivos())
                    num_nacim[0] = len(juego.inicio.nacimientos())
                    num_muertes[0] = len(juego.inicio.muertes())
                    k = 1
                    while k < m:
                        try:
                            generacion = next(iterador)
                            num_vivos[k] = len(generacion.vivos())
                            num_nacim[k] = len(generacion.nacimientos())
                            num_muertes[k] = len(generacion.muertes())
                        except StopIteration:
                            break
                        k += 1
                    plt.style.use('fivethirtyeight')
                    plt.plot(num_gens, num_vivos, color='g', label='Vivos')
                    plt.plot(num_gens, num_nacim, color='y', label='Nacimientos')
                    plt.plot(num_gens, num_muertes, color='r', label='Muertes')
                    plt.xlabel('Número de generaciones')
                    plt.ylabel('Frecuencia')
                    plt.title('Análisis del Juego de la Vida por generación')
                    plt.legend()
                    plt.tight_layout()
                    plt.show()
                else:
                    thorpy.launch_blocking_alert(title='Error',
                                                 text='¡Lo sentimos! El tamaño del tablero no puede ser mayor a 300.',
                                                 parent=None)
            else:
                thorpy.launch_blocking_alert(title='Error',
                                             text='Los valores intruducidos deben ser positivos mayores a 1. '
                                                  'Además, el número de células iniciales (N) debe ser menor a n^2.',
                                             parent=None)
        else:
            thorpy.launch_blocking_alert(title='Error',
                                         text='Los valores introducidos deben ser numéricos.',
                                         parent=None)

    # ThorPy elements
    text = thorpy.make_text('Digite los valores de entrada:')
    input_n = thorpy.Inserter(name='Tamaño de tablero (n):       ', value=str(n))
    input_N = thorpy.Inserter(name='Núm. células iniciales (N):   ', value=str(N))
    input_m = thorpy.Inserter(name='Núm. de generaciones (m):', value=str(m))
    button = thorpy.make_button('Ver gráfico', func=graficar)
    box = thorpy.Box(elements=[text, input_n, input_N, input_m, button])
    # we regroup all elements on a menu, even if we do not launch the menu
    menu = thorpy.Menu(box)
    # important : set the screen as surface for all elements
    for element in menu.get_population():
        element.surface = pantalla
    # use the elements normally...
    box.set_center((425, 200))
    box.blit()
    box.update()

    pygame.display.flip()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            menu.react(event)  # the menu automatically integrate your elements

        pantalla.fill((0, 0, 0))

        box.blit()
        box.update()

        # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
        pygame.display.flip()

        # Limitamos a 60 fotogramas por segundo.
        reloj.tick(60)
    pygame.quit()
    Menu.start()
