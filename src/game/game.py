from utils import Colors
from window import window
import pygame

pygame.init()


class TicTacToe:
    display_size_divider = 5

    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // self.display_size_divider,
            ht // self.display_size_divider),
            pygame.SRCALPHA)
        
        self.board = [["" for _ in range(3)] for _ in range(3)]

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

        # Blit game's display to original display
        resized_game_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_game_display, (0, 0))
