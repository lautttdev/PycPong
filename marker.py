import pygame
from pathlib import Path

class Marker:
    def __init__(self, screen: pygame.Surface):
        self.font_path = Path("Resources") / "fonts" / "PressStart2P.ttf"
        self.font = pygame.font.Font(self.font_path, 16)

        self.screen = screen

        self.player_one_score = 0
        self.player_two_score = 0

        self.text_pos = (self.screen.get_size()[0] / 2, 30)
    

    def update(self):
        text = self.font.render(f"{self.player_one_score} | {self.player_two_score}", False, "white")
        self.screen.blit(text, text.get_rect(center=self.text_pos))