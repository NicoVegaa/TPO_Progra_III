import pygame
import time
import os

class RenderChess:
    pantalla_ancho = 640
    pantalla_alto = 640
    screen = None
    
    # lista de recorrido
    path = []
    # Tamaño del tablero
    columnas = 0
    filas = 0
    cuadrante = 0
    tablero = 0
    movimientos = []
    # Colores para las casillas
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    PATH_COLOR = (255, 0, 0)  # Color para el recorrido
    # Cargar la imagen del caballo
    knight_image = None
    
    def __init__(self, tablero, movimientos):
        self.movimientos = movimientos
        self.tablero = tablero
        self.filas = tablero
        self.columnas = self.filas
        self.cuadrante = self.pantalla_ancho // self.columnas
    
    # Función para dibujar el tablero
    def __draw_board(self):
        for row in range(self.filas):
            for col in range(self.columnas):
                color = self.WHITE if (row + col) % 2 == 0 else self.BLACK
                pygame.draw.rect(self.screen, color, (col * self.cuadrante, row * self.cuadrante, self.cuadrante, self.cuadrante))
    
    # Función para dibujar el recorrido con líneas y números
    def __draw_path(self):
        # Ajuste de tamaño de fuente en función del tamaño de cada cuadrante
        font_size = max(12, self.cuadrante // 2)  # Tamaño mínimo de 12 para que el texto sea legible en tableros pequeños
        font = pygame.font.Font(None, font_size)
        
        # Dibujar los puntos del recorrido y las líneas de conexión
        for counter, (col, row) in enumerate(self.path):  # Cambiado el orden de (row, col) a (col, row)
            # Dibujar un círculo en cada punto del recorrido
            pygame.draw.circle(self.screen, self.PATH_COLOR, (col * self.cuadrante + self.cuadrante // 2, row * self.cuadrante + self.cuadrante // 2), self.cuadrante // 4)
            
            # Dibujar una línea desde el paso anterior al actual
            if counter > 0:
                prev_col, prev_row = self.path[counter - 1]
                pygame.draw.line(
                    self.screen,
                    self.PATH_COLOR,
                    (prev_col * self.cuadrante + self.cuadrante // 2, prev_row * self.cuadrante + self.cuadrante // 2),
                    (col * self.cuadrante + self.cuadrante // 2, row * self.cuadrante + self.cuadrante // 2),
                    3  # Grosor de la línea
                )
        
        # Dibujar los números después de las líneas para que se vean en la parte superior
        for counter, (col, row) in enumerate(self.path):
            text_surface = font.render(str(counter + 1), True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(col * self.cuadrante + self.cuadrante // 2, row * self.cuadrante + self.cuadrante // 2))
            self.screen.blit(text_surface, text_rect)
    
    def render(self):
        pygame.init()
        image_path = os.path.join(os.path.dirname(__file__), "img", "wn.png")
        self.knight_image = pygame.image.load(image_path)
        self.knight_image = pygame.transform.scale(self.knight_image, (self.cuadrante, self.cuadrante))  # Escalar la imagen
        self.screen = pygame.display.set_mode((self.pantalla_ancho, self.pantalla_alto))
        pygame.display.set_caption('Chess Board')
        
        # Inicializar la posición del caballo
        current_move_index = 0
        knight_col, knight_row = self.movimientos[current_move_index]  # Cambiado el orden a (columna, fila)
        
        # Lista para almacenar el recorrido
        self.path = [(knight_col, knight_row)]
        
        # Bucle principal
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Dibujar el tablero
            self.__draw_board()
            # Dibujar el recorrido con líneas y números
            self.__draw_path()
            # Calcular la posición del caballo en píxeles
            knight_x = knight_col * self.cuadrante
            knight_y = knight_row * self.cuadrante
            # Dibujar el caballo en la nueva posición
            self.screen.blit(self.knight_image, (knight_x, knight_y))
            # Actualizar la pantalla
            pygame.display.flip()
            # Esperar un poco antes de mover al siguiente punto
            time.sleep(0.1)  # Ajusta el tiempo para la velocidad de movimiento
            # Actualizar al siguiente movimiento
            current_move_index += 1
            if current_move_index < len(self.movimientos):
                knight_col, knight_row = self.movimientos[current_move_index]  # Cambiado el orden a (columna, fila)
                self.path.append((knight_col, knight_row))  # Agregar la nueva posición al recorrido
            else:
                running = False  # Terminar si no hay más movimientos
        
        # Salir de pygame
        pygame.quit()
