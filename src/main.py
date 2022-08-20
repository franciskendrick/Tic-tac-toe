import pygame


# Redraws
def redraw_game():
    pass


def redraw_menu():
    pass


# Loops
def game_loop():
    pass


def menu_loop():
    pass


# Execute
if __name__ == "__main__":
    pygame.init()
    
    # Initialize window
    win_size = (640, 640)
    win = pygame.display.set_mode(win_size)
    pygame.display.set_caption("Tic-Tac-Toe")

    # Execute
    menu_loop()
