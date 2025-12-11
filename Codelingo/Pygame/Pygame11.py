import random
import pygame
import math

screenWidth=800
screenHeight=500
playerStartX=370
playerStartY=380
enemyStartYMin=50
enemyStartYMax=150
enemySpeedX=4
enemySpeedY=40
bulletSpeed=10
collsionDistance=27

pygame.init()
screen=pygame.display.set_mode((screenWidth,screenHeight))
background=pygame.image.load("background.png")
pygame.display.set_caption("Space Invader")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)


playerImage=pygame.image.load("player.png")
playerX=playerStartX
playerY=playerStartY
playerXChange=0

enemyImage=[]
enemyX=[]
enemyY=[]
enemyXChange=[]
enemyYChange=[]
enemyNumber=7
for i in range(enemyNumber):
    enemyImage.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,screenWidth-64))
    enemyY.append(random.randint(enemyStartYMin,enemyStartYMax))
    enemyXChange.append(enemySpeedX)
    enemyYChange.append(enemySpeedY)

bulletImage=pygame.image.load("bullet.png")
bulletX=0
bulletY=playerStartY
bulletXChange=0
bulletYChnage=bulletSpeed
bulletState="Ready"

scoreValue=0
font=pygame.font.Font("freesansbold.ttf", 32)
txtY=10
txtX=10
gameoveFont=pygame.font.Font("freesansbold.ttf", 64)

def showScore(x,y):
    score=font.render("score:"+str(scoreValue), True, pygame.Color("white"))
    screen.blit(score,(x,y))
def gameoverText():
    score=gameoveFont.render("Gameover", True, pygame.Color("white"))
    screen.blit (score, (200,250))
def player(x,y):
    screen.blit(playerImage,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImage[i], (x,y))
def fireBullet(x,y):
    global bulletState
    bulletState="Fire"
    screen.blit(bulletImage,(x+16,y+10))
def bulletColison():
    global bulletY, bulletState, scoreValue
    for i in range(enemyNumber):
        distance = math.sqrt((enemyX[i] - bulletX) ** 2 + (enemyY[i] - bulletY) ** 2)
        if distance < collsionDistance:
            scoreValue += 1                     
            bulletY = playerStartY            
            bulletState = "Ready"               
            enemyX[i] = random.randint(0, screenWidth - 64)
            enemyY[i] = random.randint(enemyStartYMin, enemyStartYMax)
