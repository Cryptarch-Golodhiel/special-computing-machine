'''
main.py

Special Computing Machine
(Breakout Game)
E. Rogers & A. Van Dam 2021
'''

# Import the pygame library and intialize the game engine.
import pygame, util
from paddle import Paddle
from ball import Ball
from brick import Brick

pygame.init()

# Define some colors
PIGMENTBLUE = (42, 52, 146)
AUREOLIN = (246, 235, 20)
OFFWHITE = (217, 217, 217)
CINNABAR = (239, 68, 35)
APPLE = (79, 175, 68)
DEEPSAFFRON = (255, 149, 38)
MAGENTA = (255, 0, 127)

# Set up sounds.
startupSound = pygame.mixer.Sound('startup.wav')
brickHitSound = pygame.mixer.Sound('blockHit.wav')

# Set up font.
fontBasic = pygame.font.SysFont(None, 48)
fontItalic = pygame.font.SysFont('Arial', 48, False, True)

score = 0
lives = 500 # ( for testing ;) )# 3

# Open a new window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
#size = (800, 600)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))#size)
pygame.display.set_caption("Breakout Game")

# List of all sprites
all_sprites = pygame.sprite.Group()

# Instantiate the paddle
paddle = Paddle(OFFWHITE, 100, 25)
paddle.rect.x = 350
paddle.rect.y = 560
all_sprites.add(paddle)

# Instantiate the ball
ball = Ball(MAGENTA, 10, 10)
ball.rect.x = 345
ball.rect.y = 560
all_sprites.add(ball)

# Create brick wall
all_bricks = pygame.sprite.Group()
row_spacing = 60
for color in [CINNABAR, DEEPSAFFRON, APPLE, AUREOLIN]:
    for i in range(7):
        brick = Brick(color, 80, 30)
        brick.rect.x = 60 + i * 100
        brick.rect.y = row_spacing
        all_sprites.add(brick)
        all_bricks.add(brick)
    row_spacing += 40

# Display the "Start" Screen
screen.fill(MAGENTA)
startupSound.play()
util.drawText('~*~ BREAKOUT ~*~', fontItalic, screen, (WINDOW_WIDTH / 3), (WINDOW_HEIGHT / 3))
util.drawText('Press any key to start!', fontBasic, screen, (WINDOW_WIDTH / 3) - 30, (WINDOW_HEIGHT / 3) +50)
pygame.display.update()
util.waitForUserKeypress()

# The main program loop
carryOn = True

clock = pygame.time.Clock()

while carryOn:
    # Capturing Events
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT:
            util.terminate()#carryOn = False

    # Move paddle with arrows
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(10)

    # Implementing Game Logic
    all_sprites.update()

    # Check if ball is bouncing? Should this be built into
    # the ball to check its own bounds and change its own
    # velocity? What if I want multiple balls?
    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= 590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, OFFWHITE)
            screen.blit(text, (250, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            carryOn = False
    if ball.rect.y <= 40:
        ball.velocity[1] = -ball.velocity[1]

    # Detect paddle collision
    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()

    # Detect brick collision
    brick_collisions = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collisions:
        ball.bounce()
        brickHitSound.play()
        score += 1
        brick.kill()

        if len(all_bricks) == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, OFFWHITE)
            screen.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            carryOn = False

    # Check y velocity is not 0
    if ball.velocity[1] == 0:
        ball.velocity[1] += 1

    # Refreshing Screen
    screen.fill(PIGMENTBLUE)
    pygame.draw.line(screen, OFFWHITE, [0, 38], [800, 38], 2)
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, OFFWHITE)
    screen.blit(text, (20, 10))

    text = font.render("Lives: " + str(lives), 1, OFFWHITE)
    screen.blit(text, (650, 10))

    # Draw sprites
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
