import pygame 
import random

from pygame.image import frombuffer 
pygame.init()

size = [400, 300]
screen = pygame.display.set_mode(size)

img = pygame.image.load('untitled_folder/jiji_copy.PNG')
img = pygame.transform.scale(img, (100, 100))

BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
BLUE = (0, 0, 225)
GREEN = (0, 225, 0)
RED = (225, 0, 0)
YELLOW = (225, 225, 0)

pygame.display.set_caption("--PYGAME--")

x = 10
y = 10

# image, x, y
# draw() 


done = False

while not done:
    screen.fill(WHITE)
    # pygame.draw.rect(screen, RED, (x, y, 50, 50)) # (x axis, y axis, height, length)
    # print(pygame.mouse.get_pos())
    # x, y = pygame.mouse.get_pos()
    
    key_event = pygame.key.get_pressed()

    if key_event[pygame.K_SPACE]:
        x = random.randint(0, 320)
        y = random.randint(0, 210)

    # if key_event[pygame.K_LEFT]:
    #     x -= 1

    # if key_event[pygame.K_RIGHT]:
    #     x += 1
    
    # if key_event[pygame.K_UP]:
    #     y -= 1

    # if key_event[pygame.K_DOWN]:
    #     y += 1

    screen.blit(img, (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    pygame.display.update()

pygame.quit()