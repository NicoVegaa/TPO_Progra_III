
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from renderChess.render import RenderChess

def es_movimiento_valido(x, y, N, visitado):
    """
    Verifica si un movimiento a la posición (x, y) es válido.
    """
    return 0 <= x < N and 0 <= y < N and not visitado[x][y]

def obtener_vecinos(x, y, N, visitado):
    """
    Obtiene los vecinos válidos de la posición (x, y) aplicando la heurística de Warnsdorff.
    """
    movimientos = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    vecinos = []
    for movimiento in movimientos:
        nuevo_x, nuevo_y = x + movimiento[0], y + movimiento[1]
        if es_movimiento_valido(nuevo_x, nuevo_y, N, visitado):
            cuenta = sum(1 for m in movimientos if es_movimiento_valido(nuevo_x + m[0], nuevo_y + m[1], N, visitado))
            vecinos.append((nuevo_x, nuevo_y, cuenta))
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
        visitado[siguiente_x][siguiente_y] = True
        camino.append((siguiente_x, siguiente_y))

        # Llama recursivamente para continuar el recorrido
        if recorrido_del_caballo_branch_and_bound(N, camino, visitado, siguiente_x, siguiente_y, cuenta_movimientos + 1):
            return True  # Se encontró una solución

        # Retrocede si no se encuentra solución desde esta posición
        visitado[siguiente_x][siguiente_y] = False
        camino.pop()

    # Poda: Si no se encuentran vecinos válidos, se detiene esta rama
    return False

def encontrar_recorrido_del_caballo_branch_and_bound(N, inicio_x, inicio_y):
    """
    Inicializa y encuentra un recorrido del caballo en un tablero NxN utilizando branch and bound.
    """
    visitado = [[False for _ in range(N)] for _ in range(N)]
    camino = [(inicio_x, inicio_y)]
    visitado[inicio_x][inicio_y] = True

    if recorrido_del_caballo_branch_and_bound(N, camino, visitado, inicio_x, inicio_y, 1):
        return camino
    else:
        return None  # No se encontró una solución

# Ejemplo de uso
N = 10  # Tamaño del tablero
inicio_x, inicio_y = 4, 1  # Posición inicial del caballo

# Encontrar el recorrido del caballo
camino_recorrido = encontrar_recorrido_del_caballo_branch_and_bound(N, inicio_x, inicio_y)

# Imprimir el resultado
if camino_recorrido:
    print("Recorrido del caballo:")
    render = RenderChess(N, camino_recorrido)
    render.render()
    for movimiento in camino_recorrido:
        print(movimiento)
else:
    print("No se encontró un recorrido válido.")

