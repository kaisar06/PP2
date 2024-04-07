import pygame
import datetime


pygame.init()

def rot_center(image, angle, x, y):

    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=(x, y))

    return rotated_image, new_rect
clock=pygame.time.Clock()
pygame.display.set_caption('Clock')

done=False

screen=pygame.display.set_mode((800,600))

bg=pygame.image.load('images/background.jpg')
minute_hand=pygame.image.load('images/min.jpg')
second_hand=pygame.image.load('images/sec.jpg')

screen.blit(bg, (0,0))
screen.blit(minute_hand, (250,150))
screen.blit(second_hand, (250,150))

font = pygame.font.Font(None, 64)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    
    now = datetime.datetime.now()
    hours = now.hour
    sec = now.second
    min = now.minute

    clock_display = font.render("{:02d}:{:02d}:{:02d}".format(hours,min, sec), True, (0, 0, 0))

    angle_sec = sec * 6 
    angle_min = min * 6 + (angle_sec) / 60

    sec_hand, rect_sec = rot_center(second_hand, angle_sec, 400, 300)
    min_hand, rect_min = rot_center(minute_hand, angle_min, 400, 300)

    screen.blit(bg, (0,0))
    screen.blit(sec_hand, rect_sec)
    screen.blit(min_hand, rect_min)
    screen.blit(clock_display, (0, 0))
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
