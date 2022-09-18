from utils import Colors, LetterFont
from window import window
import pygame
import json
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "game"
        )
    )

# Json
with open(f"{resources_path}/game.json") as json_file:
    game_data = json.load(json_file)


class TicTacToe(LetterFont):
    display_size_divider = 5

    def __init__(self):
        super().__init__()

        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // self.display_size_divider,
            ht // self.display_size_divider),
            pygame.SRCALPHA)
        
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.letter_positions = game_data["boardletter_positions"]

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

        # Draw letters
        for i, row in enumerate(self.board):
            for j, letter in enumerate(row):
                if letter != "":
                    pos = self.letter_positions[j][i]
                    self.render_font(
                        self.display, letter, pos, enlarge=4)

        # Blit game's display to original display
        resized_game_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_game_display, (0, 0))
