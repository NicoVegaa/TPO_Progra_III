def es_seguro(x, y, tablero):
    return 0 <= x < len(tablero) and 0 <= y < len(tablero) and tablero[x][y] == -1 #Indica si la posicion x e y no se excede de la capacidad del tablero y si la posicion no está visitada

def imprimir_solucion(tablero):
    for fila in tablero:
        print(" ".join(f"{celda:2}" for celda in fila))
    print() #Imprime la solucion una vez que el caballo recorrio todas las casillas sin repetir ninguna

def resolver_caballo_tour(n):
    # Movimientos posibles del caballo
    mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
    mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Inicializar el tablero
    tablero = [[-1 for _ in range(n)] for _ in range(n)] #Crea una matriz n*n con valores de -1 de forma parcial que luego seran reemplazados por el numero de pasos del caballo

    # Comenzar desde la posición inicial
    tablero[0][0] = 0  # El caballo comienza en la posición (0, 0)

    # Comenzar el recorrido
    if not resolver_caballo_tour_util(tablero, 0, 0, 1, mov_x, mov_y, n):
        print("No hay solución")
    else:
        imprimir_solucion(tablero)

def resolver_caballo_tour_util(tablero, x_act, y_act, num_mov, mov_x, mov_y, n):
    if num_mov == n * n:
        return True

    # Probar todos los movimientos posibles del caballo
    for i in range(8):
        sig_x = x_act + mov_x[i]
        sig_y = y_act + mov_y[i]
        if es_seguro(sig_x, sig_y, tablero):
            tablero[sig_x][sig_y] = num_mov  # Asignar el número de movimiento
            if resolver_caballo_tour_util(tablero, sig_x, sig_y, num_mov + 1, mov_x, mov_y, n): #Llama de forma recursiva a la funcion con la nueva posicion
                return True
            # Retroceso (backtrack)
            tablero[sig_x][sig_y] = -1

    return False

# Ejemplo de uso
n = 5  # Tamaño del tablero
resolver_caballo_tour(n)
