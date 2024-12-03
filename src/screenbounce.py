import pygame

#setup
pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

#ball parametters
ball_color = (255,255,255)
ball_radius = (20)
ballx = screen_width//2
bally = screen_height//2


#gameloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
           running = False
#draw
    screen.fill((50,50,50))
    pygame.draw.circle(screen,ball_color,(ballx,bally),ball_radius)
    
    
    pygame.display.update()
    pygame.display.flip()

pygame.quit()