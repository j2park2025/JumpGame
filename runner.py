import pygame 
import random

from pygame.image import frombuffer 
pygame.init()

size = [400, 300]
screen = pygame.display.set_mode(size)

img = pygame.image.load('jiji_copy.PNG')
img = pygame.transform.scale(img, (100, 100))

BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
BLUE = (0, 0, 225)
GREEN = (0, 225, 0)
RED = (225, 0, 0)
YELLOW = (225, 225, 0)

pygame.display.set_caption("--PYGAME--")

x = 150
y = 200
num = 0
# image, x, y
# draw() 


done = False

jump = False

while not done:
    screen.fill(WHITE)
    key_event = pygame.key.get_pressed()

    if key_event[pygame.K_SPACE]:
        jump = True

    if jump:
        if (y>50):
            y -= 1
        if (y <= 50):
            jump = False
        print(y)
    
    if y < 200 and not jump:        
        y += 1
        print(y)
    
    # if key_event[pygame.K_a]:
    #     y -= 0.5
    # if key_event[pygame.K_s]:
    #     y -= 0.4
    # if key_event[pygame.K_d]:
    #     y -= 0.3
    # if key_event[pygame.K_f]:
    #     y -= 0.2
    # if key_event[pygame.K_g]:
    #     y -= 0.1
    # if key_event[pygame.K_h]:
    #     y += 0
    # if key_event[pygame.K_j]:
    #     y += 0.1
    # if key_event[pygame.K_k]:
    #     y += 0.2
    # if key_event[pygame.K_l]:
    #     y += 0.3
    # if key_event[pygame.KSCAN_SEMICOLON]:
    #     y += 0.4
    # if key_event[pygame.K_QUOTE]:
    #     y += 0.5

    screen.blit(img, (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    pygame.display.update()

pygame.quit()