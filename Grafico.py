from matplotlib import pyplot as plt
import numpy as np

from Game import Game


def graficar():
    # -----------------
    n = 10
    N = 30
    m = 50
    juego = Game(n, N)
    iterador = iter(juego)

    num_vivos = []
    num_nacim = []
    num_muertes = []

    generacion = None
    count = 0

    while count < m:
        try:
            generacion = next(iterador)
            num_vivos.append(len(generacion.vivos()))
            num_nacim.append(len(generacion.nacimientos()))
            num_muertes.append(len(generacion.muertes()))
        except StopIteration:
            num_vivos.append(0)
            num_muertes.append(0)
            num_nacim.append(0)

            print('se acabaron generaciones')
            break
        count += 1

    if count == m:
        print('Todo bien, se muestran', m, 'generaciones.')
        generaciones = np.arange(1, count + 1)
    else:
        print('Solo se mostrarán', count, 'generaciones.')
        generaciones = np.arange(1, count + 2)

    print(len(generaciones), len(num_vivos), len(num_nacim), len(num_muertes))

    plt.plot(generaciones, num_vivos, color='g', label='Vivos')
    plt.plot(generaciones, num_nacim, color='y', label='Nacimientos')
    plt.plot(generaciones, num_muertes, color='r', label='Muertes')

    # ---------------
    plt.xlabel('Generaciones')
    plt.ylabel('Frecuencia')
    plt.title('Análisis del Juego de la Vida por generación')

    plt.legend()
    plt.tight_layout()
    plt.show()
