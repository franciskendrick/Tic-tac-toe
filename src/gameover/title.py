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
    def __init__(self, player_won):
        filename = "youwin" if player_won else "gameover"
        animation_set = pygame.image.load(
            f"{resources_path}/{filename}_title_animation.png")
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
        pos = (22, 20) if player_won else (13, 20)
        self.rect = pygame.Rect(pos, img.get_size())
    
    def draw(self, display):
        # Reset
        if self.idx >= len(self.frames) * 5:
            self.idx = 0

        # Draw
        img = self.frames[self.idx // 5]
        display.blit(img, self.rect)

        # Update
        self.idx += 1
