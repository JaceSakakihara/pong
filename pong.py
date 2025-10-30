import pygame, sys, random
import time
from pygame.locals import *
pygame.init()

BACKGROUND = (77, 77, 77)
ELEMENTCOLOUR = (0, 0, 0)
ELEMENTCOLOUR1 = (15, 215, 255)
ELEMENTCOLOUR2 = (227, 5, 5)
ELEMENTCOLOUR3 = (149, 5, 227)






FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("pong")

PADDLEINSET = 20
PADDLEWIDTH = 10
PADDLEHEIGHT = 60
BALLSIZE = 10
def main():
    looping = True
    Rscore = 0
    Lscore = 0
    leftPaddleY = 50
    rightPaddleY = 50
    ballY = WINDOW_HEIGHT // 2
    ballX = WINDOW_WIDTH // 2
    momentum = 1
    pause = False
    ballXMomentum = momentum
    ballYMomentum = momentum
    def faster(i):
        i = i + 1
        return i


    while looping:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    latestmomentum = momentum
                    pause = not pause
#                    print("Pausing")
#        print(pause)
        if pause == True:
            #ballXMomentum = latestmomentumX
            #ballYMomentum = latestmomentumY  # work on Pause momentum
            pausegame = fontObj.render("Pause", True, ELEMENTCOLOUR3, None)
            WINDOW.blit(pausegame, (350, 270))
            pygame.display.update()
            continue



        fontObj = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 32)
        leftscore = fontObj.render("Left: " + str(Lscore), True, ELEMENTCOLOUR1, None)
        rightscore = fontObj.render("Right: " + str(Rscore), True, ELEMENTCOLOUR2, None)


        pressed = pygame.key.get_pressed()
        if pressed[K_w]:
            leftPaddleY -= 9
        elif pressed[K_s]:
            leftPaddleY += 9
        if pressed[K_UP]:
            rightPaddleY -= 9
        elif pressed[K_DOWN]:
            rightPaddleY += 9
#        if pressed[K_p]:
#            latestmomentum = momentum
#            ballYMomentum = 0
#            ballXMomentum = 0
#            pause = True
#            if pressed[K_p]:
#                pause = False
#                momentum = latestmomentum

#        if pressed[K_p]:
#            latestmomentum = momentum
#            ballYMomentum = 0
#            ballXMomentum = 0
#            pause = True
#            print("Pauesing")
#            WINDOW.blit(pausegame, (350, 270))
#            if pause == True:
#                if pressed[K_p]:
#                    ballXMomentum = latestmomentumX
#                    ballYMomentum = latestmomentumY#work on Pause momentum
#                    pause = False



#            pause = True
#            time.sleep(pressed[K_p])








#        print(ballXMomentum, ballYMomentum)
        ballX = ballX + ballXMomentum
        ballY = ballY + ballYMomentum



        WINDOW.fill(BACKGROUND)
        WINDOW.blit(leftscore, (20, 10))
        WINDOW.blit(rightscore, (670, 10))
        pygame.draw.line(WINDOW, ELEMENTCOLOUR, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT))
        if ballX <= BALLSIZE:
            momentum = 1
            latestmomentum = 1
            ballX = WINDOW_WIDTH // 2
            ballY = WINDOW_HEIGHT // 2
            ballYMomentum = momentum
            ballXMomentum = momentum
            Rscore = Rscore + 1
        if ballX >= WINDOW_WIDTH - BALLSIZE:
            momentum = 1
            latestmomentum = 1
            ballX = WINDOW_WIDTH // 2
            ballY = WINDOW_HEIGHT // 2
            ballYMomentum = momentum
            ballXMomentum = -momentum
            Lscore = Lscore + 1

        if ballX <= PADDLEINSET + PADDLEWIDTH and ballX > PADDLEINSET:
            if leftPaddleY < ballY and leftPaddleY + PADDLEHEIGHT > ballY:
                ballXMomentum = momentum
                momentum = faster(momentum)
        if ballX >= WINDOW_WIDTH - PADDLEINSET - PADDLEWIDTH and ballX < WINDOW_WIDTH - PADDLEINSET:
            if rightPaddleY < ballY and rightPaddleY + PADDLEHEIGHT > ballY:
                ballXMomentum = -momentum
                momentum = faster(momentum)
        leftPaddleRect = pygame.Rect(PADDLEINSET, leftPaddleY, PADDLEWIDTH, PADDLEHEIGHT)
        rightPaddleRect = pygame.Rect(WINDOW_WIDTH - PADDLEINSET - PADDLEWIDTH, rightPaddleY, PADDLEWIDTH, PADDLEHEIGHT)
        pygame.draw.rect(WINDOW, ELEMENTCOLOUR1, leftPaddleRect)
        pygame.draw.rect(WINDOW, ELEMENTCOLOUR2, rightPaddleRect)
        if leftPaddleY < 0:
            leftPaddleY = 0
        if leftPaddleY > WINDOW_HEIGHT - PADDLEHEIGHT:
            leftPaddleY = WINDOW_HEIGHT - PADDLEHEIGHT
        if rightPaddleY < 0:
            rightPaddleY = 0
        if rightPaddleY > WINDOW_HEIGHT - PADDLEHEIGHT:
            rightPaddleY = WINDOW_HEIGHT - PADDLEHEIGHT
        if ballY < BALLSIZE:
            ballYMomentum = momentum
        if ballY > WINDOW_HEIGHT - BALLSIZE:
            ballYMomentum = -momentum
        pygame.draw.circle(WINDOW, ELEMENTCOLOUR3, (int(ballX), int(ballY)), BALLSIZE)
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()
