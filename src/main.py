from utils import Colors
from window import window
from menu import Menu
from game import TicTacToe
import pygame
import sys


# Redraws
def redraw_game():
    # Draw game
    tictactoe.draw(win)

    # Update display
    pygame.display.update()


def redraw_menu():
    # Draw background
    win.fill(Colors.white)

    # Draw menu
    menu.draw(win)

    # Update display
    pygame.display.update()


# Loops
def game_loop():
    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

            # Key detection
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # exit game
                    menu_loop()

        # Handle tic-tac-toe board
        if not tictactoe.game_finished:
            tictactoe.handle_mousemotion()
            tictactoe.handle_moves()
            tictactoe.get_winner()

        # Update display
        redraw_game()

    pygame.quit()
    sys.exit()


def menu_loop():
    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

            # Menu buttons' down detection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left-clicked has been uped
                is_pressed = menu.button.button_down_detection()
                menu.button.reset_overdetection()
                if is_pressed:  # button is pressed
                    game_loop()

            # Menu buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                menu.button.button_over_detection()

        # Update display
        redraw_menu()
        clock.tick(30)

    pygame.quit()
    sys.exit()


# Execute
if __name__ == "__main__":
    pygame.init()
    
    # Initialize window
    win = pygame.display.set_mode(window.rect.size)
    pygame.display.set_caption("Tic-Tac-Toe")
    clock = pygame.time.Clock()

    # Initialize windows
    menu = Menu()
    tictactoe = TicTacToe()

    # Execute
    menu_loop()
