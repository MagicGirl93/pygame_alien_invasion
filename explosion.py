import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):
    """ A class to represent a single explosion."""

    def __init__(self, ai_game, alien_midtop):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the explosion image and set its rect attribute.
        self.image = pygame.image.load('images/explosion.bmp')
        self.rect = self.image.get_rect()

        # Place the explosion in the alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.midtop = alien_midtop

        # Store the explosion position as a decimal value.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if explosion is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the explosion down the screen."""
        # Update The decimal position of the bullet.
        self.y += self.settings.explosion_speed
        # Update the rect position.
        self.rect.y = self.y
