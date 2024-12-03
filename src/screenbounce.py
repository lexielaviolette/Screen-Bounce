import pygame

#setup
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#ball parametters


#draw
screen.fill((50,50,50))
pygame.draw.circle(screen,(255,255,255),(screen/2,screen/2),20)
pygame.display.flip()