import pygame
import time
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tighnari and Kazuya dating sim")
icon = pygame.image.load('genshin.png')
pygame.display.set_icon(icon)
kazuya = pygame.image.load('kazuha.png')
playerX = 500
playerY = 300
thing = pygame.image.load('thing.png')
thingX = 100
thingY = 300
barr = pygame.image.load('bar.png')
barr30 = pygame.image.load('bar30.png')
barr70 = pygame.image.load('bar70.png')
barr100 = pygame.image.load('bar100.png')

love = 0
x = 500
y = 200
xx = 100
xxx = 400
font = pygame.font.Font('freesansbold.ttf', 32)
run_once = 0

def choices(x, y):
    choice = font.render("Left.Step on me pls",True, (0, 0, 0))
    choice1 = font.render("Right.Hey ur cute",True, (0, 0, 0))
    screen.blit(choice, (x, y))
    screen.blit(choice1, (x, 150))


def choices1(x, y):
    choice2 = font.render("Left.I like your ears",True, (0, 0, 0))
    choice3 = font.render("Right.You green like shrek",True, (0, 0, 0))
    screen.blit(choice2, (x, y))
    screen.blit(choice3, (xxx, 150))


def choices2(x, y):
    choice4 = font.render("Left.Do you play amongus",True, (0, 0, 0))
    choice5 = font.render("Right.Wanna step on me?",True, (0, 0, 0))
    screen.blit(choice4, (x, y))
    screen.blit(choice5, (xxx, 150))


def show_response(xx, y):
    response = font.render("they got married",True, (0, 0, 0))
    screen.blit(response, (xx, y))

def show_response1(xx, y):
    response1 = font.render("thanks Kazuya :)",True, (0, 0, 0))
    screen.blit(response1, (xx, y))

def show_response2(xx, y):
    response2 = font.render("Your human ears looks better though",True, (0, 0, 0))
    screen.blit(response2, (xx, y))

def show_response3(xx, y):
    response3 = font.render("yes sure, lets also get married :D",True, (0, 0, 0))
    screen.blit(response3, (xx, y))

def tigh():
    screen.blit(thing, (thingX, thingY))

def player():
    screen.blit(kazuya, (playerX,playerY))

def bar():
    screen.blit(barr, (300, 50))
def bar30():
    screen.blit(barr30, (300, 50))
def bar70():
    screen.blit(barr70, (300, 50))
def bar100():
    screen.blit(barr100, (300, 50))



running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if love == 0:
        bar()
        choices(x, y)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                running = False
            if event.key == pygame.K_RIGHT:
                show_response1(xx, y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                for i in range(1):
                    love = love + 30

    
    if love == 30:
        bar30()
        choices1(x, y)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                show_response2(10, 250)
            if event.key == pygame.K_RIGHT:
                running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                for i in range(1):
                    love = love + 40

    if love == 70:
        bar70()
        choices2(x, y)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                running = False
            if event.key == pygame.K_RIGHT:
                show_response3(10, 250)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                for i in range(1):
                    love = love + 30
                    
    if love == 100:
        show_response(x, y)



    tigh()
    player()
    pygame.display.update()