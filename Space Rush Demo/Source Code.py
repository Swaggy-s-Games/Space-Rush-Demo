from cmath import rect
import pygame
import random
import time

# intialize the pygame
pygame.init()

# title and stuff
pygame.display.set_caption('Flappy ship by @itsswaggy')
icon = pygame.image.load('Spaceship.png')
pygame.display.set_icon(icon)

# create window
screen = pygame.display.set_mode((800, 600))

# score and stuff
score = -1
font = pygame.font.Font('Bubblegum.ttf', 32)

def show_score():
    score_value = font.render('Score: ' + str(score), True, (255,255,255))
    screen.blit(score_value, (345, 20))

# baground
bg = pygame.image.load('bg.png')

# spaceship
playerImg = pygame.image.load('Spaceship.png')
hitbox = playerImg.get_rect()
vel = 2

# small asteroid
asteroid_smallImg = pygame.image.load('asteroid.png')
hitbox_ = asteroid_smallImg.get_rect()
vel_ = 1

# big asteroid
big_asteroidImg = pygame.image.load('Big_asteroid.png')
hitbox__ = big_asteroidImg.get_rect()
vel__ = 0.5
hitbox__.y = -150

# gameloop
running = True
while running:

    # RGB
    screen.fill((149, 27, 218))
    # bagground
    screen.blit(bg, (0,0))

    # define quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keyboard input
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_RIGHT]:
        hitbox.x += vel
    if userInput[pygame.K_LEFT]:
        hitbox.x -= vel
    if userInput[pygame.K_UP]:
        hitbox.y -= vel
    if userInput[pygame.K_DOWN]:
        hitbox.y += vel

    # movement
    if hitbox_.x >= 20:
        hitbox_.x -= vel_
    
    if hitbox__.x >= 0:
        hitbox__.x -= vel__

    if score == 10:
        hitbox__.y = 112

    if hitbox__.y < 0:
        vel__ = 0

    # player bounderies
    if hitbox.y <= 0:
        hitbox.y = 0
    elif hitbox.y >= 536:
        hitbox.y = 536
        
    if hitbox.x <= 0:
        hitbox.x = 0
    elif hitbox.x >= 736:
        hitbox.x = 736

    # if the asteroid hits the left side, tp back
    if hitbox_.x <= 20:
        hitbox_.x = 736
        hitbox_.y = random.randint(1,536)
        score += 1
        vel_ += 0.1
    
    if score > 9 and hitbox__.x <= 0:
        hitbox__.x = 672
        hitbox__.y = random.randint(1,472)
        score += 1
        vel__ += 0.1

    # define if the hitboxes hit eachother
    if hitbox.colliderect(hitbox_):
        time.sleep(3)
        pygame.quit()

    if hitbox.colliderect(hitbox__):
        time.sleep(3)
        pygame.quit()

    screen.blit(playerImg, hitbox)
    screen.blit(asteroid_smallImg, hitbox_)
    screen.blit(big_asteroidImg, hitbox__)

    # update the window
    show_score()
    pygame.time.delay(3)
    pygame.display.update()    

    
