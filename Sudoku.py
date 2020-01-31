import copy


class Sudoku:
    matrizInicial = None
    matrizFinal = None

    def __init__(self, matriz):
        self.matrizInicial = self.__inicializar_matriz(matriz)

    def generar_resultados(self):
        self.matrizFinal = self.__procesar_tablero(self.matrizInicial)

    def __quitar_elemento_horizontal(self, matriz, x, y, v):
        for xd in range(9):
            if xd != x:
                if v in matriz[y][xd]:
                    matriz[y][xd].remove(v)
                    if len(matriz[y][xd]) == 1:
                        self.__setear_valor(matriz, xd, y, list(matriz[y][xd])[0])
                    elif len(matriz[y][xd]) == 0:
                        raise Exception("En la validación horizontal, la celda ({}, {}) quedó vacía...".format(xd + 1, y + 1))

    def __quitar_elemento_vertical(self, matriz, x, y, v):
        for yd in range(9):
            if yd != y:
                if v in matriz[yd][x]:
                    matriz[yd][x].remove(v)
                    if len(matriz[yd][x]) == 1:
                        self.__setear_valor(matriz, x, yd, list(matriz[yd][x])[0])
                    elif len(matriz[yd][x]) == 0:
                        raise Exception("En la validación vertical, la celda ({}, {}) quedó vacía...".format(x + 1, yd + 1))

    def __quitar_elemento_cuadrante(self, matriz, x, y, v):
        cuadrante_x = x // 3
        cuadrante_y = y // 3
        rango_x = range(cuadrante_x * 3, (cuadrante_x + 1) * 3)
        rango_y = range(cuadrante_y * 3, (cuadrante_y + 1) * 3)
        for yd in rango_y:
            for xd in rango_x:
                if yd != y or xd != x:
                    if v in matriz[yd][xd]:
                        matriz[yd][xd].remove(v)
                        if len(matriz[yd][xd]) == 1:
                            self.__setear_valor(matriz, xd, yd, list(matriz[yd][xd])[0])
                        elif len(matriz[yd][xd]) == 0:
                            raise Exception("En la validación por cuadrante, la celda ({}, {}) quedó vacía...".format(xd + 1, yd + 1))

    def __setear_valor(self, matriz, x, y, v):
        matriz[y][x] = {v}
        self.__quitar_elemento_horizontal(matriz, x, y, v)
        self.__quitar_elemento_vertical(matriz, x, y, v)
        self.__quitar_elemento_cuadrante(matriz, x, y, v)

    def __procesar_tablero(self, matriz):
        menor_cantidad = self.__buscar_posicion_menor(matriz)
        if menor_cantidad is not None:
            for valores in matriz[menor_cantidad[1]][menor_cantidad[0]]:
                posible_matriz = copy.deepcopy(matriz)
                try:
                    self.__setear_valor(posible_matriz, menor_cantidad[0], menor_cantidad[1], valores)
                    posible_matriz = self.__procesar_tablero(posible_matriz)
                    if posible_matriz is not None:
                        return posible_matriz
                except Exception:
                    pass
            return None
        else:
            return matriz

    def __inicializar_matriz(self, matriz_entrada):
        if len(matriz_entrada) != 9:
            raise Exception("Las dimensiones de la matriz de entrada no son 9 x 9")

        for y in range(len(matriz_entrada)):
            if len(matriz_entrada[y]) != 9:
                raise Exception("Las dimensiones de la matriz de entrada no son 9 x 9")

        # Se inicializa la matriz con todas las opciones...
        matriz = list()
        for y in range(9):
            fila = list()
            for x in range(9):
                columna = {1, 2, 3, 4, 5, 6, 7, 8, 9}
                fila.append(columna)
            matriz.append(fila)

        # Se setean las opciones conocidas...
        for y in range(len(matriz_entrada)):
            for x in range(len(matriz_entrada[y])):
                if matriz_entrada[y][x] is not None:
                    self.__setear_valor(matriz, x, y, matriz_entrada[y][x])

        return matriz

    def imprimir_matriz_inicial(self):
        Sudoku.imprimir_tablero(self.matrizInicial, "Tablero Entrada")

    @staticmethod
    def __buscar_posicion_menor(matriz):
        menor_cantidad = None
        for x in range(9):
            for y in range(9):
                if len(matriz[y][x]) > 1:
                    if menor_cantidad is None:
                        menor_cantidad = (x, y)
                    elif len(matriz[y][x]) < len(matriz[menor_cantidad[1]][menor_cantidad[0]]):
                        menor_cantidad = (x, y)
        return menor_cantidad

    @staticmethod
    def imprimir_tablero(matriz, texto):
        print(texto)
        for y in range(len(matriz)):
            imp_fila = ""
            for x in range(len(matriz[y])):
                imp_fila = imp_fila + " " + str(matriz[y][x]).ljust(30)
            print(imp_fila)
        print("")
