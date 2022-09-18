from utils import Colors
from window import window
import pygame

pygame.init()


class Game:
    def __init__(self):
        self.display = pygame.Surface(
            window.rect.size, pygame.SRCALPHA)

    def draw(self, display):
        # Fill game's display with a transparent background
        self.display.fill((0, 0, 0, 0))

        # Draw lines
        for i in range(1, 3): 
            size = 640 * 0.333
            pygame.draw.line(
                display, Colors.black, (0, size * i), (640, size * i), 5)
            pygame.draw.line(
                display, Colors.black, (size * i, 0), (size * i, 640), 5)

        # Blit game's display to original display
        resized_game_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_game_display, (0, 0))
