import pygame  
import random

pygame.init()

HEIGHT = 450
WIDTH = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Game")

clock = pygame.time.Clock()

is_mouth_open = True

x = 20
y = 20

dx = 0
dy = 0

SPEED = 5 
FOOD_RADIUS = 10
PACMAN_RADIUS = 20

def create_pacman(pacman_x,pacman_y):
    YELLOW = (255, 255, 0)
    BLACK = (0,0,0)
    """ temp = pacman_x
    pacman_x = pacman_y
    pacman_y = temp """
    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), PACMAN_RADIUS)
    if is_mouth_open:
        mouth_color = BLACK
    else:
        mouth_color = YELLOW
    pygame.draw.polygon(
        screen, 
        mouth_color,
        [
            (pacman_x,pacman_y),
            (pacman_x+PACMAN_RADIUS,pacman_y-PACMAN_RADIUS+PACMAN_RADIUS//2),
            (pacman_x+PACMAN_RADIUS,pacman_y+PACMAN_RADIUS-PACMAN_RADIUS//2)
        ]
        , 0)   
    pygame.draw.circle(screen, BLACK, (pacman_x, pacman_y-PACMAN_RADIUS//2), PACMAN_RADIUS//6)


def create_food(food_x, food_y):
    RED = (255,0,0)
    pygame.draw.circle(screen, RED, (food_x, food_y), FOOD_RADIUS)

    

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                dx = 0
                dy = SPEED
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -SPEED
            elif event.key == pygame.K_RIGHT:
                dx = SPEED
                dy = 0
            elif event.key == pygame.K_LEFT:
                dx = -SPEED
                dy = 0

        if event.type == pygame.QUIT:
            is_running = False

    
    screen.fill((0, 0, 0))

    create_pacman(x,y)

    for i in range(1,50):
        create_food(50+i*(FOOD_RADIUS*2+5),50)

    x += dx
    y += dy

    pygame.draw.arc(screen, (255,0,0), pygame.Rect(0, 0, 300, 200), 15,40, 10)


    



    is_mouth_open = not is_mouth_open


    pygame.time.delay(10)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()