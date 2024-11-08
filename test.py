import pygame
import time
import sys

# Configurar Pygame
pygame.init()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Tamaño de la ventana de Pygame (depende del tamaño del tablero)
TAM_CELDA = 60
ANCHO_VENTANA = 5 * TAM_CELDA
ALTO_VENTANA = 5 * TAM_CELDA

# Crear ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Recorrido del Caballo")

# Función para dibujar el tablero
def dibujar_tablero(N, visitado, camino):
    ventana.fill(NEGRO)
    for y in range(N):
        for x in range(N):
            color = BLANCO if (x + y) % 2 == 0 else NEGRO
            pygame.draw.rect(ventana, color, (x * TAM_CELDA, y * TAM_CELDA, TAM_CELDA, TAM_CELDA))
            # Si la casilla está visitada, la pintamos de otro color
            if visitado[y][x]:
                pygame.draw.rect(ventana, VERDE, (x * TAM_CELDA, y * TAM_CELDA, TAM_CELDA, TAM_CELDA))
            # Mostrar el recorrido (camino)
            if (y, x) in camino:
                pygame.draw.circle(ventana, AZUL, (x * TAM_CELDA + TAM_CELDA // 2, y * TAM_CELDA + TAM_CELDA // 2), TAM_CELDA // 4)
    
    # Actualizar la pantalla
    pygame.display.update()

# Función para verificar si un movimiento es válido
def es_movimiento_valido(x, y, N, visitado):
    return 0 <= x < N and 0 <= y < N and not visitado[y][x]

# Función para obtener los vecinos del caballo según la heurística de Warnsdorff
def obtener_vecinos(x, y, N, visitado):
    movimientos = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    vecinos = []
    for movimiento in movimientos:
        nuevo_x, nuevo_y = x + movimiento[0], y + movimiento[1]
        if es_movimiento_valido(nuevo_x, nuevo_y, N, visitado):
            cuenta = sum(1 for m in movimientos if es_movimiento_valido(nuevo_x + m[0], nuevo_y + m[1], N, visitado))
            vecinos.append((nuevo_x, nuevo_y, cuenta))
    return sorted(vecinos, key=lambda x: x[2])

# Función de recorrido del caballo con branch and bound
def recorrido_del_caballo_branch_and_bound(N, camino, visitado, x, y, cuenta_movimientos, movimientos_totales):
    if cuenta_movimientos == N * N:
        return True, movimientos_totales
    
    vecinos = obtener_vecinos(x, y, N, visitado)
    vecinos = vecinos[:2]
    for siguiente_x, siguiente_y, _ in vecinos:
        movimientos_totales += 1
        visitado[siguiente_y][siguiente_x] = True
        camino.append((siguiente_y, siguiente_x))

        # Dibujar en cada paso
        dibujar_tablero(N, visitado, camino)
        #time.sleep(0.01)  # Pausa para visualizar el movimiento
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        encontrado, movimientos_totales = recorrido_del_caballo_branch_and_bound(N, camino, visitado, siguiente_x, siguiente_y, cuenta_movimientos + 1, movimientos_totales)
        if encontrado:
            return camino, movimientos_totales

        visitado[siguiente_y][siguiente_x] = False
        camino.pop()

    return False, movimientos_totales

# Función principal para encontrar el recorrido
def encontrar_recorrido_del_caballo_branch_and_bound(N, inicio_x, inicio_y):
    visitado = [[False for _ in range(N)] for _ in range(N)]
    camino = [(inicio_y, inicio_x)]
    visitado[inicio_y][inicio_x] = True
    movimientos_totales = 1
    
    encontrado, movimientos_totales = recorrido_del_caballo_branch_and_bound(N, camino, visitado, inicio_x, inicio_y, 1, movimientos_totales)
    if encontrado:
        return camino, movimientos_totales
    else:
        return None

# Configuración inicial
N = 7
inicio_x, inicio_y = 2, 2  # Empezar en la esquina superior izquierda

# Ejecutar el algoritmo y mostrar el recorrido
camino, movimientos_totales = encontrar_recorrido_del_caballo_branch_and_bound(N, inicio_x, inicio_y)

# Si se encuentra una solución, mostrar el camino final
if camino:
    print("Recorrido encontrado:", camino)
else:
    print("No se encontró un recorrido válido.")

# Cerrar Pygame
pygame.quit()
