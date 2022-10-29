from utils import NumberFont, clip_set_to_list_on_xaxis
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


class Score(NumberFont):
    # Initialize
    def __init__(self):
        super().__init__()

        self.init_images()
        self.init_scores()

    def init_images(self):
        # Images
        background_spriteset = pygame.image.load(
            f"{resources_path}/score_background.png")
            
        self.background_imgs = [
            image for image in clip_set_to_list_on_xaxis(background_spriteset)
        ]

        self.title_imgs = clip_set_to_list_on_xaxis(
            pygame.image.load(
                f"{resources_path}/score_title.png"))

        # Positions
        self.background_pos = menu_data["scorebkg_positions"]
        self.title_pos = menu_data["scoretitle_positions"]

    def init_scores(self):
        # Scores
        self.scores = {
            "player": 0,
            "venice": 0
        }

        # Positions
        self.score_pos = menu_data["scoretxt_positions"]

    # Draw
    def draw(self, display):
        # Background
        for img, pos in zip(self.background_imgs, self.background_pos.values()):
            display.blit(img, pos)

        # Title
        for img, pos in zip(self.title_imgs, self.title_pos.values()):
            display.blit(img, pos)

        # Scores
        for score, pos in zip(self.scores.values(), self.score_pos.values()):
            self.render_font(
                display, self.format_score(str(score).zfill(7)), pos)

    # Format function/s
    def format_score(self, score, index=3):
        new_score = score[:-index] + "," + score[-index:]

        index += 4
        if index >= len(new_score):
            return new_score
        else:
            new_score = self.format_score(new_score, index)
            return new_score
