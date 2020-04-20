from Generacion import Generacion
import numpy as np


# Clase iterable
class Game:

    # Crea un tablero de n x n con N elementos iniciales
    # aleatorios. Los elementos son tuplas (x, y).
    def __init__(self, n, N):
        self.n = n
        self.inicio = Generacion(self, None, self.generar_tuplas(N))  # Generacion inicial

    # Esto permite iterar sobre el juego
    # es decir , puede utilizar un para para
    # recorrer las generaciones i.e.:
    # for generacion in Game:
    def __iter__(self):
        self.actual = self.inicio
        return self

    # Devuelve, a partir del elemento actual de la iteración,
    # la siguiente generación en el juego .
    def __next__(self):
        if len(self.actual.vivos()) > 0:
            self.actual = self.actual.siguiente()
            return self.actual
        else:
            raise StopIteration

    # Genera N tuplas aleatorias diferentes
    def generar_tuplas(self, N):
        elementos = []
        count = 0
        while count < N:
            x = (int(np.random.uniform(0, self.n)), int(np.random.uniform(0, self.n)))
            if x not in elementos:
                elementos.append(x)
                count += 1
        return elementos
