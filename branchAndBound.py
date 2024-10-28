def is_valid_move(x, y, N, visited):
    """
    Verifica si un movimiento a la posición (x, y) es válido.
    """
    return 0 <= x < N and 0 <= y < N and not visited[x][y]

def get_neighbours(x, y, N, visited):
    """
    Obtiene los vecinos válidos de la posición (x, y) aplicando la heurística de Warnsdorff.
    """
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    neighbours = []
    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if is_valid_move(new_x, new_y, N, visited):
            count = sum(1 for m in moves if is_valid_move(new_x + m[0], new_y + m[1], N, visited))
            neighbours.append((new_x, new_y, count))
    return sorted(neighbours, key=lambda x: x[2])

def knight_tour_branch_and_bound(N, path, visited, x, y, move_count):
    """
    Encuentra un recorrido del caballo utilizando branch and bound con la regla de Warnsdorff.
    """
    if move_count == N * N:
        # Si se ha recorrido todo el tablero, se ha encontrado una solución
        return True

    # Obtener vecinos ordenados por la cantidad de movimientos futuros (heurística)
    neighbours = get_neighbours(x, y, N, visited)

    for next_x, next_y, _ in neighbours:
        # Marca el movimiento como visitado y añádelo al camino
        visited[next_x][next_y] = True
        path.append((next_x, next_y))

        # Llama recursivamente para continuar el recorrido
        if knight_tour_branch_and_bound(N, path, visited, next_x, next_y, move_count + 1):
            return True  # Se encontró una solución

        # Retrocede si no se encuentra solución desde esta posición
        visited[next_x][next_y] = False
        path.pop()

    # Poda: Si no se encuentran vecinos válidos, se detiene esta rama
    return False

def find_knight_tour_branch_and_bound(N, start_x, start_y):
    """
    Inicializa y encuentra un recorrido del caballo en un tablero NxN utilizando branch and bound.
    """
    visited = [[False for _ in range(N)] for _ in range(N)]
    path = [(start_x, start_y)]
    visited[start_x][start_y] = True

    if knight_tour_branch_and_bound(N, path, visited, start_x, start_y, 1):
        return path
    else:
        return None  # No se encontró una solución

# Ejemplo de uso
N = 5  # Tamaño del tablero
start_x, start_y = 0, 0  # Posición inicial del caballo

# Encontrar el recorrido del caballo
tour_path = find_knight_tour_branch_and_bound(N, start_x, start_y)

# Imprimir el resultado
if tour_path:
    print("Recorrido del caballo:")
    for move in tour_path:
        print(move)
else:
    print("No se encontró un recorrido válido.")
