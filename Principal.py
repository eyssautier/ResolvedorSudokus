import io

from Sudoku import Sudoku


def llenar_tablero(archivo_entrada):
    matriz = list()
    with open(archivo_entrada) as entrada:
        for linea in entrada:
            linea = linea.strip().replace(" ", "")
            if len(linea) > 0:
                fila = list()
                for x in range(len(linea)):
                    v = linea[x]
                    if v.isnumeric():
                        fila.append(int(v))
                    else:
                        fila.append(None)
                matriz.append(fila)
    return matriz


def grabar_tablero(matriz, archivo_salida):
    with open(archivo_salida, "w") as salida:
        for y in range(len(matriz)):
            imp_fila = ""
            for x in range(len(matriz[y])):
                imp_fila = imp_fila + " " + str(list(matriz[y][x])[0])
                if (x + 1) % 3 == 0:
                    imp_fila = imp_fila + "   "
            salida.write(imp_fila + "\n")
            if (y + 1) % 3 == 0 and y < len(matriz) - 1:
                salida.write("\n")


def principal():
    matriz = llenar_tablero("recursos/entradaSudoku.txt")
    try:
        sudoku = Sudoku(matriz)
        sudoku.generar_resultados()
        if sudoku.matrizFinal is not None:
            grabar_tablero(sudoku.matrizFinal, "recursos/salidaSudoku.txt")
        else:
            with io.open("recursos/salidaSudoku.txt", "w", encoding="utf8") as salida:
                salida.write("Sudoku sin solución...")
    except Exception as err:
        with io.open("recursos/salidaSudoku.txt", "w", encoding="utf8") as salida:
            salida.write("Error al procesor el Sudoku\n{0}".format(err))


if __name__ == "__main__":
    principal()
