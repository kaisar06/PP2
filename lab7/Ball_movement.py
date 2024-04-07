import pygame

pygame.init()
clock = pygame.time.Clock()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("red ball")

x=250
y=250

running = True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.circle(screen, 'Red', (x,y), 25)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y-=20
    if pressed[pygame.K_DOWN]:
        y+=20
    if pressed[pygame.K_LEFT]:
        x-=20
    if pressed[pygame.K_RIGHT]:
        x+=20
    

    x = max(25, min(x, 475))
    y = max(25, min(y, 475))

    clock.tick(25)
    pygame.display.update()

pygame.quit()
