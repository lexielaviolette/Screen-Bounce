import pygame

#setup
pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

#ball parametters

#gameloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
           running = False
#draw
    screen.fill((50,50,50))
    pygame.draw.circle(screen,(255,255,255),(screen_width//2,screen_height//2),20)
    
    
    pygame.display.update()
    pygame.display.flip()

pygame.quit()