import time
import sys

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
        if es_movimiento_valido(nuevo_x, nuevo_y, N, visitado):
            # Incrementamos movimientos_totales para cada intento de movimiento
            cuenta = sum(1 for m in movimientos if es_movimiento_valido(nuevo_x + m[0], nuevo_y + m[1], N, visitado))
            vecinos.append((nuevo_x, nuevo_y, cuenta))

    # Ordena el array vecinos de menor a mayor
    return sorted(vecinos, key=lambda x: x[2])

def bound(nodosVivos):
    return nodosVivos[:2]

def recorrido_del_caballo_branch_and_bound(N, camino, visitado, x, y, cuenta_movimientos, movimientos_totales):
    """
    Encuentra un recorrido del caballo utilizando branch and bound con la regla de Warnsdorff.
    """
    if cuenta_movimientos == N * N:
        # Si se ha recorrido todo el tablero, se ha encontrado una solución
        return True, movimientos_totales

    # Obtener vecinos ordenados por la cantidad de movimientos futuros (heurística)
    vecinos = obtener_vecinos(x, y, N, visitado)
    
    vecinos = bound(vecinos)
    
    for siguiente_x, siguiente_y, _ in vecinos:
        movimientos_totales += 1
        # Marca el movimiento como visitado y añádelo al camino
        visitado[siguiente_y][siguiente_x] = True
        camino.append((siguiente_y, siguiente_x))

        # Llama recursivamente para continuar el recorrido
        encontrado, movimientos_totales = recorrido_del_caballo_branch_and_bound(N, camino, visitado, siguiente_x, siguiente_y, cuenta_movimientos + 1, movimientos_totales)
        if encontrado:
            return camino, movimientos_totales # Se encontró una solución

        # Retrocede si no se encuentra solución desde esta posición
        visitado[siguiente_y][siguiente_x] = False
        camino.pop()

    # Poda Explicita: Si no se encuentran vecinos válidos, se detiene esta rama
    return False, movimientos_totales # retorna los movimientos que realizo hasta esa rama

def encontrar_recorrido_del_caballo_branch_and_bound(N, inicio_x, inicio_y):
    """
    Inicializa y encuentra un recorrido del caballo en un tablero NxN utilizando branch and bound.
    """
    visitado = [[False for _ in range(N)] for _ in range(N)]
    camino = [(inicio_y, inicio_x)]
    visitado[inicio_y][inicio_x] = True
    movimientos_totales = 1
    
    encontrado, movimientos_totales = recorrido_del_caballo_branch_and_bound(N, camino, visitado, inicio_x, inicio_y, 1, movimientos_totales)
    if encontrado:
        return camino, movimientos_totales
    else:
        return None

'''
movimientos totales no cuenta la pos inicial
'''

def benchmark():
    dim = 10
    for i in range(5, dim + 1):
        print(f"\nProbando dimensión: {i}x{i}")
        for fila in range(i):
            for columna in range(i):
                #Condición para omitir las casillas negras (cuando la suma de las coordenadas no es par)
                if (dim % 2 != 0):
                    if (fila + columna) % 2 != 0:
                        continue  # No probar en casillas negras
                
                start = time.time()
                resultado = encontrar_recorrido_del_caballo_branch_and_bound(i, fila, columna)
                end = time.time()
                
                if resultado:
                    camino, mov_totales = resultado
                    print(f"Posición inicial ({fila}, {columna}) - {mov_totales} movimientos, tiempo: {end - start:.4f} segundos")
                else:
                    print(f"Posición inicial ({fila}, {columna}) - no tiene solución")

#benchmark()