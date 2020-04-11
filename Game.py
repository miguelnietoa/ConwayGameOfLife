from Generacion import Generacion
import random as rnd


# Clase iterable
class Game:

    # Crea un tablero de n x n con N elementos iniciales
    # aleatorios. Los elementos son tuplas (x, y).
    def __init__(self, n, N):
        self.elementos = []
        self.n = n
        self.generar_tuplas(N)
        self.inicio = Generacion(self, None, self.elementos)  # Generacion inicial

    # Esto permite iterar sobre el juego
    # es decir , puede utilizar un para para
    # recorrer las generaciones i.e.:
    # for generacion in Game :
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

    def generar_tuplas(self, N):
        count = 0
        while count < N:
            x = (rnd.randint(0, self.n - 1), rnd.randint(0, self.n - 1))
            if x not in self.elementos:
                self.elementos.append(x)
                count += 1
