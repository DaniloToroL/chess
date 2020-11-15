import pygame
import engine

WIDTH, HEIGHT = 512, 512
DIM = 8
PIXEL = HEIGHT // DIM
FPS_MAX = 15
IMAGES = {}

def load_images():
    """
    Initialize a global dictionary of images
    """
    pieces = ['wp','wR', 'wN', 'wB','wQ', 'wK', 'bp','bR', 'bN', 'bB','bQ', 'bK',]
    for piece in pieces:
        print(f"images/{piece}.png")
        IMAGES[piece] = pygame.transform.scale(pygame.image.load(f"images/{piece}.png"), (PIXEL, PIXEL))
    

def main():
    """
    docstring
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    game_state = engine.GameState()
    load_images()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:

                pos_x, pos_y = pygame.mouse.get_pos()
                idx_x = pos_x // PIXEL
                idx_y = (pos_y //  PIXEL) 
                if game_state.selected is None:
                    piece = game_state.board[idx_y][idx_x]
                    game_state.selected = {"piece": piece, "pos": (idx_x, idx_y)}
                else:
                    move_piece(screen, game_state, (idx_x, idx_y))
        
        draw_game_state(screen, game_state)
        clock.tick(FPS_MAX)
        pygame.display.flip()

def draw_game_state(screen, game_state):
    draw_board(screen)
    draw_pieces(screen, game_state.board)

def draw_board(screen):
    """
        Draw squares on the board
    """
    colors = [pygame.Color("white"), pygame.Color((150,150,150))]
    for row in range(DIM):
        for column in range(DIM):
            color = colors[(row + column) % 2]
            rect = pygame.Rect(column*PIXEL, row*PIXEL, PIXEL, PIXEL)
            pygame.draw.rect(screen, color, rect)


def draw_pieces(screen, board):
    """
        Draw the pieces on the board using current board
    """
    for row in range(DIM):
        for col in range(DIM):
            piece = board[row][col]
            if piece != "--":
                rect = pygame.Rect(col* PIXEL, row*PIXEL, PIXEL, PIXEL)
                screen.blit(IMAGES[piece], rect)

def move_piece(screen, game_state, position):
    x, y = position
    
    piece = game_state.selected
    last_x, last_y = piece["pos"]
    game_state.board[y][x] = piece["piece"]
    game_state.board[last_y][last_x] = "--"
    game_state.selected = None
    draw_pieces(screen, game_state.board)


if __name__ == "__main__":
    main()




