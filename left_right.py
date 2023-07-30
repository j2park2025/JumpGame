import pygame

pygame.display.set_mode((600,450)) 
pygame.display.set_caption("Day1")
done = False
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                done = True                
            elif event.key == pygame.K_LEFT:
                done = True

pygame.quit()

