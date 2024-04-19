import pygame
import random

#initialization
pygame.init()

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#dimensions
WIDTH = 800
HEIGHT = 600

#block size
block_size = 25

#speed of snake
snake_speed = 7

#display
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake")

#game speed
Clock = pygame.time.Clock()

#font of text
font = pygame.font.SysFont(None,25)

def drawgrid():
    for x in range(0, WIDTH, block_size):
        pygame.draw.line(screen, BLACK, (x,0), (x,HEIGHT))
    for y in range(0, HEIGHT, block_size):
        pygame.draw.line(screen, BLACK, (0,y), (WIDTH,y))


def mainloop():
    gameover = False
    gameclose = False

    #main coordinates of snake^s head
    lead_x = 400
    lead_y = 300

    # Set initial movement direction of the snake
    lead_x_change = 0
    lead_y_change = 0

    # Set initial length of the snake
    snake_list = []
    snake_length = 1

    #random coordinates of food
    rand_food_x = round(random.randrange(0,775)/25)*25
    rand_food_y = round(random.randrange(0,575)/25)*25

    #initialize score
    SCORE = 0

    while not gameover:

        while gameclose == True:
            screen.fill(WHITE)
            screen_text = font.render("Game over, press C to play again or Q to quit", True, RED)
            screen.blit(screen_text,(100, 100))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameover = True
                        gameclose = False
                    if event.key == pygame.K_c:
                        mainloop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_x_change = 0
                    lead_y_change = -block_size
                elif event.key == pygame.K_DOWN:
                    lead_x_change = 0
                    lead_y_change = block_size
        
        if lead_x>=WIDTH or lead_x < 0 or lead_y>=HEIGHT or lead_y < 0:
            gameclose = True 
        lead_x += lead_x_change
        lead_y += lead_y_change
        screen.fill(WHITE)
        drawgrid()
        pygame.draw.rect(screen,GREEN, [rand_food_x,rand_food_y,block_size,block_size])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list)>snake_length:
            del snake_list[0]
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True
        #draw snake
        for segment in snake_list:
            pygame.draw.rect(screen, BLACK, [segment[0], segment[1], block_size, block_size])
        
        #display score
        score_text = font.render("Score: " + str(SCORE),True,BLACK)
        screen.blit(score_text,(10,10))

        pygame.display.update()

        if lead_x == rand_food_x and lead_y == rand_food_y:
            rand_food_x = round(random.randrange(0,778)/25)*25
            rand_food_y = round(random.randrange(0,575)/25)*25
            snake_length += 1
            SCORE += 1
        Clock.tick(snake_speed)

    pygame.quit()
    quit()



mainloop()




                
