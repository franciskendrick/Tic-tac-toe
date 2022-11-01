import pygame
import random
import math

pygame.init()


class HumanPlayer:
    def __init__(self, user_letter):
        self.user_letter = user_letter

    def handle_mousedown(self, board):
        if pygame.mouse.get_focused():  # mouse is in the pygame window
            if pygame.mouse.get_pressed()[0]:  # left-click is pressed
                # Loop over every box in board until hovered box is found
                mouse_pos = pygame.mouse.get_pos()

                for i, (*_, hitbox) in enumerate(board.board):
                    # Check value variable
                    if hitbox.collidepoint(*mouse_pos) and i in board.available_moves():
                        board.board[i][0] = self.user_letter  # value
                        return i
        return None


class ComputerPlayer:  # Venice AI
    def __init__(self, user_letter):
        self.user_letter = user_letter

    def get_move(self, board):
        if len(board.available_moves()) == 9:
            move = random.choice(board.available_moves())
        else:
            move = self.minimax(board, self.user_letter)["position"]

        return move

    def minimax(self, state, player):
        max_player = self.user_letter  # yourself
        other_player = "O" if player == "X" else "X"

        # Check if the previous move won
        if state.current_winner == other_player:
            return {
                "position": None, 
                "eval": 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {"position": None, "eval": 0}

        # Check if player evaluating is the maximizing or minimizing
        if player == max_player:  # maximizing player
            best = {"position": None, "eval": -math.inf}
        else:  # minimizing player
            best = {"position": None, "eval": math.inf}

        # Try every possible move
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            child = self.minimax(state, other_player)

            # Undo move
            state.board[possible_move][0] = ""
            state.current_winner = None
            child["position"] = possible_move

            # Compare evaluation of child and best
            if player == max_player:
                if child["eval"] > best["eval"]:
                    best = child
            else:
                if child["eval"] < best["eval"]:
                    best = child

        # Return best move
        return best
