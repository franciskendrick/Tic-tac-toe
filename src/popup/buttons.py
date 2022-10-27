from utils import clip_set_to_list_on_xaxis, palette_swap
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


class Buttons:
    # Initialize
    def __init__(self):
        spriteset = pygame.image.load(
            f"{resources_path}/buttons.png")
        order = ["yes", "no"]
        images = clip_set_to_list_on_xaxis(spriteset)
        
        # Palette
        hover_palette = {
            "yes": {
                (9, 10, 20): (37, 86, 46),
                (235, 237, 233): (70, 130, 50)},
            "no": {
                (9, 10, 20): (117, 36, 56),
                (235, 237, 233): (165, 48, 48)}
        }

        # Buttons
        self.buttons = {}
        for name, img in zip(order, images):
            # Initialize
            hover_img = palette_swap(img.convert(), hover_palette[name])
            img_rect = pygame.Rect(
                popup_data["buttons_positions"][name], img.get_rect().size)

            # Append
            button = [
                False,  # is hovered
                img,  # orig image
                hover_img,  # hover image
                img_rect  # image rectangle
            ]
            self.buttons[name] = button

    # Draw
    def draw(self, display):
        for button in self.buttons.values():
            is_hovered, orig_img, hover_img, img_rect = button
            img = hover_img if is_hovered else orig_img

            display.blit(img, img_rect)  # image

    # Action detection
    def button_down_detection(self):
        pass

    def button_over_detection(self):
        pass

    # Functions
    def reset_overdetection(self):
        pass
