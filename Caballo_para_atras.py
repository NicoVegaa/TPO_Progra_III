from collections import deque

def is_valid_move(x, y, N, visited):
    return 0 <= x < N and 0 <= y < N and not visited[x][y]

def get_neighbours(x, y, N, visited):
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    neighbours = []
    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if is_valid_move(new_x, new_y, N, visited):
            count = sum(1 for m in moves if is_valid_move(new_x + m[0], new_y + m[1], N, visited))
            neighbours.append((new_x, new_y, count))
    return sorted(neighbours, key=lambda x: x[2])

def knight_tour(N, start_x, start_y):
    visited = [[False for _ in range(N)] for _ in range(N)]
    path = [(start_x, start_y)]
    visited[start_x][start_y] = True

    def backtrack():
        if len(path) == N * N:  # Todos los movimientos están hechos
            return True
        
        current_x, current_y = path[-1]
        neighbours = get_neighbours(current_x, current_y, N, visited)

        for next_x, next_y, _ in neighbours:
            # Realiza el movimiento
            path.append((next_x, next_y))
            visited[next_x][next_y] = True
            
            # Llama recursivamente a backtrack
            if backtrack():
                return True
            
            # Si no se encuentra solución, retrocede
            path.pop()
            visited[next_x][next_y] = False
        
        return False

    if backtrack():
        return path
    else:
        return None

# Ejemplo de uso
N = 4  # Tamaño del tablero
start_x, start_y = 0, 0  # Posición inicial del caballo

# Encontrar el recorrido del caballo
tour_path = knight_tour(N, start_x, start_y)

# Imprimir el resultado
if tour_path:
    print("Recorrido del caballo:")
    for move in tour_path:
        print(move)
else:
    print("No se encontró un recorrido válido.")
