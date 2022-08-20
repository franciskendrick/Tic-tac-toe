from utils import clip_set_to_list_on_yaxis
import pygame
import json
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "menu"
        )
    )

# Json
with open(f"{resources_path}/menu.json") as json_file:
    menu_data = json.load(json_file)


class Title:
    def __init__(self):
        animation_set = pygame.image.load(
            f"{resources_path}/title_animation.png")
        self.idx = 0

        # Get title animation's frames
        self.frames = []
        for img in clip_set_to_list_on_yaxis(animation_set):
            # Resize image
            wd, ht = img.get_size()
            size = (wd * 2, ht * 2)
            img = pygame.transform.scale(img, size)

            # Append to frames
            self.frames.append(img)

        # Initialize rectangle
        self.rect = pygame.Rect(
            menu_data["title_position"], img.get_size())

    def draw(self, display):
        # Reset
        if self.idx >= len(self.frames) * 5:
            self.idx = 0

        # Draw
        img = self.frames[self.idx // 5]
        display.blit(img, self.rect)

        # Update
        self.idx += 1
