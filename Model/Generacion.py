import itertools


class Generacion:

    # Recibe como parámetros la generación anterior, y
    # lista de elementos ( tuplas ) que estarán en esta generación.
    def __init__(self, game, anterior, elementos):
        self.game = game
        self.anterior = anterior
        self.elementos = elementos

    # Lista ’list ’ con los elementos actualmente vivos .
    def vivos(self):
        return self.elementos

    # Lista ’list ’ con los elementos que, a partir del estado actual,
    # serán nuevos en la próxima generación
    def nacimientos(self):
        vecinos = self.__calc_vecinos__()

        # Hallamos las tuplas que están en vecinos pero no en los elementos actualmente vivos
        probables = list(
            set(vecinos.keys()).difference(set(self.elementos))
        )
        nacimientos = [tupla for tupla in probables if vecinos[tupla] == 3]
        del probables, vecinos
        return nacimientos

    # Lista ’list ’ con los elementos que, a partir del estado actual,
    # no estarán en la próxima generación, pero que sí están en la actual.
    def muertes(self):
        vecinos = self.__calc_vecinos__()
        muertes = [tupla for tupla in self.elementos if vecinos[tupla] <= 1 or vecinos[tupla] >= 4]
        del vecinos
        return muertes

    # Devuelve la generación siguiente, conformada por
    # los elementos que estarán presentes
    def siguiente(self):
        vecinos = self.__calc_vecinos__()
        elementos = [tupla for tupla in vecinos
                     if vecinos[tupla] == 3 or (tupla in self.elementos and vecinos[tupla] == 2)]
        del vecinos
        return Generacion(self.game, self, elementos)

    def __calc_vecinos__(self):
        # Generamos las tuplas que están alrededor del punto (0,0).
        # set: transforma objeto iterable a conjunto
        # (un conjunto en Python no tiene repetidos).
        around = list(
            set(itertools.permutations([-1, -1, 1, 1, 0], 2))
        )
        # Creamos un diccionario y añadimos los elementos vivos y sus vecinos,
        # aquí se guardará el número de vecinos de las tuplas necesarias
        # {(x1, y1): k1, (x2, y2): k2, ...}
        vecinos = dict.fromkeys(self.elementos, 0)
        # Calculamos los vecinos
        for x, y in self.elementos:
            for a, b in around:
                if 0 <= x + a < self.game.n and 0 <= y + b < self.game.n:
                    if (x + a, y + b) in vecinos:
                        vecinos[(x + a, y + b)] += 1
                    else:
                        vecinos[(x + a, y + b)] = 1
        return vecinos
