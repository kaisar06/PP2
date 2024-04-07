import pygame, sys
import pygame.display
from pygame.locals import *
import random, time



pygame.init()

clock = pygame.time.Clock()
#colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#fonts
big_font = pygame.font.SysFont("Verdana", 60)
small_font = pygame.font.SysFont("Verdana", 20)
game_over = big_font.render("Game Over", True, BLACK)

#background
background = pygame.image.load('images/AnimatedStreet.png')

#screen
screen = pygame.display.set_mode((400,600))
screen.fill(WHITE)
pygame.display.set_caption("Racer")

#necessary varibles
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCORE = 0
COINS=0
SPEED = 5

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)

    def move(self):
        global COINS
        self.rect.move_ip(0,SPEED)
        if self.rect.bottom>SCREEN_HEIGHT:
            self.rect.top=0
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)
            self.kill()

coins = pygame.sprite.Group()
def spawn_coin():
    if random.randint(1,100)==1:
        coin=Coin()
        coins.add(coin)
        all_sprites.add(coin)

            

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('images/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40),0)
    
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE+=1
            self.rect.top=0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40),0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left>0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right<SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)


P1=Player()
E1=Enemy()
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)

INC_SPEED = pygame.USEREVENT+1
pygame.time.set_timer(INC_SPEED,1000)




running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
            sys.exit()
        if event.type == INC_SPEED:
            SPEED+=0.5
    
    screen.blit(background, (0,0))
    scores=small_font.render(str(SCORE),True,BLACK)
    screen.blit(scores,(10,10))
    coin_text=small_font.render(str(COINS), True, BLACK)
    screen.blit(coin_text,(380,10))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    spawn_coin()
    
    if pygame.sprite.spritecollide(P1, coins, True):
        COINS+=1

    
    if pygame.sprite.spritecollideany(P1,enemies):
        pygame.mixer.Sound('sounds/crash.wav').play()
        time.sleep(1)

        screen.fill(RED)
        screen.blit(game_over,(30,250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    pygame.display.update()
    clock.tick(60)



    








