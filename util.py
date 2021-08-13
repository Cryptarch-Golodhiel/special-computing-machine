'''
util.py

Special Computing Machine
(Breakout Game)
E. Rogers & A. Van Dam 2021
'''

# Functions borrowed from A. Sweigart (https://www.nostarch.com/inventwithpython)

import pygame, sys

TEXTCOLOR = (0, 0, 0)

def terminate():
    pygame.quit()
    sys.exit()

def waitForUserKeypress():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # Pressing ESC quits
                    terminate()
                return

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
