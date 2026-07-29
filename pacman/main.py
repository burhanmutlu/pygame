import pygame  
import random
import time

pygame.init()

SPEED = 20 
FOOD_RADIUS = 10
PACMAN_RADIUS = 20
HEIGHT = 11*PACMAN_RADIUS*2
WIDTH = 20*PACMAN_RADIUS*2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Game")

clock = pygame.time.Clock()

x = 10*PACMAN_RADIUS*2+PACMAN_RADIUS
y = 9*PACMAN_RADIUS*2-PACMAN_RADIUS
dx = SPEED
dy = 0
yon = "d"
is_mouth_open = True
baslangic_zamani = time.time()

def create_pacman(pacman_x,pacman_y):
    YELLOW = (255, 255, 0)
    BLACK = (0,0,0)
    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), PACMAN_RADIUS)
    if is_mouth_open:
        mouth_color = BLACK
    else:
        mouth_color = YELLOW
    if yon == "d":
        pygame.draw.polygon(
            screen, 
            mouth_color,
            [
                (pacman_x,pacman_y),
                (pacman_x+PACMAN_RADIUS,pacman_y-PACMAN_RADIUS+PACMAN_RADIUS//2),
                (pacman_x+PACMAN_RADIUS,pacman_y+PACMAN_RADIUS-PACMAN_RADIUS//2)
            ]
            , 0)   
    elif yon == "a":
        pygame.draw.polygon(
            screen, 
            mouth_color,
            [
                (pacman_x,pacman_y),
                (pacman_x-PACMAN_RADIUS,pacman_y-PACMAN_RADIUS+PACMAN_RADIUS//2),
                (pacman_x-PACMAN_RADIUS,pacman_y+PACMAN_RADIUS-PACMAN_RADIUS//2)
            ]
            , 0) 
    elif yon == "w":
        pygame.draw.polygon(
            screen, 
            mouth_color,
            [
                (pacman_x,pacman_y),
                (pacman_x-PACMAN_RADIUS+PACMAN_RADIUS//2,pacman_y-PACMAN_RADIUS),
                (pacman_x+PACMAN_RADIUS-PACMAN_RADIUS//2,pacman_y-PACMAN_RADIUS)
            ]
            , 0) 
    elif yon == "s":
        pygame.draw.polygon(
            screen, 
            mouth_color,
            [
                (pacman_x,pacman_y),
                (pacman_x-PACMAN_RADIUS+PACMAN_RADIUS//2,pacman_y+PACMAN_RADIUS),
                (pacman_x+PACMAN_RADIUS-PACMAN_RADIUS//2,pacman_y+PACMAN_RADIUS)
            ]
            , 0) 
    #pygame.draw.circle(screen, BLACK, (pacman_x, pacman_y-PACMAN_RADIUS//2), PACMAN_RADIUS//6)

def create_food(food_x, food_y):
    RED = (255,0,0)
    pygame.draw.circle(screen, RED, (food_x, food_y), FOOD_RADIUS)

map =[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1],
    [1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 1],
    [1, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 2, 1, 2, 1],
    [1, 2, 1, 2, 2, 2, 2, 2, 1, 0, 0, 1, 2, 2, 2, 2, 2, 1, 2, 1],
    [1, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1],
    [1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and grid_y % 1 == 0 and grid_x % 1 ==0:
                dx = 0
                dy = SPEED
                yon = "s"
            elif event.key == pygame.K_UP and grid_y % 1 == 0 and grid_x % 1 ==0:
                dx = 0
                dy = -SPEED
                yon = "w"
            elif event.key == pygame.K_RIGHT and grid_y % 1 ==0 and grid_x % 1 ==0:
                dx = SPEED
                dy = 0
                yon = "d"
            elif event.key == pygame.K_LEFT and grid_y % 1 ==0 and grid_x % 1 ==0: 
                dx = -SPEED
                dy = 0
                yon = "a"

        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((0, 0, 0))

    for satir in range(10):
        for sutun in range(20):
            val = map[satir][sutun] 
            if val == 1:
                pygame.draw.rect(screen, (0,0,255),(sutun*PACMAN_RADIUS*2,satir*PACMAN_RADIUS*2,PACMAN_RADIUS*2,PACMAN_RADIUS*2),0)
            elif val == 2:
                create_food((PACMAN_RADIUS-FOOD_RADIUS)+sutun*PACMAN_RADIUS*2+FOOD_RADIUS, (PACMAN_RADIUS-FOOD_RADIUS)+satir*PACMAN_RADIUS*2+FOOD_RADIUS)
            
    x += dx
    y += dy

    grid_x = (x+PACMAN_RADIUS)/40
    grid_y = (y+PACMAN_RADIUS)/40

    print(grid_x, " ", grid_y)

    create_pacman(x,y)

    gecen_zaman = round((time.time() - baslangic_zamani),2)
    if gecen_zaman > 0.2:
        is_mouth_open = not is_mouth_open
        baslangic_zamani = time.time()

    pygame.display.flip()

    clock.tick(20)

pygame.quit()


"""
1-yemleri yemek
2-duvar kontrolu
3-skor
4-muzik eklemek
5-hayalet 
"""
