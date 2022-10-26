from utils import clip_set_to_list_on_yaxis
import pygame
import json
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "popup"
        )
    )

# Json
with open(f"{resources_path}/popup.json") as json_file:
    popup_data = json.load(json_file)


class Title:
    def __init__(self):
        animation_set = pygame.image.load(
            f"{resources_path}/title_animation.png")
        self.idx = 0

        # Get title animation's frames
        self.frames = [
            img for img in clip_set_to_list_on_yaxis(animation_set)
        ]

        # Initialize rectangle
        self.rect = pygame.Rect(
            popup_data["title_position"], self.frames[0].get_size())

    def draw(self, display):
        # Reset
        if self.idx >= len(self.frames) * 5:
            self.idx = 0

        # Draw
        img = self.frames[self.idx // 5]
        display.blit(img, self.rect)

        # Update
        self.idx += 1
