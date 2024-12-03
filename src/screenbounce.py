import pygame
import random

#setup
pygame.init()
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

#ball parametters
ball_color = ((30/5)%256, 255, 255)
ball_radius = (40)
ballx = screen_width//2
bally = screen_height//2
ballx_speed = random.choice([.05,.14])
bally_speed = random.choice([.05,.14])


#gameloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
           running = False

    ballx += ballx_speed
    bally += bally_speed

    if ballx + ball_radius > screen_width or ballx - ball_radius < 0:
        ballx_speed *= -1
    if bally + ball_radius > screen_height or bally - ball_radius < 0:
        bally_speed *= -1
#draw
    screen.fill((50,50,50))
    pygame.draw.circle(screen,ball_color,(ballx,bally),ball_radius)
    
    
    pygame.display.update()
    pygame.display.flip()

pygame.quit()