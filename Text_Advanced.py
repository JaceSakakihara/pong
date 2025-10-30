import pygame, sys, random
from pygame.locals import *

pygame.init()

# Colours
BACKGROUND = (255, 255, 255)
TEXTCOLOUR = (200, 100, 0)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')

BOTTOMLINEHEIGHT = 20

# Set up fonts
fontObj = pygame.font.Font(None, 32)
textSufaceObj = fontObj.render('blah blah', True, TEXTCOLOUR, None)
textRectObj = textSufaceObj.get_rect()
textRectObj = textSufaceObj.get_rect()
textRectObj.midbottom = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - BOTTOMLINEHEIGHT - 15)


# The main function that controls the game
def main():
    looping = True

    # The main game loop
    while looping:
        # Get inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Processing
        # This section will be built out later

        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        WINDOW.blit(textSufaceObj, textRectObj)
        pygame.draw.line(WINDOW, TEXTCOLOUR, (0, WINDOW_HEIGHT - BOTTOMLINEHEIGHT), (WINDOW_WIDTH, WINDOW_HEIGHT - BOTTOMLINEHEIGHT), 3)
        pygame.display.update()
        fpsClock.tick(FPS)


main()
