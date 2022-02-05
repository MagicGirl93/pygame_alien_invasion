import pygame


class GameOver:
    """A class to manage the image 'Game Over'."""

    def __init__(self, ai_game):
        """Initialize 'Game Over' attributes."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the 'Game Over' image and get its rect.
        self.image = pygame.image.load('images/GameOver.bmp')
        self.rect = self.image.get_rect()

        # Place the 'Game Over'.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.center = self.screen_rect.center

        # Initialize 'Game Over'.
        self.end_game = False

    def blitme(self):
        """Draw the 'Game Over' at its current location."""
        self.screen.blit(self.image, self.rect)
