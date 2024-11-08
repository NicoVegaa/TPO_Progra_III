import pygame
import time
import os

class RenderChess:
    pantalla_ancho = 680  # Incrementamos el ancho para incluir el área lateral
    pantalla_alto = 680   # Incrementamos el alto para incluir el área superior
    header_height = 40    # Altura del encabezado para mostrar los números de columnas
    side_width = 40       # Ancho para el área lateral con los números de filas
    screen = None
    
    # Lista de recorrido
    path = []
    # Tamaño del tablero
    columnas = 0
    filas = 0
    cuadrante = 0
    tablero = 0
    movimientos = []
    # Colores para las casillas y texto
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    PATH_COLOR = (255, 0, 0)  # Color para el recorrido
    TEXT_COLOR = (255, 255, 255)  # Color del texto de posición en el encabezado
    # Cargar la imagen del caballo
    knight_image = None
    
    def __init__(self, tablero, movimientos):
        self.movimientos = movimientos
        self.tablero = tablero
        self.filas = tablero
        self.columnas = self.filas
        self.cuadrante = (self.pantalla_ancho - self.side_width) // self.columnas
    
    # Función para dibujar el tablero
    def __draw_board(self):
        for row in range(self.filas):
            for col in range(self.columnas):
                color = self.WHITE if (row + col) % 2 == 0 else self.BLACK
                pygame.draw.rect(self.screen, color, (self.side_width + col * self.cuadrante, self.header_height + row * self.cuadrante, self.cuadrante, self.cuadrante))
    
    # Función para dibujar encabezado y costado con números de posición
    def __draw_header_and_side(self):
        # Ajustar el tamaño de la fuente en función del tamaño del cuadrante
        font_size = max(12, self.cuadrante // 3)
        font = pygame.font.Font(None, font_size)  # Tamaño de fuente para los números

        # Dibujar números de columnas en el encabezado
        for col in range(self.columnas):
            text_surface = font.render(str(col), True, self.TEXT_COLOR)
            text_rect = text_surface.get_rect(center=(self.side_width + col * self.cuadrante + self.cuadrante // 2, self.header_height // 2 + 10))
            self.screen.blit(text_surface, text_rect)

        # Dibujar números de filas en el costado
        for row in range(self.filas):
            text_surface = font.render(str(row), True, self.TEXT_COLOR)
            text_rect = text_surface.get_rect(center=(self.side_width // 2 - 10, self.header_height + row * self.cuadrante + self.cuadrante // 2))
            self.screen.blit(text_surface, text_rect)
    
    # Función para dibujar el recorrido con líneas y números
    def __draw_path(self):
        font_size = max(12, self.cuadrante // 2)
        font = pygame.font.Font(None, font_size)
        
        for counter, (row, col) in enumerate(self.path):
            pygame.draw.circle(self.screen, self.PATH_COLOR, (self.side_width + col * self.cuadrante + self.cuadrante // 2, self.header_height + row * self.cuadrante + self.cuadrante // 2), self.cuadrante // 4)
            if counter > 0:
                prev_row, prev_col = self.path[counter - 1]
                pygame.draw.line(
                    self.screen,
                    self.PATH_COLOR,
                    (self.side_width + prev_col * self.cuadrante + self.cuadrante // 2, self.header_height + prev_row * self.cuadrante + self.cuadrante // 2),
                    (self.side_width + col * self.cuadrante + self.cuadrante // 2, self.header_height + row * self.cuadrante + self.cuadrante // 2),
                    3
                )
        
        for counter, (row, col) in enumerate(self.path):
            text_surface = font.render(str(counter + 1), True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(self.side_width + col * self.cuadrante + self.cuadrante // 2, self.header_height + row * self.cuadrante + self.cuadrante // 2))
            self.screen.blit(text_surface, text_rect)
    
    def render(self):
        pygame.init()
        image_path = os.path.join(os.path.dirname(__file__), "img", "wn.png")
        self.knight_image = pygame.image.load(image_path)
        self.knight_image = pygame.transform.scale(self.knight_image, (self.cuadrante, self.cuadrante))
        self.screen = pygame.display.set_mode((self.pantalla_ancho, self.pantalla_alto))
        pygame.display.set_caption('Chess Board')
        
        current_move_index = 0
        knight_row, knight_col = self.movimientos[current_move_index]
        self.path = [(knight_row, knight_col)]
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Dibujar el tablero
            self.__draw_board()
            # Dibujar encabezado y costado
            self.__draw_header_and_side()
            # Dibujar el recorrido con líneas y números
            self.__draw_path()
            
            # Posición del caballo
            knight_x = self.side_width + knight_col * self.cuadrante
            knight_y = self.header_height + knight_row * self.cuadrante
            self.screen.blit(self.knight_image, (knight_x, knight_y))
            
            pygame.display.flip()
            time.sleep(0.3)
            #time.sleep(0.00000000000000001)

            current_move_index += 1
            if current_move_index < len(self.movimientos):
                knight_row, knight_col = self.movimientos[current_move_index]
                self.path.append((knight_row, knight_col))
            else:
                running = False
        

        # Detecta la ruta de trabajo actual y guarda el archivo en la carpeta `out`
        output_path = os.path.join(os.path.dirname(__file__), f"out/tablero_{self.filas}x{self.columnas}.png")
        pygame.image.save(self.screen, output_path)
        
        #pygame.image.save(self.screen, f"out/tablero_{self.filas}x{self.columnas}.png")
        #pygame.image.save(self.screen, f"interfaz/out/tablero_{self.filas}x{self.columnas}.png")
        pygame.quit()
