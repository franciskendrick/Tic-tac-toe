from window import window
from .title import Title
from .buttons import Buttons
import pygame

pygame.init()


class PopUp:
    display_size_divider = 5

    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // self.display_size_divider,
            ht // self.display_size_divider),
            pygame.SRCALPHA)

        self.title = Title()
        self.buttons = Buttons()

    def draw(self, display):
        # Fill popup's display with a transparent background
        self.display.fill((0, 0, 0, 0))

        # Draw popup window on popup's display
        self.title.draw(self.display)
        self.buttons.draw(self.display)

        # Blit popup's display to original display
        resized_menu_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_menu_display, (0, 0))
