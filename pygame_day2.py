import pygame
pygame.init()

screen = pygame.display.set_mode((500,350)) 
pygame.display.set_caption("background")
background = pygame.image.load('baegyeong.png')
background = pygame.transform.scale(background,(500,350))
player = pygame.image.load('jiji.png')
player = pygame.transform.scale(player,(70,70))
# screen.fill([180, 200, 215]) 
# pygame.display.update() 

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(background, (0,0))
    screen.blit(player, (200,188))
    pygame.display.update()         
        