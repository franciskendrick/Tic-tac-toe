from utils import Colors
from window import window
from screens import screen
from game import TicTacToe
from menu import Menu
from popup import PopUp
from gameover import GameOver
import pygame
import time
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


def redraw_popup():
    # Draw background
    win.fill(Colors.white)

    # Draw popup
    popup.draw(win)

    # Update display
    pygame.display.update()


def redraw_gameover():
    # Draw background
    win.fill(Colors.white)

    # Draw game
    tictactoe.draw(win)

    # Draw gameover
    gameover.draw(win)

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
                    is_yes = popup_loop()
                    if is_yes:
                        tictactoe.reset_game()
                        menu_loop()
                    else:
                        game_loop()
                if event.key == pygame.K_SPACE:  # restart game
                    is_yes = popup_loop()
                    if is_yes:
                        tictactoe.reset_game()
                    else:
                        game_loop()

        # Handle mouse motion
        tictactoe.handle_mousemotion()

        # Update display
        redraw_game()

        # Handle moves
        tictactoe.handle_moves()

        # Get winner
        winner = tictactoe.get_winner()
        if winner is not None:
            # Reset game's mouse over detection
            tictactoe.reset_overdetection()

            # Update display
            redraw_game()

            # Initialize gameover's title
            gameover.init_title(winner)

            # Update scoreboard
            if winner is not "DRAW":
                screen.scoreboard.scores[winner] += 1

            # Pause
            time.sleep(0.8)

            # Redirect to gameover loop            
            gameover_loop()

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
                is_pressed = screen.button.button_down_detection()
                screen.button.reset_overdetection()
                if is_pressed:  # button is pressed
                    game_loop()

            # Menu buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                screen.button.button_over_detection()

        # Update display
        redraw_menu()
        clock.tick(30)

    pygame.quit()
    sys.exit()


def popup_loop():
    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

            # PopUp buttons' down detection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left-clicked has been uped
                button_pressed = popup.buttons.button_down_detection()
                popup.buttons.reset_overdetection() 
                if button_pressed == "yes":  # yes button is pressed
                    return True
                elif button_pressed == "no":  # no button is pressed
                    return False

            # PopUp buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                popup.buttons.button_over_detection()

        # Update display
        redraw_popup()
        clock.tick(30)

    pygame.quit()
    sys.exit()


def gameover_loop():
    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

            # GameOver buttons' down detection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left-clicked has been uped
                is_pressed = screen.button.button_down_detection()
                screen.button.reset_overdetection()
                if is_pressed:  # button is pressed
                    tictactoe.reset_game()
                    game_loop()

            # GameOver buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                screen.button.button_over_detection()

            # Key detection
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # exit game
                    tictactoe.reset_game()
                    menu_loop()
                if event.key == pygame.K_SPACE:  # restart game
                    tictactoe.reset_game()
                    game_loop()

        # Update display
        redraw_gameover()
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
    tictactoe = TicTacToe()
    menu = Menu()
    popup = PopUp()
    gameover = GameOver()

    # Execute
    menu_loop()
