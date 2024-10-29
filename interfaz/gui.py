import tkinter as tk
from tkinter import ttk, messagebox
from render import RenderChess
import sys
import os
# Asegúrate de que la ruta de tu módulo sea correcta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from parte2.branchAndBound import encontrar_recorrido_del_caballo_branch_and_bound
def comenzar():
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
        camino_recorrido = encontrar_recorrido_del_caballo_branch_and_bound(tamano_tablero, posicion_x, posicion_y)
        # Imprimir el resultado
        if camino_recorrido:
            resultado = "Recorrido del caballo:\n"
            for movimiento in camino_recorrido:
                resultado += f"{movimiento}\n"
            # Renderizar el tablero
            render = RenderChess(tamano_tablero, camino_recorrido)
            render.render()
    
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
ttk.Label(frame, text="Posición en Y:").grid(row=1, column=0, sticky="w", pady=5)
entry_x = ttk.Entry(frame, width=10, font=("Arial", 11))
entry_x.grid(row=1, column=1, pady=5)
ttk.Label(frame, text="Posición en X:").grid(row=2, column=0, sticky="w", pady=5)
entry_y = ttk.Entry(frame, width=10, font=("Arial", 11))
entry_y.grid(row=2, column=1, pady=5)
# Botón para comenzar
boton_comenzar = ttk.Button(frame, text="Comenzar", command=comenzar)
boton_comenzar.grid(row=3, column=0, columnspan=2, pady=20)
# Ejecutar la aplicación
root.mainloop()