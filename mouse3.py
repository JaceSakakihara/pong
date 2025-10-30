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
UpText = fontObj.render('Up', True, TEXTCOLOUR, None)
DownText = fontObj.render("Down", True, TEXTCOLOUR, None)
GoodText = fontObj.render("Good", True, TEXTCOLOUR, None)

def word(i):
    if i < 1 and i > 0.5:
        print('good')
    elif i > 1 and i < 2:
        print('ok')
    elif i > 3:
        print("bad")
    elif i < 0.5 and i > 0.1:
        print("excellent")
    elif i < 0.1 and i > 0:
        print("flash")
    elif i == 0:
        print("you're not human...")
def main():
    looping = True
    gameState = 'menu'
    toHit = random.randint(0, 3)
    timer = 0
    timeTaken = 0
    timeToWait = 0
    startButton = pygame.Rect(150, 40, 100, 50)
    leftButton = pygame.Rect(50, 190, 100, 50)
    rightButton = pygame.Rect(250, 190, 100, 50)
    UpButton = pygame.Rect(150, 139, 100, 50)
    DownButton = pygame.Rect(150, 241, 100, 50)
    mouseClicked = False


    while looping:
        startState = 'normal'
        leftState = 'normal'
        rightState = 'normal'
        upState = 'normal'
        DownState = 'normal'


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
                print("Time Taken :" + str(timeTaken))
                toHit = random.randint(0, 3)
                word(timeTaken)
                timer = time.time() + random.randint(2, 5)
        elif leftButton.collidepoint(mouse):
            leftState = 'hover'

        if rightButton.collidepoint(mouse) and mouseClicked:
            rightState = 'clicked'
            if gameState == 'inGame' and toHit == 1 and time.time() > timer:
                timeTaken = time.time() - timer
                print("Time Taken :" + str(timeTaken))
                toHit = random.randint(0, 3)
                word(timeTaken)
                timer = time.time() + random.randint(2, 5)
        elif rightButton.collidepoint(mouse):
            rightState = 'hover'

        if UpButton.collidepoint(mouse) and mouseClicked:
            upState = 'clicked'
            if gameState == 'inGame' and toHit == 2 and time.time() > timer:
                timeTaken = time.time() - timer
                print("Time Taken :" + str(timeTaken))
                toHit = random.randint(0, 3)
                word(timeTaken)
                timer = time.time() + random.randint(2, 5)
        elif UpButton.collidepoint(mouse):
            upState = 'hover'

        if DownButton.collidepoint(mouse) and mouseClicked:
            DownState = 'clicked'
            if gameState == 'inGame' and toHit == 3 and time.time() > timer:
                timeTaken = time.time() - timer
                print("Time Taken :" + str(timeTaken))
                toHit = random.randint(0, 3)
                word(timeTaken)
                timer = time.time() + random.randint(2, 5)
        elif DownButton.collidepoint(mouse):
            DownState = 'hover'



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
            elif toHit == 1:
                WINDOW.blit(rightText, (175, 65))
            elif toHit == 3:
                WINDOW.blit(DownText, (175, 65))
            else:
                WINDOW.blit(UpText, (175, 65))

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

        if upState == 'hover':
            pygame.draw.rect(WINDOW, BUTTON_HOVER, UpButton)
            WINDOW.blit(UpText, (180, 145))
        elif upState == 'clicked':
            pygame.draw.rect(WINDOW, BUTTON_CLICKED, UpButton)
            WINDOW.blit(UpText, (180, 145))
        elif upState == 'normal':
            pygame.draw.rect(WINDOW, BUTTON_NORMAL, UpButton)
            WINDOW.blit(UpText, (180, 145))

        if DownState == 'hover':
            pygame.draw.rect(WINDOW, BUTTON_HOVER, DownButton)
            WINDOW.blit(DownText, (160, 240))
        elif DownState == 'clicked':
            pygame.draw.rect(WINDOW, BUTTON_CLICKED, DownButton)
            WINDOW.blit(DownText, (160, 240))
        elif DownState == 'normal':
            pygame.draw.rect(WINDOW, BUTTON_NORMAL, DownButton)
            WINDOW.blit(DownText, (160, 240))

        pygame.display.update()
        fpsClock.tick(FPS)


main()

