import pygame, sys, random
from pygame.locals import *

pygame.init()

# Colours
BACKGROUND = (255, 255, 255)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')


# The main function that controls the game
def main():
    looping = True

    tom = pygame.image.load('images/tom_standing.png').convert_alpha()
    tom = pygame.transform.scale(tom, (50, 95))
    tomX = WINDOW_WIDTH // 2 - 25
    tomY = WINDOW_HEIGHT //2 - 48
    mouseDown = False
    rightmouseDown = False
    mouseReleased = False
    # The main game loop
    while looping:
        # Get inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print('left mouse button down')
                mouseDown = True
                mouseReleased = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                print("left mouse button up")
                mouseDown = False
                mouseReleased = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                print('right mouse button down')
                rightmouseDown = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                print("right mouse button up")
                rightmouseDown = False
         #note:
        # right fast
        mouse = pygame.mouse.get_pos()

        # Processing
        '''print('X coordinate: ', mouse[0], 'Y coordinate:', mouse[1])
        print(mouse)
        '''
        if pygame.mouse.get_focused() == 1 and mouseDown == False:
            if tomX < mouse[0]:
                tomX = tomX + 1
            if tomX > mouse[0]:
                tomX = tomX - 1
            if tomY < mouse[1]:
                tomY = tomY + 1
            if tomY > mouse[1]:
                tomY = tomY - 1
            if mouseReleased == True:
                tomX = WINDOW_WIDTH //2 - 25
                tomY = WINDOW_HEIGHT //2 - 48
                mouseReleased = False
        if pygame.mouse.get_focused() == 1 and rightmouseDown == True:
            if tomX < mouse[0]:
                tomX = tomX + 4
            if tomX > mouse[0]:
                tomX = tomX - 4
            if tomY < mouse[1]:
                tomY = tomY + 4
            if tomY > mouse[1]:
                tomY = tomY - 4
        # This section will be built out later

        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        WINDOW.blit(tom, (tomX, tomY))
        pygame.display.update()
        fpsClock.tick(FPS)


main()