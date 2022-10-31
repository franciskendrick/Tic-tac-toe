from window import window
from screens import Button, Tutorial, Score
from .title import Title
import pygame

pygame.init()


class GameOver:
    display_size_divider = 5

    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // self.display_size_divider,
            ht // self.display_size_divider),
            pygame.SRCALPHA)

        self.button = Button(self.display_size_divider)
        self.tutorial = Tutorial()
        self.score = Score()

    def init_title(self, player_won):
        self.title = Title(player_won)

    def draw(self, display):
        # Fill gameover's display with a white opaque background
        self.display.fill((235, 237, 233, 200))

        # Draw gameover window on gameover's display
        self.title.draw(self.display)
        self.button.draw(self.display)
        self.tutorial.draw(self.display)
        self.score.draw(self.display)

        # Blit gameover's display to original display
        resized_gameover_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_gameover_display, (0, 0))
