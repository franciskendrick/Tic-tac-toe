from window import window
from screens import Button, Tutorial, Score
from .title import Title
import pygame

pygame.init()


class Menu:
    display_size_divider = 5

    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // self.display_size_divider,
            ht // self.display_size_divider),
            pygame.SRCALPHA)

        self.title = Title()
        self.button = Button(self.display_size_divider)
        self.tutorial = Tutorial()
        self.score = Score()

    def draw(self, display):
        # Fill menu's display with a transparent background
        self.display.fill((0, 0, 0, 0))

        # Draw menu window on menu's display
        self.title.draw(self.display)
        self.button.draw(self.display)
        self.tutorial.draw(self.display)
        self.score.draw(self.display)

        # Blit menu's display to original display
        resized_menu_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_menu_display, (0, 0))
