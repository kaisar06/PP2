import pygame
import random


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
CELL_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE
FPS = 5  
SCORE_PER_FOOD = 10
FOOD_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)
SPEED_INCREMENT = 0.1  

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.food = self.generate_food()
        self.score = 0
        self.level = 1
        self.speed = FPS

    def generate_food(self):
        while True:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if food not in self.snake:
                return food

    def draw_grid(self):
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, (40, 40, 40), (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, (40, 40, 40), (0, y), (SCREEN_WIDTH, y))

    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, SNAKE_COLOR, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def draw_food(self):
        pygame.draw.rect(self.screen, FOOD_COLOR, (self.food[0] * CELL_SIZE, self.food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def check_collision(self):
        if self.snake[0] in self.snake[1:] or not (0 <= self.snake[0][0] < GRID_WIDTH and 0 <= self.snake[0][1] < GRID_HEIGHT):
            return True
        return False

    def level_up(self):
        if self.score % 30 == 0:
            self.level += 1
            self.speed += SPEED_INCREMENT 
            self.clock.tick(int(self.speed))  

    def reset(self):
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.food = self.generate_food()
        self.score = 0
        self.level = 1
        self.speed = FPS

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != DOWN:
                        self.direction = UP
                    elif event.key == pygame.K_DOWN and self.direction != UP:
                        self.direction = DOWN
                    elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                        self.direction = LEFT
                    elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                        self.direction = RIGHT

           
            x, y = self.snake[0]
            dx, dy = self.direction
            new_head = (x + dx, y + dy)
            self.snake.insert(0, new_head)

      
            if self.check_collision():
                self.reset()
                continue

          
            if new_head == self.food:
                self.score += SCORE_PER_FOOD
                self.food = self.generate_food()
                self.level_up()  
            else:
                self.snake.pop()

            
            self.screen.fill(BACKGROUND_COLOR)
            self.draw_grid()
            self.draw_snake()
            self.draw_food()
            pygame.display.flip()

            
            self.clock.tick(int(self.speed))

        pygame.quit()


if __name__ == "__main__":
    SnakeGame().run()
