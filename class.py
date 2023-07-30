import pygame 
import random


pygame.init()

class Character:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.x = x 
        self.y = y 

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
BLUE = (0, 0, 225)
GREEN = (0, 225, 0)
RED = (225, 0, 0)
YELLOW = (225, 225, 0)
size = [400, 300]
screen = pygame.display.set_mode(size)

charact = Character('jiji_copy.PNG', random, random) 
cats = []
done=False
while not done:
    screen.fill(WHITE)
    
    key_event = pygame.key.get_pressed()
    
    # if key_event[pygame.K_SPACE]:
    x = random.randint(0, 320)
    y = random.randint(0, 210)
    
    # some append some don't??
    perc = random.randint(0, 10)
    if perc<5:
        cats.append(Character('jiji_copy.PNG', x, y)) #random timing 으로 하는거랑

    # percentage = random.randint()
    for i in range(len(cats)-1, -1, -1):
        cats[i].x-=0.1 #cats.x = cats[i]
                     #cats.x = cats.x - 1
        if(cats[i].x < 0):
            del cats[i]
            # cats[i].append()
            # cats.insert(i, )
        else:
            cats[i].draw() #여기가 왜 out of range error 가 뜨는지 확인
    
    # if key_event[pygame.K_LEFT]:
    #     charact.x -= 1

    # if key_event[pygame.K_RIGHT]:
    #     charact.x += 1
    
    # if key_event[pygame.K_UP]:
    #     charact.y -= 1

    # if key_event[pygame.K_DOWN]:
    #     charact.y += 1

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    pygame.display.update()

pygame.quit()