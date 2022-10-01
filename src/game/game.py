from utils import Colors, LetterFont
from window import window
from .player import HumanPlayer, ComputerPlayer
import pygame
import time

pygame.init()


class TicTacToe:
    display_size_divider = 5

    # Initialize
    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // self.display_size_divider,
            ht // self.display_size_divider),
            pygame.SRCALPHA)

        # Board
        self.board = Board(self.display_size_divider)

        # Players
        self.human_player = HumanPlayer("X")
        self.computer_player = ComputerPlayer("O")

        # Turn
        self.x_turn = True

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
        self.board.draw(self.display)

        # Blit game's display to original display
        resized_game_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_game_display, (0, 0))

    # Handle mouse
    def handle_mousemotion(self):
        if pygame.mouse.get_focused():  # mouse is INSIDE the pygame window
            self.ishovered_off = False

            # Loop over every box in board and update is_hovered variable
            mouse_pos = pygame.mouse.get_pos()
            for i, row in enumerate(self.board.board):
                for j, (value, *_, hitbox) in enumerate(row):
                    # Toggle is hovered variable
                    if hitbox.collidepoint(*mouse_pos) and value == "":
                        self.board.board[i][j][1] = True  # is hovered
                    else:
                        self.board.board[i][j][1] = False  # is hovered
        elif not pygame.mouse.get_focused():  # mouse is OUTSIDE the pygame window
            if not self.ishovered_off:
                self.ishovered_off = True

                # Turn off is_hovered variables
                for i, row in enumerate(self.board.board):
                    for j, _ in enumerate(row):
                        self.board.board[i][j][1] = False  # is hovered

    # Handle moves
    def handle_moves(self):
        if self.x_turn:
            move = self.human_player.handle_mousedown(self.board.board)
            if move != None:
                i, j = move
                self.board.board[i][j][0] = "X"
                self.x_turn = False
        else:
            move = self.computer_player.get_move(self.board)
            if move != None:
                i, j = move
                self.board.board[i][j][0] = "O"
                self.x_turn = True
                time.sleep(0.8)


class Board(LetterFont):
    def __init__(self, e):
        super().__init__()

        # Board
        self.board = []
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
        
        self.ishovered_off = False

        # Winner
        self.current_winner = None
    
    def draw(self, display):
        for row in self.board:
            for (value, is_hovered, letter_pos, box_rect, _) in row:
                # Draw box
                color = Colors.light_gray if is_hovered else Colors.white
                pygame.draw.rect(display, color, box_rect)

                # Draw letter
                if value != "":
                    self.render_font(
                        display, value, letter_pos, enlarge=4)

    # Get data
    def make_move(self, move, letter):
        i, j = move
        if self.board[i][j][0] == "":
            self.board[i][j][0] = letter
            if self.winner() == letter:
                self.current_winner = letter
            return True
        return False

    def winner(self):
        # Rows
        for row in self.board:
            true_row = [row[i][0] for i in range(len(row))]
            if len(set(true_row)) == 1 and true_row[0] != "":
                return true_row[0]

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

        return None

    def empty_squares(self):
        empty_squares = True
        for row in self.board:
            true_row = [row[i][0] for i in range(len(row))]
            empty_squares = "" in true_row

        return empty_squares

    def num_empty_squares(self):
        empty_squares = 0
        for row in self.board:
            true_row = [row[i][0] for i in range(len(row))]
            empty_squares += true_row.count("")

        return empty_squares

    def available_moves(self):
        available_moves = []
        for i, row in enumerate(self.board):
            for j, (value, *_) in enumerate(row):
                if value == "":
                    available_moves.append([i, j])

        return available_moves
