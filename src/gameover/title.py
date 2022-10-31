from utils import clip_set_to_list_on_yaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "gameover"
        )
    )


class Title:
    def __init__(self, winner):
        filename_switchcase = {
            "X": "youwin",
            "O": "gameover",
            "DRAW": "draw"
        }
        animation_set = pygame.image.load(
            f"{resources_path}/{filename_switchcase[winner]}_title_animation.png")
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
        position_switchcase = {
            "X": (22, 18),
            "O": (13, 18),
            "DRAW": (40, 18)
        }
        self.rect = pygame.Rect(
            position_switchcase[winner], img.get_size())
    
    def draw(self, display):
        # Reset
        if self.idx >= len(self.frames) * 5:
            self.idx = 0

        # Draw
        img = self.frames[self.idx // 5]
        display.blit(img, self.rect)

        # Update
        self.idx += 1
