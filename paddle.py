'''
paddle.py

Special Computing Machine
(Breakout Game)
E. Rogers & A. Van Dam 2021
'''

import pygame

BLACK = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        # Pass in the color of the paddle
        # and its x and y position, w & h...
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle as a rectangle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of
        # the image
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # Check for out of bounds
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # Check for out of bounds
        if self.rect.x > 700:
            self.rect.x = 700
