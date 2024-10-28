from renderChess.render import RenderChess

def initialize_board(size):
    return [[-1 for _ in range(size)] for _ in range(size)]

def is_valid_move(x, y, board):
    size = len(board)
    return 0 <= x < size and 0 <= y < size and board[x][y] == -1

def print_board(board):
    size = len(board)
    for row in board:
        print(' '.join(str(cell).rjust(3, ' ') for cell in row))


# lista para guardar las posiciones que intenta el algoritmo, para luego visualizarlo en la pantalla
attempted_positions = []
posiciones_favorables = []

def solve_knights_tour(board, x, y, move_count):
    size = len(board)
    
    if move_count == size * size:
        return True
    

    knight_moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    for dx, dy in knight_moves:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(new_x, new_y, board):
            # registra cada intento de posicion
            attempted_positions.append((new_x, new_y))
            board[new_x][new_y] = move_count
            
            if solve_knights_tour(board, new_x, new_y, move_count + 1):
                posiciones_favorables.append((new_x, new_y))
                return True
            
            board[new_x][new_y] = -1  # Backtrack
    return False

def main():
    size = 5
    board = initialize_board(size)
    start_x, start_y = 0, 0
    board[start_x][start_y] = 0

    if solve_knights_tour(board, start_x, start_y, 1):
        print("Solution found!")
        print_board(board)
        movimientos_optimos = posiciones_favorables

        if (size == 5):
            # solo tenemos foto de un tablero de 5 x 5 
            # la idea es que no sea un png sino que se genere dinamicamente
            render = RenderChess(size, movimientos_optimos)
            render.render()
        else:
            print(f"no hay foto para tablero de {size} posiciones")
            for pos in posiciones_favorables:
                print(f"({pos[0]}, {pos[1]})")
    else:
        print("No solution exists.")
    
    # Imprimir las posiciones intentadas
    #for pos in attempted_positions:
    #    print(f"({pos[0]}, {pos[1]})")

if __name__ == "__main__":
    main()
