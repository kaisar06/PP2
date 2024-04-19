import pygame

#def draw_rectangle(surface_draw, Colour, (, y, width, height)):
    #pygame.draw.rect(surface_draw,Colour, (x, y, width, height))


pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH,HEIGHT))
baseLayer = pygame.Surface((WIDTH,HEIGHT))
pygame.display.set_caption("paint")

#variables
drawing = True
is_mouse_pressed = False
Last_x=-1
Last_y=-1

#colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
color = RED

#mode
mode = "Rectangle"


while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            drawing = False
        
        # pressing buttons
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = RED
            if event.key == pygame.K_g:
                color = GREEN
            if event.key == pygame.K_b:
                color = BLUE 
            if event.key == pygame.K_0:
                mode = "Rectangle"
            if event.key == pygame.K_1:
                mode = "Circle"
            if event.key == pygame.K_2:
                mode = "Pen"
            if event.key == pygame.K_3:
                mode = "Eraser"

       
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                is_mouse_pressed = True
                X_now,Y_now = event.pos
                X_prev,Y_prev = event.pos
        
        if event.type == pygame.MOUSEMOTION:
            if is_mouse_pressed:
                Last_x,Last_y = event.pos
                if mode == "Rectangle":
                    start_x = min(X_now,Last_x)
                    start_y = min(Y_now,Last_y)
                    width = abs(Last_x-X_now)
                    height = abs(Last_y-Y_now)
                    baseLayer.fill((0, 0, 0, 0))
                    pygame.draw.rect(baseLayer,color,(start_x,start_y,width,height),1)
                elif mode == "Circle":
                    Radius = abs(Last_x-X_now)
                    baseLayer.fill((0, 0, 0, 0))
                    pygame.draw.circle(baseLayer,color,(X_now,Y_now),Radius,1)
                if Last_x!=-1 and Last_y!=-1:
                    pygame.draw.line(baseLayer, color, (X_prev, Y_prev), (Last_x, Last_y), 1)
                    X_prev,Y_prev=Last_x,Last_y
                if mode == "Eraser":
                    if mode == "Eraser":
                        pygame.draw.circle(baseLayer, "Black",(X_now,Y_now),20)

                    
            
            
        if event.type == pygame.MOUSEBUTTONUP:
            is_mouse_pressed = False
            baseLayer.blit(screen, (0, 0))

                        
                        
        
       




    screen.blit(baseLayer,(0,0))
    pygame.display.update()
