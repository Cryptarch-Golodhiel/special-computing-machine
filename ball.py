'''
ball.py

Special Computing Machine
(Breakout Game)
E. Rogers & A. Van Dam 2021
'''

import pygame
import random
from random import randint

BLACK = (0, 0, 0)

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [randint(4, 8), randint(-9, 7) + 1]
        
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.choice([randint(-8, 0), randint(1,8)])
