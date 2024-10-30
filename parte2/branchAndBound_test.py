from branchAndBound import encontrar_recorrido_del_caballo_branch_and_bound, movimientos_totales
import time

def run_test():
    N = 3  # Tamaño del tablero NxN
    inicio_x, inicio_y = 0, 0  # Posición inicial del caballo

    # Medir el tiempo de inicio
    tiempo_inicio = time.time()
    
    # Ejecutar el algoritmo para encontrar el recorrido del caballo
    camino = encontrar_recorrido_del_caballo_branch_and_bound(N, inicio_x, inicio_y)
    
    # Medir el tiempo de finalización
    tiempo_fin = time.time()
    
    # Calcular el tiempo total de ejecución
    tiempo_total = tiempo_fin - tiempo_inicio
    
    # Mostrar el resultado
    if camino:
        print("Recorrido del caballo encontrado:")
        for paso, (x, y) in enumerate(camino, 1):
            print(f"Paso {paso}: ({x}, {y})")
    else:
        print("No se encontró un recorrido del caballo para este tablero.")
    
    print(f"\nTiempo de ejecución: {tiempo_total:.4f} segundos")
    print(f"Total de movimientos intentados: {movimientos_totales}")

run_test()