# parte1/backtracking.py
import time
import sys
sys.setrecursionlimit(100000)

def inicializar_tablero(tamano):
    return [[-1 for _ in range(tamano)] for _ in range(tamano)] # llena de -1 una matriz

def es_movimiento_valido(x, y, tablero):
    tamano = len(tablero)
    return 0 <= x < tamano and 0 <= y < tamano and tablero[y][x] == -1

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(str(celda).rjust(3, ' ') for celda in fila))


# Lista para guardar las posiciones que intenta el algoritmo, para luego visualizarlo en pantalla
#posiciones_intentadas = []
posiciones_favorables = []
total_movimientos = 0

def resolver_recorrido_del_caballo(tablero, x, y, cuenta_movimientos, movimientos):
    global total_movimientos
    tamano = len(tablero)
    
    # Si todos los movimientos están hechos
    if cuenta_movimientos == tamano * tamano:
        return True, movimientos  # Regresar el recorrido

    movimientos_caballo = [ # posibles movimientos del caballo
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    for dx, dy in movimientos_caballo:
        nuevo_x, nuevo_y = x + dx, y + dy
        if es_movimiento_valido(nuevo_x, nuevo_y, tablero):
            total_movimientos += 1 # variable para contar la cantidad total de movimientos que realiza el caballo
            posiciones_favorables.append((nuevo_y, nuevo_x))  # Agregar posiciones favorables
            tablero[nuevo_y][nuevo_x] = cuenta_movimientos
            movimientos.append((nuevo_y, nuevo_x))  # Agregar movimiento
            
            # Recursividad
            encontrado, movimientos_resultantes = resolver_recorrido_del_caballo(tablero, nuevo_x, nuevo_y, cuenta_movimientos + 1, movimientos)
            if encontrado:
                return True, movimientos_resultantes  # Retornar cuando se encuentre el recorrido
            
            # Retroceso
            tablero[nuevo_y][nuevo_x] = -1  # Deshacer movimiento
            movimientos.pop()  # Eliminar movimiento si el camino no es válido

    return False, movimientos  # Retornar falso si no hay recorrido


def benchmark():
    dim = 8
    for i in range(dim+1):
        global total_movimientos
        total_movimientos = 0  # Reinicia el conteo para cada nuevo tablero
        tablero = inicializar_tablero(i)
        resultado, _ = resolver_recorrido_del_caballo(tablero, 0, 0, 1, [])
        if resultado:
            print(f'dimensión: {i}x{i}, movimientos realizados: ', total_movimientos)
        else:
            print(f'no se encontro solucion para tablero: {i}x{i}')


#benchmark()