import pygame

pygame.init()


class Player:
    def __init__(self, user_letter):
        self.user_letter = user_letter
        self.type = "max" if self.user_letter == "X" else "min"


class HumanPlayer(Player):
    def __init__(self, user_letter):
        super().__init__(user_letter)

    # Handle mouse
    def handle_mousedown(self, board):
        if pygame.mouse.get_focused():  # mouse is in the pygame window
            if pygame.mouse.get_pressed()[0]:  # left-click is pressed
                # Loop over every box in board until hovered box is found
                mouse_pos = pygame.mouse.get_pos()
                for i, row in enumerate(board):
                    for j, (*_, hitbox) in enumerate(row):
                        # Update value variable
                        if hitbox.collidepoint(*mouse_pos):
                            board[i][j][0] = self.user_letter  # value
                            return


class ComputerPlayer(Player):  # Venice AI
    def __init__(self, user_letter):
        super().__init__(user_letter)
