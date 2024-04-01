import pygame as pg
import random,time

# Инициализация Pygame
pg.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH /CELL_SIZE
GRID_HEIGHT = HEIGHT / CELL_SIZE

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Создание экрана
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Змейка")

clock = pg.time.Clock()
level=1
font=pg.font.SysFont("comicsansms",20)
font_big=pg.font.SysFont("comicsansms",56)
status="Нуб"
game_over=font_big.render("Game Over",1,"red")
score=0


# Функция отрисовки змейки и яблока
def draw_objects(snake, apple):
    screen.fill(WHITE)
    for segment in snake:
        pg.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pg.draw.rect(screen, RED, (apple[0] * CELL_SIZE, apple[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    

# Главная функция игры

snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
direction = pg.Vector2(1, 0)
apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
fps=6

running =True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_UP] and direction.y != 1:  
        direction = pg.Vector2(0, -1)
    elif keys[pg.K_DOWN] and direction.y != -1:  
        direction = pg.Vector2(0, 1)
    elif keys[pg.K_LEFT] and direction.x != 1:  
        direction = pg.Vector2(-1, 0)
    elif keys[pg.K_RIGHT] and direction.x != -1: 
        direction = pg.Vector2(1, 0)

    snake_head = snake[0] + direction
    if snake_head[0] < 0 or snake_head[0] >= GRID_WIDTH or snake_head[1] < 0 or snake_head[1] >= GRID_HEIGHT or snake_head in snake:
        screen.fill(WHITE)
        screen.blit(game_over, (250, 240))
        screen.blit(font.render(f"Вы дошли до {level} уровня", True, GREEN), (250, 380))

        if level == 2:
            status = "Любитель"
        elif level == 3:
            status = "Профи"
        elif level == 4:
            status = "Сумасшедший"
        elif level>=5:
            status = "Читер"
        screen.blit(font_big.render(f"Ваш статус: {status}", True, GREEN), (150, 140))
        pg.display.flip()
        time.sleep(2)
        
        running= False

    snake.insert(0, snake_head)
    if snake_head == apple:
        
        score+=1
        
        if score%5==0:
            level+=1
            fps+=2
        apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    score_dr=font.render(f"Счет:{str(score)}",1,GREEN)
    level_dr=font.render(f"Уровень:{str(level)}",1,GREEN)
    draw_objects(snake, apple)
    screen.blit(score_dr,(10,10))
    screen.blit(level_dr,(690,10))

    pg.display.flip()
    clock.tick(fps)
    
 

pg.quit()


