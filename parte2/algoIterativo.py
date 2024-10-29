def es_movimiento_valido(x, y, N, visitado):
    return 0 <= x < N and 0 <= y < N and not visitado[x][y]

def obtener_vecinos(x, y, N, visitado):
    movimientos = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    vecinos = []
    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if es_movimiento_valido(nx, ny, N, visitado):
            # Cuenta cuántos movimientos válidos hay desde el nuevo movimiento
            count = sum(1 for mx, my in movimientos if es_movimiento_valido(nx + mx, ny + my, N, visitado))
            vecinos.append((nx, ny, count))
    # Ordena vecinos según la cantidad de opciones futuras (heurística de Warnsdorff)
    vecinos.sort(key=lambda v: v[2])
    return vecinos

def encontrar_recorrido_del_caballo_branch_and_bound_iterativo(N, inicio_x, inicio_y):
    # Matriz para marcar las posiciones visitadas
    visitado = [[False] * N for _ in range(N)]
    recorrido = [(inicio_x, inicio_y)]
    visitado[inicio_x][inicio_y] = True

    x, y = inicio_x, inicio_y
    for _ in range(N * N - 1):  # El caballo debe realizar N^2 - 1 movimientos
        vecinos = obtener_vecinos(x, y, N, visitado)
        if not vecinos:
            return None  # No se encontró un camino completo
        # Selecciona el vecino con la menor cantidad de movimientos futuros
        nx, ny, _ = vecinos[0]
        visitado[nx][ny] = True
        recorrido.append((nx, ny))
        x, y = nx, ny

    return recorrido