# parte1/backtracking.py
import time


def inicializar_tablero(tamano):
    return [[-1 for _ in range(tamano)] for _ in range(tamano)]

def es_movimiento_valido(x, y, tablero):
    tamano = len(tablero)
    return 0 <= x < tamano and 0 <= y < tamano and tablero[x][y] == -1

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(str(celda).rjust(3, ' ') for celda in fila))


# Lista para guardar las posiciones que intenta el algoritmo, para luego visualizarlo en pantalla
#posiciones_intentadas = []
posiciones_favorables = []
total_movimientos = 0

def resolver_recorrido_del_caballo(tablero, x, y, cuenta_movimientos):
    global total_movimientos
    tamano = len(tablero)
    
    if cuenta_movimientos == tamano * tamano:
        return True
    
    movimientos_caballo = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    #posiciones_intentadas.append((x, y)) # todas las posiciones
    
    for dx, dy in movimientos_caballo:
        total_movimientos += 1
        nuevo_x, nuevo_y = x + dx, y + dy
        if es_movimiento_valido(nuevo_x, nuevo_y, tablero):
            posiciones_favorables.append((nuevo_x, nuevo_y))  # agrego posiciones favorables acá por la recursividad
            tablero[nuevo_x][nuevo_y] = cuenta_movimientos
            
            if resolver_recorrido_del_caballo(tablero, nuevo_x, nuevo_y, cuenta_movimientos + 1):
                return True
            
            tablero[nuevo_x][nuevo_y] = -1  # Retroceso
            posiciones_favorables.pop()  # Eliminar si el camino no es válido
    return False