from utils import palette_swap
from window import window
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

# Window
pygame.display.set_mode(window.rect.size)

# Json
with open(f"{resources_path}/screens.json") as json_file:
    screens_data = json.load(json_file)


class Button:
    # Initialize 
    def __init__(self, display_size_divider):
        image = pygame.image.load(
            f"{resources_path}/play_button.png")
        enlarge = display_size_divider

        # Palette
        hover_palette = {
            (9, 10, 20): (57, 74, 80),
            (235, 237, 233): (129, 151, 150)}
        
        # Initialize resize image
        wd, ht = image.get_size()
        resized_image = pygame.transform.scale(
            image, (wd * 2, ht * 2))

        # Initialize hover image
        hover_img = palette_swap(resized_image.convert(), hover_palette)

        # Initialize rectangles
        rect = pygame.Rect(
            screens_data["playbutton_position"],
            resized_image.get_rect().size)
        hitbox = pygame.Rect(
            rect.x * enlarge, rect.y * enlarge,
            rect.width * enlarge, rect.height * enlarge)

        # Append button
        self.button = [
            False,  # if mouse is over
            resized_image,  # original image
            hover_img,  # hover image
            rect,  # image's rectangle
            hitbox  # hitbox
        ]

    # Draw 
    def draw(self, display):
        mouse_is_over, orig_img, hover_img, rect, _ = self.button
        img = hover_img if mouse_is_over else orig_img

        display.blit(img, rect)

    # Action detection 
    def button_down_detection(self):
        *_, hitbox = self.button

        mouse_pos = pygame.mouse.get_pos()
        if hitbox.collidepoint(mouse_pos):
            return True

    def button_over_detection(self):
        *_, hitbox = self.button

        mouse_pos = pygame.mouse.get_pos()
        self.button[0] = True if hitbox.collidepoint(mouse_pos) else False

    # Functions 
    def reset_overdetection(self):
        self.button[0] = False
