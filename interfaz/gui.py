import tkinter as tk
from tkinter import ttk, messagebox
from render import RenderChess
import sys
import os

# Ajusta el sistema de path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from parte2.branchAndBound import encontrar_recorrido_del_caballo_branch_and_bound
from parte2.algoIterativo import encontrar_recorrido_del_caballo_branch_and_bound_iterativo
from parte1.backtracking import resolver_recorrido_del_caballo, inicializar_tablero

def comenzar_branch_and_bound():
    try:
        # Obtener valores de los campos
        tamano_tablero = int(entry_tamano.get())
        posicion_x = int(entry_x.get())
        posicion_y = int(entry_y.get())
        
        # Validar valores
        if tamano_tablero <= 0:
            raise ValueError("El tamaño del tablero debe ser mayor que 0.")
        if not (0 <= posicion_x < tamano_tablero) or not (0 <= posicion_y < tamano_tablero):
            raise ValueError(f"Las coordenadas deben estar entre 0 y {tamano_tablero - 1}.")
        
        # Encontrar el recorrido del caballo
        camino_recorrido, mov_totales = encontrar_recorrido_del_caballo_branch_and_bound(tamano_tablero, posicion_x, posicion_y)
        print(camino_recorrido[:2])
        # Imprimir el resultado
        if camino_recorrido:
            resultado = "Recorrido del caballo:\n"
            for movimiento in camino_recorrido:
                resultado += f"{movimiento}\n"
            # Renderizar el tablero
            render = RenderChess(tamano_tablero, camino_recorrido)
            render.render()
            print(mov_totales)
        else:
            messagebox.showinfo("Resultado", "No se encontró un recorrido completo.")
    
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")


def comenzar_heuristico_iterativo():
    try:
        # Obtener valores de los campos
        tamano_tablero = int(entry_tamano.get())
        posicion_x = int(entry_x.get())
        posicion_y = int(entry_y.get())
        
        # Validar valores
        if tamano_tablero <= 0:
            raise ValueError("El tamaño del tablero debe ser mayor que 0.")
        if not (0 <= posicion_x < tamano_tablero) or not (0 <= posicion_y < tamano_tablero):
            raise ValueError(f"Las coordenadas deben estar entre 0 y {tamano_tablero - 1}.")
        
        # Encontrar el recorrido del caballo
        camino_recorrido = encontrar_recorrido_del_caballo_branch_and_bound_iterativo(tamano_tablero, posicion_x, posicion_y)
        
        # Imprimir el resultado
        if camino_recorrido:
            # Renderizar el tablero
            render = RenderChess(tamano_tablero, camino_recorrido)
            render.render()
        else:
            messagebox.showinfo("Resultado", "No se encontró un recorrido completo.")
    
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")



def comenzar_backtracking():
    try:
        # Obtener valores de los campos
        tamano_tablero = int(entry_tamano.get())
        posicion_x = int(entry_x.get())
        posicion_y = int(entry_y.get())
        
        # Validar valores
        if tamano_tablero <= 0:
            raise ValueError("El tamaño del tablero debe ser mayor que 0.")
        if not (0 <= posicion_x < tamano_tablero) or not (0 <= posicion_y < tamano_tablero):
            raise ValueError(f"Las coordenadas deben estar entre 0 y {tamano_tablero - 1}.")
        
        # Inicializar tablero
        tablero = inicializar_tablero(tamano_tablero)
        tablero[posicion_x][posicion_y] = 0  # Establecer la posición inicial
        
        # Encontrar el recorrido del caballo
        movimientos_iniciales = [(posicion_x, posicion_y)]  # Lista de movimientos inicial
        _, camino_recorrido = resolver_recorrido_del_caballo(tablero, posicion_x, posicion_y, 1, movimientos_iniciales)
        print(camino_recorrido[:2])
        
        # Imprimir el resultado
        if camino_recorrido:
            resultado = "Recorrido del caballo:\n"
            for fila in tablero:
                resultado += ' '.join(str(celda).rjust(3, ' ') for celda in fila) + "\n"
            # Renderizar el tablero
            render = RenderChess(tamano_tablero, camino_recorrido)  # Aquí pasas los movimientos
            render.render()
        else:
            messagebox.showinfo("Resultado", "No se encontró un recorrido completo.")
    
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")

# Configurar la ventana principal
root = tk.Tk()
root.title("Configuración del Tablero")
root.geometry("400x350")
root.resizable(False, False)

# Estilo
style = ttk.Style(root)
style.configure("TLabel", font=("Arial", 12), padding=5)
style.configure("TEntry", padding=5)
style.configure("TButton", font=("Arial", 12), padding=5)

# Frame para centrar los elementos
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

# Etiquetas y campos de entrada
ttk.Label(frame, text="Tamaño del tablero:").grid(row=0, column=0, sticky="w", pady=5)
entry_tamano = ttk.Entry(frame, width=10, font=("Arial", 11))
entry_tamano.grid(row=0, column=1, pady=5)

ttk.Label(frame, text="Posición en i:").grid(row=1, column=0, sticky="w", pady=5)
entry_x = ttk.Entry(frame, width=10, font=("Arial", 11))
entry_x.grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Posición en j:").grid(row=2, column=0, sticky="w", pady=5)
entry_y = ttk.Entry(frame, width=10, font=("Arial", 11))
entry_y.grid(row=2, column=1, pady=5)

# Botón para comenzar Backtracking básico
boton_backtracking = ttk.Button(frame, text="Probar Backtracking Básico", command=comenzar_backtracking)
boton_backtracking.grid(row=3, column=0, columnspan=2, pady=10)

# Botón para comenzar con Branch and Bound
boton_byb = ttk.Button(frame, text="Probar Branch and Bound", command=comenzar_branch_and_bound)
boton_byb.grid(row=4, column=0, columnspan=2, pady=10)

# heuristico iterativo
boton_byb_iterativo = ttk.Button(frame, text="heuristico iterativo", command=comenzar_heuristico_iterativo)
boton_byb_iterativo.grid(row=5, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
root.mainloop()
