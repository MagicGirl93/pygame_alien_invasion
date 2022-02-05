import pygame
from pygame.sprite import Sprite


class ShipLevel(Sprite):
    """ A class to represent the number of ships the player has left."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # Load the ship-level image and set its rect attribute.
        self.image = pygame.image.load('images/ship_pink.bmp')
        self.rect = self.image.get_rect()

