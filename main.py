# Import the pygame library and intialize the game engine.
import pygame
from paddle import Paddle

# Start your engines
pygame.init()

# Define some colors
DARKBLUE = (0, 63, 99)
YELLOW = (242, 177, 56)
WHITE = (217, 217, 217)
GREY = (161, 165, 166)
CHARCOAL = (53, 61, 64)
GREEN = (102, 140, 74)
ORANGE = (242, 100, 41)

score = 0
lives = 3

# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

# List of all sprites
all_sprites = pygame.sprite.Group()

# Instantiate the paddle
paddle = Paddle(WHITE, 100, 25)
paddle.rect.x = 350
paddle.rect.y = 560

all_sprites.add(paddle)

# The main program loop
carryOn = True

clock = pygame.time.Clock()

while carryOn:
    # Capturing Events
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT:
            carryOn = False

    # Move paddle with arrows
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)

    # Implementing Game Logic
    all_sprites.update()

    # Refreshing Screen
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20, 10))

    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650, 10))

    # Draw sprites
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()