import pygame
import time

# Inicialización de pygame
pygame.init()

# Configuración de la pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess Board")

# Colores para las casillas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PATH_COLOR = (255, 0, 0)  # Color para el recorrido

# Tamaño del tablero
ROWS, COLS = 8, 8
SQUARE_SIZE = SCREEN_WIDTH // COLS

# Cargar la imagen del caballo
knight_image = pygame.image.load("img/wn.png")
knight_image = pygame.transform.scale(knight_image, (SQUARE_SIZE, SQUARE_SIZE))  # Escalar la imagen

# Lista de movimientos (fila, columna)
# 5x5
moves_5 = [
    (0, 0),
    (2, 1),
    (4, 0),
    (3, 2),
    (4, 4),
    (2, 3),
    (0, 4),
    (1, 2),
    (3, 3),
    (1, 4),
    (0, 2),
    (1, 0),
    (3, 1),
    (4, 3),
    (2, 4),
    (0, 3),
    (1, 1),
    (3, 0),
    (4, 2),
    (3, 4),
    (1, 3),
    (0, 1),
    (2, 2),
    (4, 1),
    (2, 0)
]

#6x6
moves_6 = [
    (0, 0),
    (2, 1),(4, 0),(5, 2),(4, 4),(2, 5),
    (0, 4),(1, 2),(2, 0),(0, 1),
    (1, 3),(0, 5),(2, 4),(4, 5),
    (3, 3),(5, 4),(3, 5),(1, 4),(0, 2),
    (1, 0),(3, 1),(5, 0),(4, 2),(2, 3),
    (1, 5),(0, 3),(1, 1),(3, 2),(5, 3),(4, 1),(2, 2),
    (3, 4),(5, 5),(4, 3),(5, 1),(3, 0)
]

#8x8
moves_8 = [
    (0, 0), (2, 1), (0, 2), (1, 0), (3, 1), (5, 0),
    (7, 1), (6, 3), (7, 5), (6, 7), (4, 6), (2, 7),
    (0, 6), (1, 4), (2, 6), (0, 7), (1, 5), (0, 3),
    (1, 1), (3, 0), (5, 1), (7, 0), (6, 2), (7, 4),
    (6, 6), (4, 7), (5, 5), (7, 6), (5, 7), (3, 6),
    (1, 7), (0, 5), (1, 3), (0, 1), (2, 2), (3, 4),
    (4, 2), (5, 4), (7, 3), (6, 1), (4, 0), (5, 2),
    (6, 0), (7, 2), (6, 4), (4, 3), (3, 5), (2, 3),
    (0, 4), (1, 6), (3, 7), (2, 5), (3, 3), (4, 5),
    (2, 4), (1, 2), (2, 0), (4, 1), (5, 3), (3, 2),
    (4, 4), (6, 5), (7, 7), (5, 6)
]

#10x10

# Inicializar la posición del caballo
current_move_index = 0
knight_row, knight_col = moves_8[current_move_index]

# Lista para almacenar el recorrido
path = [(knight_row, knight_col)]

# Función para dibujar el tablero
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Función para dibujar el recorrido
def draw_path():
    for counter, (row, col) in enumerate(path):
        pygame.draw.circle(screen, PATH_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 4)
        # Opcional: dibujar el número en el camino
        font = pygame.font.Font(None, 36)  # Crear fuente
        text_surface = font.render(str(counter + 1), True, (0, 0, 0))  # Texto negro
        text_rect = text_surface.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
        screen.blit(text_surface, text_rect)
# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibujar el tablero
    draw_board()

    # Dibujar el recorrido
    draw_path()

    # Calcular la posición del caballo en píxeles
    knight_x = knight_col * SQUARE_SIZE
    knight_y = knight_row * SQUARE_SIZE

    # Dibujar el caballo en la nueva posición
    screen.blit(knight_image, (knight_x, knight_y))

    # Actualizar la pantalla
    pygame.display.flip()

    # Esperar un poco antes de mover al siguiente punto
    time.sleep(1)  # Ajusta el tiempo para la velocidad de movimiento

    # Actualizar al siguiente movimiento
    current_move_index += 1
    if current_move_index < len(moves_8):
        knight_row, knight_col = moves_8[current_move_index]
        path.append((knight_row, knight_col))  # Agregar la nueva posición al recorrido
    else:
        running = False  # Terminar si no hay más movimientos

# Salir de pygame
pygame.quit()





