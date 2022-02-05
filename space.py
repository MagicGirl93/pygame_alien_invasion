import pygame


class Space:
    """A class to manage the space."""

    def __init__(self, ai_game):
        """Initialize the space and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the space image and get its rect.
        self.image = pygame.image.load('images/space.bmp')
        self.rect = self.image.get_rect()

    def blitme(self):
        """Draw the space at its current location."""
        self.screen.blit(self.image, self.rect)
