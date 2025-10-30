import pygame, sys, random, time, math
from pygame.locals import *

pygame.init()
#PAUSE work on paudse
# Colours
BACKGROUND = (129, 136, 138)
TEXTCOLOUR = (0, 0, 0)
BALLCOLOUR = (149, 5, 227)
PADDLELEFTCOLOUR = (15, 215, 255)
PADDLERIGHTCOLUR = (227, 5, 5)
BOARDCOLUR = (100, 100 ,100)

PADDLEINSET = 20
PADDLEWIDTH = 10
PADDLEHEIGHT = 60
BALLSIZE = 10
GAMEROUNDS = 5
BOARDTOPSPACING = 40
BOARDBOTTOMSPACING = 20




# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong')

def splash_screen():
    font = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 32)
    text = font.render('PONG', True, TEXTCOLOUR)
    textRect = text.get_rect()
    textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    WINDOW.fill(BACKGROUND)
    WINDOW.blit(text, textRect)
    pygame.display.update()
    time.sleep(1.7)
    return "menu"

def menu_screen():
    looping = True
    action = "game"
    font = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 32)
    fontTitle = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 64)
    title = fontTitle.render("PONG", True, TEXTCOLOUR)
    menuItem1 = font.render('Instructions - i', True, TEXTCOLOUR)
    menuItem2 = font.render("Play Game - p or SPACE", True, TEXTCOLOUR)
    menuItem3 = font.render('Quit - q', True, TEXTCOLOUR)
    titleRect = title.get_rect()
    menuItem1Rect = menuItem1.get_rect()
    menuItem2Rect = menuItem2.get_rect()
    menuItem3Rect = menuItem3.get_rect()
    titleRect.center = (WINDOW_WIDTH // 2, 100)
    menuItem1Rect.topleft = (200, 200)
    menuItem2Rect.topleft = (200, 300)
    menuItem3Rect.topleft = (200, 400)

    while looping:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pressed = pygame.key.get_pressed()
        if pressed[K_b]:
            action = 'menu'
            looping = False
        elif pressed[K_SPACE] or pressed[K_p]:
            action = 'game'
            looping = False

        WINDOW.fill(BACKGROUND)
        WINDOW.blit(title, titleRect)
        WINDOW.blit(menuItem1, menuItem1Rect)
        WINDOW.blit(menuItem2, menuItem2Rect)
        WINDOW.blit(menuItem3, menuItem3Rect)
        pygame.display.update()
        fpsClock.tick(FPS)
    return action


def instructions_screen():
    looping = True
    action = 'game'
    font = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 32)
    fontTitle = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 64)
    title = fontTitle.render("PONG", True, TEXTCOLOUR)
    menuItem1 = font.render('Instructions', True, TEXTCOLOUR)
    menuItem2 = font.render("Content coming soon", True, TEXTCOLOUR)
    menuItem3 = font.render("Back - b, Play game - g or SPACE", True, TEXTCOLOUR)
    titleRect = title.get_rect()
    menuItem1Rect = menuItem1.get_rect()
    menuItem2Rect = menuItem2.get_rect()
    menuItem3Rect = menuItem3.get_rect()
    titleRect.center = (WINDOW_WIDTH // 2, 100)
    menuItem1Rect.topleft = (200, 200)
    menuItem2Rect.topleft = (200, 300)
    menuItem3Rect.topleft = (200, 400)
    while looping:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pressed = pygame.key.get_pressed()
        if pressed[K_b]:
            action = 'menu'
            looping = False
        elif pressed[K_SPACE] or pressed[K_p]:
            action = "game"
            looping = False

        WINDOW.fill(BACKGROUND)
        WINDOW.blit(title, titleRect)
        WINDOW.blit(menuItem1, menuItem1Rect)
        WINDOW.blit(menuItem2, menuItem2Rect)
        WINDOW.blit(menuItem3, menuItem3Rect)
        pygame.display.update()
        fpsClock.tick(FPS)
    return action

def goodbye_screen():
    font = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 32)
    text = font.render('Pong', True, TEXTCOLOUR)
    goodbyeText = font.render('See you soon...', True, TEXTCOLOUR)
    textRect = text.get_rect()
    goodbyeTextRect = goodbyeText.get_rect()
    textRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)
    goodbyeTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 50)

    WINDOW.fill(BACKGROUND)
    WINDOW.blit(text, textRect)
    WINDOW.blit(goodbyeText, goodbyeTextRect)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    sys.exit()
    return 'menu'


# The main function that controls the game


