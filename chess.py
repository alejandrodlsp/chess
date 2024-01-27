import pygame
from board import Board
import draw

X_SIZE = 500
Y_SIZE = 500

running = True
screen = None
board = Board()

def on_setup():
    draw.draw_board(screen, board)

def on_teardown():
    pass

def update_loop():
    pass

def on_mouse_button_down(event):
    if event.button == 1:
        draw.handle_click_event(event, board)
                    
if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode([X_SIZE, Y_SIZE])
    pygame.display.set_caption("Chess Board")

    on_setup()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                on_mouse_button_down(event)

        update_loop()
        pygame.display.flip()

    on_teardown()
    pygame.quit()