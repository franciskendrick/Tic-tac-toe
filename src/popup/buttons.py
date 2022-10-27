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
    def __init__(self, enlarge):
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
            hitbox = pygame.Rect(
                img_rect.x * enlarge, img_rect.y * enlarge,
                img_rect.width * enlarge, img_rect.height * enlarge)

            # Append
            button = [
                False,  # is hovered
                img,  # orig image
                hover_img,  # hover image
                img_rect,  # image rectangle
                hitbox  # hitbox
            ]
            self.buttons[name] = button

    # Draw
    def draw(self, display):
        for button in self.buttons.values():
            is_hovered, orig_img, hover_img, img_rect, _ = button
            img = hover_img if is_hovered else orig_img

            display.blit(img, img_rect)  # image

    # Action detection
    def button_down_detection(self):
        for (name, button) in self.buttons.items():
            *_, hitbox = button

            mouse_pos = pygame.mouse.get_pos()
            if hitbox.collidepoint(mouse_pos):
                return name

    def button_over_detection(self):
        for button in self.buttons.values():
            *_, hitbox = button

            mouse_pos = pygame.mouse.get_pos()
            button[0] = True if hitbox.collidepoint(mouse_pos) else False

    # Functions
    def reset_overdetection(self):
        for button in self.buttons.values():
            button[0] = False
