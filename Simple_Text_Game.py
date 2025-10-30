import pygame, sys, random
from pygame.locals import *

pygame.init()

# Colours
BACKGROUND = (255, 255, 255)
TEXTCOLOUR = (200, 100, 0)
RANDCOLOR = (43, 12, 90)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')

# Set up fonts
fontObj = pygame.font.Font('font/FreckleFace-Regular.ttf', 32)
rightText = fontObj.render('Right', True, TEXTCOLOUR, None)
leftText = fontObj.render('Left', True, TEXTCOLOUR,   RANDCOLOR)
rightTextRectObj = rightText.get_rect()
leftTextRectObj = leftText.get_rect()
# Center the text on the window
rightTextRectObj.center = (WINDOW_WIDTH // 2 + 80, WINDOW_HEIGHT // 2)
leftTextRectObj.center = (WINDOW_WIDTH // 2 + -80, WINDOW_HEIGHT // 2)


# Selects ramdomly either Left or Right
def select_side():
    side = ''
    chosen = random.randint(0, 1)
    if chosen == 1:
        side = 'Right'
    else:
        side = 'Left'

    return side


# The main function that controls the game
def main():
    looping = True

    target = select_side()  # Prime the target before the main loop
    goes = 0  # How many goes the user has had
    score = 0
    rounds = 10  # How many rounds in the game
    active = True  # Used so that the next target won't be set until the user releases the key on the keyboard

    # The main game loop
    while looping:
        sideChosen = ''

        # Get inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pressed = pygame.key.get_pressed()
        if pressed[K_RIGHT]:
            sideChosen = 'Right'
        elif pressed[K_LEFT]:
            sideChosen = 'Left'

        # Processing
        if sideChosen != '' and sideChosen == target and active == True:
            print('Correct')
            goes = goes + 1
            score = score + 1
            active = False
        elif sideChosen == target and active == True:
            print('Incorrect')
            goes = goes + 1
            active = False
        elif active == False and sideChosen == '':  # Enable the next round
            active = True
            target = select_side()

        if goes == rounds:
            looping = False

        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        if target == 'Right' and active == True:
            WINDOW.blit(rightText, rightTextRectObj)
        elif target == 'Left' and active == True:
            WINDOW.blit(leftText, leftTextRectObj)
        pygame.display.update()
        fpsClock.tick(FPS)

    print('Game Over')
    print(f'Your score was : {score} out of 10')


main()
