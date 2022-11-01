from .button import Button
from .tutorial import Tutorial
from .score import Score
import pygame

pygame.init()


class Screen:
    def __init__(self):
        self.button = Button(5)
        self.tutorial = Tutorial()
        self.scoreboard = Score()

    def draw(self, display):
        self.button.draw(display)
        self.tutorial.draw(display)
        self.scoreboard.draw(display)


screen = Screen()
