from window import window
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

    def draw(self, display):
        # Fill gameover's display with a transparent background
        self.display.fill((0, 0, 0, 0))

        # Blit gameover's display to original display
        resized_gameover_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_gameover_display, (0, 0))
