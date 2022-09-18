from .font_to_dict import clip_font_to_dict
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "..", "..",
        "resources", "font"
    )
)


class NumberFont:
    # Order of characters in font spriteset
    order = [
        "0", "1", "2", "3", "4",
        "5", "6", "7", "8", "9"
    ]

    # Spacing
    character_spacing = 1

    def __init__(self):
        # Get font spriteset
        font_set = pygame.image.load(
            f"{resources_path}/number_font.png")
        font_set.convert()

        # Get characters dictionary
        self.characters = clip_font_to_dict(
            font_set, self.order)

    def render_font(self, display, text, pos, enlarge=1):
        handle_display = pygame.Surface(
            display.get_size(), pygame.SRCALPHA)
        x, y = pos
        x_offset = 0

        # Loop over every character in text
        for char in text:
            # Get character image
            character = self.characters[char]

            # Resize
            if enlarge != 1:
                # Resize character image
                wd, ht = character.get_size()
                resized_character = pygame.transform.scale(
                    character, (wd * enlarge, ht * enlarge))

                # Resize character spacing
                spacing = self.character_spacing * enlarge
            else:
                spacing = self.character_spacing

            # Blit to handle display
            handle_display.blit(
                resized_character, (x + x_offset, y))

            # Add to offset the width of resized character and spacing
            x_offset += resized_character.get_width() + spacing

        # Blit to display
        display.blit(handle_display, (0, 0))
