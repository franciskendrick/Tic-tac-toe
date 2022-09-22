from utils import Colors, LetterFont
from window import window
import pygame

pygame.init()


class TicTacToe(LetterFont):
    display_size_divider = 5

    # Initialize
    def __init__(self, user_letter):
        super().__init__()

        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // self.display_size_divider,
            ht // self.display_size_divider),
            pygame.SRCALPHA)
        
        # Board
        self.board = []
        e = self.display_size_divider
        for i, (box_x, ltr_x) in enumerate(
                zip(range(0, 128, 42+1), range(11, 97+1, 43))):
            self.board.append([])
            for (box_y, ltr_y) in zip(
                    range(0, 128, 42+1), range(9, 95+1, 43)):
                box = [
                    "",  # value
                    False,  # is hovered
                    (ltr_x, ltr_y),  # letter's position
                    pygame.Rect(box_x, box_y, 42, 42),  # box's rectangle
                    pygame.Rect(box_x*e, box_y*e, 42*e, 42*e),  # hitbox
                ]
                self.board[i].append(box)
        
        self.user_letter = user_letter
        self.ishovered_off = False

    # Draw
    def draw(self, display):
        # Fill game's display with a transparent background
        self.display.fill((0, 0, 0, 0))

        # Draw lines
        for i in range(1, 3): 
            size = 128 * 0.333
            pygame.draw.line(
                self.display, Colors.black, (0, size * i), (128, size * i))
            pygame.draw.line(
                self.display, Colors.black, (size * i, 0), (size * i, 128))

        # Draw boxes
        for row in self.board:
            for (value, is_hovered, letter_pos, box_rect, _) in row:
                # Draw box
                color = Colors.light_gray if is_hovered else Colors.white
                pygame.draw.rect(self.display, color, box_rect)

                # Draw letter
                if value != "":
                    self.render_font(
                        self.display, value, letter_pos, enlarge=4)

        # Blit game's display to original display
        resized_game_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_game_display, (0, 0))

    # Handle mouse
    def handle_mousemotion(self):
        if pygame.mouse.get_focused():  # mouse is INSIDE the pygame window
            self.ishovered_off = False

            mouse_pos = pygame.mouse.get_pos()
            for i, row in enumerate(self.board):
                for j, (value, *_, hitbox) in enumerate(row):
                    # Toggle is hovered variable
                    if hitbox.collidepoint(*mouse_pos) and value == "":
                        self.board[i][j][1] = True  # is hovered
                    else:
                        self.board[i][j][1] = False  # is hovered
        else:  # mouse is OUTSIDE the pygame window
            if not self.ishovered_off:
                self.ishovered_off = True

                # Turn off is hovered variables
                for i, row in enumerate(self.board):
                    for j, _ in enumerate(row):
                        self.board[i][j][1] = False  # is hovered

    def handle_mousedown(self):
        if pygame.mouse.get_focused():  # mouse is in the pygame window
            if pygame.mouse.get_pressed()[0]:  # left-click is pressed
                mouse_pos = pygame.mouse.get_pos()
                for i, row in enumerate(self.board):
                    for j, (*_, hitbox) in enumerate(row):
                        # Update value variable
                        if hitbox.collidepoint(*mouse_pos):
                            self.board[i][j][0] = self.user_letter  # value

    # Get Winner
    def get_winner(self):
        # Rows
        for i in range(3):
            row = [self.board[j][i][0] for j in range(3)]
            if len(set(row)) == 1 and row[0] != "":
                return row[0]

        # Columns
        for i in range(3):
            col = [self.board[j][i][0] for j in range(3)]
            if len(set(col)) == 1 and col[0] != "":
                return col[0]

        # Diagonals
        if len(set([self.board[i][i][0] for i in range(3)])) == 1 and self.board[0][0][0] != "":
            return self.board[0][0][0]
        if len(set([self.board[i][2-i][0] for i in range(3)])) == 1 and self.board[0][2][0] != "":
            return self.board[0][2][0]
