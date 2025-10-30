import pygame, sys, random, time
from pygame.locals import *

pygame.init()

# Colours
BACKGROUND = (255, 255, 255)
BUTTON_NORMAL = (255, 100, 100)
BUTTON_HOVER = (100, 255, 100)
BUTTON_CLICKED = (100, 100, 255)
TEXTCOLOUR = (0, 0, 0)

FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')

fontObj = pygame.font.Font('font/FreckleFace-Regular.ttf', 32)
startText = fontObj.render('Start', True, TEXTCOLOUR, None)
leftText = fontObj.render('Left', True, TEXTCOLOUR, None)
rightText = fontObj.render('Right', True, TEXTCOLOUR, None)

def main():
    looping = True
    gameState = 'menu'
    toHit = random.randint(0, 1)  # 0 = Left, 1 = Right
    timer = 0
    timeTaken = 0
    timeToWait = 0

    startButton = pygame.Rect(150, 40, 100, 50)
    leftButton = pygame.Rect(50, 190, 100, 50)
    rightButton = pygame.Rect(250, 190, 100, 50)
    mouseClicked = False

    while looping:
        startState = 'normal'
        leftState = 'normal'
        rightState = 'normal'

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouseClicked = False

        mouse = pygame.mouse.get_pos()

        if startButton.collidepoint(mouse) and mouseClicked:
            startState = 'clicked'
            gameState = 'inGame'
            timer = time.time() + random.randint(2, 5)
        elif startButton.collidepoint(mouse):
            startState = 'hover'

        if leftButton.collidepoint(mouse) and mouseClicked:
            leftState = 'clicked'
            if gameState == 'inGame' and toHit == 0 and time.time() > timer:
                timeTaken = time.time() - timer
                print(f"Time Taken :" + str(timeTaken))
                toHit = random.randint(0, 1)
                timer = time.time() + random.randint(2, 5)
        elif leftButton.collidepoint(mouse):
            leftState = 'hover'

        if rightButton.collidepoint(mouse) and mouseClicked:
            rightState = 'clicked'
            if gameState == 'inGame' and toHit == 1 and time.time() > timer:
                timeTaken = time.time() - timer
                print("Time Taken :" + str(timeTaken))
                toHit = random.randint(0, 1)
                timer = time.time() + random.randint(2, 5)
        elif rightButton.collidepoint(mouse):
            rightState = 'hover'


        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        if startState == 'hover' and gameState == 'menu':
            pygame.draw.rect(WINDOW, BUTTON_HOVER, startButton)
            WINDOW.blit(startText, (175, 55))
        elif startState == 'clicked' and gameState == 'menu':
            pygame.draw.rect(WINDOW, BUTTON_CLICKED, startButton)
            WINDOW.blit(startText, (175, 55))
        elif startState == 'normal' and gameState == 'menu':
            pygame.draw.rect(WINDOW, BUTTON_NORMAL, startButton)
            WINDOW.blit(startText, (175, 55))

        if gameState == 'inGame' and time.time() > timer:
            if toHit == 0:
                WINDOW.blit(leftText, (175, 65))
            else:
                WINDOW.blit(rightText, (175, 65))

        if leftState == 'hover':
            pygame.draw.rect(WINDOW, BUTTON_HOVER, leftButton)
            WINDOW.blit(leftText, (80, 205))
        elif leftState == 'clicked':
            pygame.draw.rect(WINDOW, BUTTON_CLICKED, leftButton)
            WINDOW.blit(leftText, (80, 205))
        elif leftState == 'normal':
            pygame.draw.rect(WINDOW, BUTTON_NORMAL, leftButton)
            WINDOW.blit(leftText, (80, 205))

        if rightState == 'hover':
            pygame.draw.rect(WINDOW, BUTTON_HOVER, rightButton)
            WINDOW.blit(rightText, (270, 205))
        elif rightState == 'clicked':
            pygame.draw.rect(WINDOW, BUTTON_CLICKED, rightButton)
            WINDOW.blit(rightText, (270, 205))
        elif rightState == 'normal':
            pygame.draw.rect(WINDOW, BUTTON_NORMAL, rightButton)
            WINDOW.blit(rightText, (270, 205))

        pygame.display.update()
        fpsClock.tick(FPS)


main()