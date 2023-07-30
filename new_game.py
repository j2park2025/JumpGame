
import pygame 
pygame.init()

size = (400, 300)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("--PYGAME--")

done= False

while not done:
    screen.fill((225,225,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    pygame.display.update()

pygame.quit()