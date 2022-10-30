from utils import Colors, LetterFont
from window import window
from .player import HumanPlayer, ComputerPlayer
import pygame
import time
import math

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

        # Status
        self.x_turn = True
        self.game_finished = False

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

    # Handle 
    def handle_mousemotion(self):
        if pygame.mouse.get_focused():  # mouse is INSIDE the pygame window
            self.ishovered_off = False

            # Loop over every box in board and update is_hovered variable
            mouse_pos = pygame.mouse.get_pos()
            for i, (value, *_, hitbox) in enumerate(self.board.board):
                # Toggle is hovered variable
                if hitbox.collidepoint(*mouse_pos) and value == "":
                    self.board.board[i][1] = True  # is hovered
                else:
                    self.board.board[i][1] = False  # is hovered
        elif not pygame.mouse.get_focused():  # mouse is OUTSIDE the pygame window
            if not self.ishovered_off:
                self.ishovered_off = True

                # Turn off is_hovered variables
                for i in range(len(self.board.board)):
                    self.board.board[i][1] = False  # is hovered

    def handle_moves(self):
        if self.x_turn:
            move = self.human_player.handle_mousedown(self.board.board)
            if move != None:
                self.board.board[move][0] = "X"
                self.x_turn = False
        else:
            move = self.computer_player.get_move(self.board)
            if move != None:
                self.board.board[move][0] = "O"
                self.x_turn = True
                time.sleep(0.8)

    # Get data
    def get_winner(self):
        winner = self.board.winner()
        if winner is not None:  # check who won
            self.reset_overdetection()
            self.game_finished = True

            return winner
        elif self.board.num_empty_squares() <= 0:  # check if draw
            self.reset_overdetection()
            self.game_finished = True

            return "DRAW"

    # Reset
    def reset_overdetection(self):
        for i in range(len(self.board.board)):
            self.board.board[i][1] = False  # is hovered

    def reset_game(self):
        # Board
        self.board.init_board(self.display_size_divider)

        # Status
        self.x_turn = True
        self.game_finished = False


class Board(LetterFont):
    # Initialize
    def __init__(self, e):
        super().__init__()

        self.init_board(e)
        self.ishovered_off = False
        self.current_winner = None

    def init_board(self, e):
        self.board = [] 
        for (box_x, ltr_x) in zip(range(0, 128, 42+1), range(11, 97+1, 43)):
            for (box_y, ltr_y) in zip(range(0, 128, 42+1), range(9, 95+1, 43)):
                box = [
                    "",  # value
                    False,  # is hovered
                    (ltr_x, ltr_y),  # letter's position
                    pygame.Rect(box_x, box_y, 42, 42),  # box's rectangle
                    pygame.Rect(box_x*e, box_y*e, 42*e, 42*e),  # hitbox
                ]
                self.board.append(box)

    # Draw
    def draw(self, display):
        for (value, is_hovered, letter_pos, box_rect, _) in self.board:
            # Draw box
            color = Colors.light_gray if is_hovered else Colors.white
            pygame.draw.rect(display, color, box_rect)

            # Draw letter
            if value != "":
                self.render_font(
                    display, value, letter_pos, enlarge=4)

    # Move
    def make_move(self, move, letter):
        if self.board[move][0] == "":
            self.board[move][0] = letter
            if self.winner(move, letter) == letter:
                self.current_winner = letter
            return True
        return False

    # Get winner
    def winner(self, move=None, letter=None):  # returns the winner of the game
        if (move, letter) == (None, None):  # no variables were given
            letter = self.winner_with_novars()
        else:  # both variables were given
            letter = self.winner_with_vars(move, letter)
        
        return letter

    def winner_with_vars(self, move, letter):
        # Rows
        ind = move % 3
        column = [self.board[ind + (i * 3)] for i in range(3)]
        if all([value == letter for (value, *_) in column]):
            return letter

        # Columns
        ind = math.floor(move / 3)
        row = self.board[ind * 3:(ind + 1) * 3]
        if all([value == letter for (value, *_) in row]):
            return letter

        # Diagonals
        if move % 2 == 0:
            # Diagonal 1
            diagonal = [self.board[i] for i in [0, 4, 8]]
            if all([value == letter for (value, *_) in diagonal]):
                return letter

            # Diagonal 2
            diagonal = [self.board[i] for i in [2, 4, 6]]
            if all([value == letter for (value, *_) in diagonal]):
                return letter

        return None

    def winner_with_novars(self):
        for letter in ["X", "O"]:
            # Rows
            for ind in range(3):
                column = [self.board[ind + (i * 3)] for i in range(3)]
                if all([value == letter for (value, *_) in column]):
                    return letter

            # Columns
            for ind in range(3):
                row = self.board[ind * 3:(ind + 1) * 3]
                if all([value == letter for (value, *_) in row]):
                    return letter

            # Diagonals
            diagonal = [self.board[i] for i in [0, 4, 8]]
            if all([value == letter for (value, *_) in diagonal]):
                return letter

            diagonal = [self.board[i] for i in [2, 4, 6]]
            if all([value == letter for (value, *_) in diagonal]):
                return letter

        return None

    # Get data
    def empty_squares(self):  # returns a list of the positions of board's empty squares
        return "" in [self.board[i][0] for i in range(len(self.board))]

    def num_empty_squares(self):  # resturns the number of how many empty squares are left
        return [self.board[i][0] for i in range(len(self.board))].count("")

    def available_moves(self):  # returns a list of all available moves
        return [
            move for move, (value, *_) in enumerate(self.board) if value == ""
        ]
