import pygame
pygame.init()

size = [400, 300]
screen = pygame.display.set_mode(size)

BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
BLUE = (0, 0, 225)
GREEN = (0, 225, 0)
RED = (225, 0, 0)
YELLOW = (225, 225, 0)

img = pygame.image.load('untitled_folder/jiji_copy.PNG')
img = pygame.transform.scale(img, (100, 100))

done = False

while not done:
    screen.fill(WHITE)
    # pygame.draw.rect(screen, RED, (10, 10, 50, 50)) # (x axis, y axis, height, length)
    # pygame.draw.polygon(screen, GREEN, [[200, 150], [150, 200], [250, 200]]) # 각 꼭짓점의 위치
    # pygame.draw.circle(screen, BLUE, [60, 200], 40) #(x axis, y axis (of the centre) and radius/DIA not liekly)
    pygame.draw.polygon(screen, YELLOW, [[200, 125], [150, 200], [250, 200]])
    pygame.draw.polygon(screen, YELLOW, [[200, 225], [150, 150], [250, 150]])

    screen.blit(img, (200, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    pygame.display.update()


    

