from utils import Colors
from window import window
from menu import Menu
import pygame
import sys


# Redraws
def redraw_game():
    pass


def redraw_menu():
    # Draw background
    win.fill(Colors.white)

    # Update display
    pygame.display.update()


# Loops
def game_loop():
    pass


def menu_loop():
    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

        # Update display
        redraw_menu()

    pygame.quit()
    sys.exit()


# Execute
if __name__ == "__main__":
    pygame.init()
    
    # Initialize window
    win = pygame.display.set_mode(window.rect.size)
    pygame.display.set_caption("Tic-Tac-Toe")

    # Initialize windows
    menu = Menu()

    # Execute
    menu_loop()