def process_paddle (paddleY, paddleMomentum):
    newPaddleY = paddleY
    newPaddleMomentum = paddleMomentum
    newPaddleY = newPaddleY + (newPaddleMomentum // 5)
    if newPaddleMomentum > 0:
        newPaddleMomentum = newPaddleMomentum - 1
    if newPaddleMomentum < 0:
        newPaddleMomentum = newPaddleMomentum + 1
    if newPaddleY < BOARDBOTTOMSPACING:
        newPaddleY = BOARDBOTTOMSPACING + 5
    if newPaddleY > WINDOW_HEIGHT - BOARDBOTTOMSPACING - PADDLEHEIGHT:
        newPaddleY = WINDOW_HEIGHT - BOARDBOTTOMSPACING - PADDLEHEIGHT - 5

    return newPaddleY, newPaddleMomentum

def process_ball(ballCoordinates, ballAngle, ballmomentum, leftPaddleY, rightPaddleY):
    goal = False
    newBallAngle = ballAngle

    ballCoordinates[0] = ballCoordinates[0] + (ballmomentum * math.sin(math.radians(ballAngle)))
    ballCoordinates[1] = ballCoordinates[1] + (ballmomentum * math.cos(math.radians(ballAngle)))
    if ballCoordinates[1] < BOARDTOPSPACING + (BALLSIZE):
        ballCoordinates[1] = BOARDTOPSPACING + (BALLSIZE) + 1
        newBallAngle = (180 - ballAngle) % 360
    if ballCoordinates[1] > WINDOW_HEIGHT - BOARDBOTTOMSPACING - (BALLSIZE):
        ballCoordinates[1] = WINDOW_HEIGHT - BOARDBOTTOMSPACING - (BALLSIZE) - 1
        newBallAngle = (180 - ballAngle) % 360
    if ballCoordinates[0] > WINDOW_WIDTH - BALLSIZE - PADDLEINSET - PADDLEWIDTH:
        if ballCoordinates[1] > rightPaddleY and ballCoordinates[1] < rightPaddleY + PADDLEHEIGHT:
            ballCoordinates[0] = WINDOW_WIDTH - BALLSIZE - PADDLEINSET - PADDLEWIDTH - 1
            angleMultiplier = (rightPaddleY - ballCoordinates[1])
            newBallAngle = ((360 - newBallAngle) % 360) - angleMultiplier
    if ballCoordinates[0] < BALLSIZE + PADDLEINSET + PADDLEWIDTH:
        if ballCoordinates[1] > leftPaddleY and ballCoordinates[1] < leftPaddleY + PADDLEHEIGHT:
            ballCoordinates[0] = BALLSIZE + PADDLEINSET + PADDLEWIDTH + 1
            angleMultiplier = (leftPaddleY - ballCoordinates[1])
            newBallAngle = ((360 - newBallAngle) % 360) + angleMultiplier
    if ballCoordinates[0] < BALLSIZE:
        ballCoordinates[0] = WINDOW_WIDTH // 2
        goal ='right'
    if ballCoordinates[0] > WINDOW_WIDTH - BALLSIZE:
        ballCoordinates[0] = WINDOW_WIDTH // 2
        goal = 'left'
    return ballCoordinates, ballmomentum, newBallAngle, goal

def render_board():
    pygame.draw.line(WINDOW, BOARDCOLUR, (0, BOARDTOPSPACING), (WINDOW_WIDTH, BOARDTOPSPACING), 3)
    pygame.draw.line(WINDOW, BOARDCOLUR, (0, WINDOW_HEIGHT - BOARDBOTTOMSPACING), (WINDOW_WIDTH, WINDOW_HEIGHT - BOARDBOTTOMSPACING), 3)
    pygame.draw.line(WINDOW, BOARDCOLUR, ((WINDOW_WIDTH // 2) - 1, BOARDTOPSPACING), ((WINDOW_WIDTH // 2) - 1, WINDOW_HEIGHT - BOARDBOTTOMSPACING), 2)
    return True

def render_scores (playerLeftScore, playerRightScore):
    render_scores_side(playerLeftScore, "left")
    render_scores_side(playerRightScore, "right")

def render_scores_side(playerScore, side):
    yCoord = 20
    xCoord = 30
    xCoordAdd = 20
    if side == "right":
        xCoord = WINDOW_WIDTH - 30
        xCoordAdd = -20
    radius = 7
    counter = 1
    while counter <= 3:
        if playerScore < counter:
            pygame.draw.circle(WINDOW, BOARDCOLUR, (xCoord, yCoord), radius, 2)
        else:
            pygame.draw.circle(WINDOW, BOARDCOLUR, (xCoord, yCoord), radius)
        counter = counter + 1
        xCoord = xCoord + xCoordAdd
    return True
def render_paddle(side, y):
    if side == 'left':
        x = PADDLEINSET
    else:
        x = WINDOW_WIDTH - PADDLEINSET - PADDLEWIDTH
    paddleRect = pygame.Rect(x, y, PADDLEWIDTH, PADDLEHEIGHT)
    pygame.draw.rect(WINDOW,PADDLELEFTCOLOUR, paddleRect)
    return True

def render_ball (ballCoordinates):
    pygame.draw.circle(WINDOW, BALLCOLOUR, (int(ballCoordinates[0]), int(ballCoordinates[1])), BALLSIZE)
    return True

def game_screen():
    winner = ''
    looping = True
    action = 'game over'
    leftPaddleMomentum = 0
    rightPaddleMomentum = 0
    leftPaddleY = 200
    rightPaddleY = 400
    ballCoordinates = [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]
    ballMomentum = 5
    ballAngle = 150
    playerLeftScore = 0
    playerRightScore = 0
    goal = False
    while looping:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pressed = pygame.key.get_pressed()
        if pressed[K_w]:
            leftPaddleMomentum -= 2
        elif pressed[K_s]:
            leftPaddleMomentum += 2
        if pressed[K_UP]:
            rightPaddleMomentum -= 2
        elif pressed[K_DOWN]:
            rightPaddleMomentum += 2
        if pressed[K_SPACE]:
            start = 'go'
        if pressed[K_q]:
            action = 'menu'
            looping = False
        leftPaddleY, leftPaddleMomentum = process_paddle(leftPaddleY, leftPaddleMomentum)
        rightPaddleY, rightPaddleMomentum = process_paddle(rightPaddleY, rightPaddleMomentum)
        ballCoordinates, ballMomentum, ballAngle, goal = process_ball(ballCoordinates, ballAngle, ballMomentum, leftPaddleY, rightPaddleY)
        if goal == 'left':
            playerLeftScore = playerLeftScore + 1
            ballAngle = 150
            if playerLeftScore >= 3:
                winner = 'left'
                looping = False
        elif goal == 'right':
            playerRightScore = playerRightScore + 1
            ballAngle = 330
            if playerRightScore >= 3:
                winner = 'right'
                looping = False

        WINDOW.fill(BACKGROUND)
        render_board()
        render_scores(playerLeftScore, playerRightScore)
        render_ball(ballCoordinates)
        render_paddle('left', leftPaddleY)
        render_paddle('right', rightPaddleY)
        pygame.display.update()
        fpsClock.tick(FPS)

    time.sleep(0.5)
    return action, winner

def game_over_screen(winner):
    looping = True
    action = 'game'
    font = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 32)
    fontTitle = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 64)

    title = fontTitle.render('PONG', True, TEXTCOLOUR)
    menuItem1 = font.render('Game over', True, TEXTCOLOUR)
    menuItem2 = font.render(f'Player {winner} wins!!', True, TEXTCOLOUR)
    menuItem3 = font.render('Play again - p or SPACE, Menu - b', True, TEXTCOLOUR)

    titleRect = title.get_rect()
    menuItem1Rect = menuItem1.get_rect()
    menuItem2Rect = menuItem2.get_rect()
    menuItem3Rect = menuItem3.get_rect()

    titleRect.center = (WINDOW_WIDTH // 2, 100)
    menuItem1Rect.topleft = (200, 200)
    menuItem2Rect.topleft = (200, 300)
    menuItem3Rect.topleft = (200, 400)

    while looping:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        pressed = pygame.key.get_pressed()
        if pressed[K_b]:
            action = 'menu'
            looping = False
        elif pressed[K_SPACE] or pressed[K_p]:
            action = 'game'
            looping = False
        elif pressed[K_q]:
            action = 'bye'
            looping = False

        WINDOW.fill(BACKGROUND)
        WINDOW.blit(title, titleRect)
        WINDOW.blit(menuItem1, menuItem1Rect)
        WINDOW.blit(menuItem2, menuItem2Rect)
        WINDOW.blit(menuItem3, menuItem3Rect)
        pygame.display.update()
        fpsClock.tick(FPS)
    return action

def main():
    looping = True

    screen = 'splash'
    winner = ""
    # The main game loop
    while looping:
        # Get inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Processing
        if screen == 'splash':
            screen = splash_screen()
        elif screen == 'menu':
            screen = menu_screen()
        elif screen == 'game':
            screen, winner = game_screen()
        elif screen == "game_over":
            screen = game_over_screen(winner)
        elif screen == 'instructions':
            screen = instructions_screen()
        else:
            screen = goodbye_screen()

        # This section will be built out later

        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()