import time
import sys


# Variable global para contar todos los intentos de movimiento
movimientos_totales = 0

sys.setrecursionlimit(100000)

def es_movimiento_valido(x, y, N, visitado):
    """
    Verifica si un movimiento a la posición (x, y) es válido.
    """
    return 0 <= x < N and 0 <= y < N and not visitado[y][x]

def obtener_vecinos(x, y, N, visitado):
    """
    Obtiene los vecinos válidos de la posición (x, y) aplicando la heurística de Warnsdorff.
    """
    movimientos = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    vecinos = []
    for movimiento in movimientos:
        nuevo_x, nuevo_y = x + movimiento[0], y + movimiento[1]
        # Incrementamos movimientos_totales para cada intento de movimiento
        global movimientos_totales
        if es_movimiento_valido(nuevo_x, nuevo_y, N, visitado):
            movimientos_totales += 1
            cuenta = sum(1 for m in movimientos if es_movimiento_valido(nuevo_x + m[0], nuevo_y + m[1], N, visitado))
            vecinos.append((nuevo_x, nuevo_y, cuenta))
    
    # Ordena el array vecinos de menor a mayor
    return sorted(vecinos, key=lambda x: x[2])

def recorrido_del_caballo_branch_and_bound(N, camino, visitado, x, y, cuenta_movimientos):
    """
    Encuentra un recorrido del caballo utilizando branch and bound con la regla de Warnsdorff.
    """
    if cuenta_movimientos == N * N:
        # Si se ha recorrido todo el tablero, se ha encontrado una solución
        return True

    # Obtener vecinos ordenados por la cantidad de movimientos futuros (heurística)
    vecinos = obtener_vecinos(x, y, N, visitado)

    for siguiente_x, siguiente_y, _ in vecinos:
        # Marca el movimiento como visitado y añádelo al camino
        visitado[siguiente_y][siguiente_x] = True
        camino.append((siguiente_y, siguiente_x))

        # Llama recursivamente para continuar el recorrido
        if recorrido_del_caballo_branch_and_bound(N, camino, visitado, siguiente_x, siguiente_y, cuenta_movimientos + 1):
            return True  # Se encontró una solución

        # Retrocede si no se encuentra solución desde esta posición
        visitado[siguiente_y][siguiente_x] = False
        camino.pop()

    # Poda: Si no se encuentran vecinos válidos, se detiene esta rama
    return False

def encontrar_recorrido_del_caballo_branch_and_bound(N, inicio_x, inicio_y):
    """
    Inicializa y encuentra un recorrido del caballo en un tablero NxN utilizando branch and bound.
    """
    global movimientos_totales
    movimientos_totales = 0  # Reiniciar el contador para cada ejecución

    visitado = [[False for _ in range(N)] for _ in range(N)]
    camino = [(inicio_y, inicio_x)]
    visitado[inicio_y][inicio_x] = True
    
    if recorrido_del_caballo_branch_and_bound(N, camino, visitado, inicio_x, inicio_y, 1):
        return camino, movimientos_totales
    else:
        return None  # No se encontró una solución