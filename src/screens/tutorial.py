import pygame
import json
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "screens"
        )
    )

# Json
with open(f"{resources_path}/screens.json") as json_file:
    screens_data = json.load(json_file)


class Tutorial:
    def __init__(self):
        self.image = pygame.image.load(
            f"{resources_path}/tutorial.png")
        self.pos = screens_data["tutorial_position"]

    def draw(self, display):
        display.blit(self.image, self.pos)
