import pygame
import random
import time

pygame.init()

SPEED = 40
FOOD_RADIUS = 10
PACMAN_RADIUS = 20
HEIGHT = 11 * PACMAN_RADIUS * 2
WIDTH = 20 * PACMAN_RADIUS * 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Game")

clock = pygame.time.Clock()

x = 10 * PACMAN_RADIUS * 2 + PACMAN_RADIUS
y = 9 * PACMAN_RADIUS * 2 - PACMAN_RADIUS
dx = SPEED
dy = 0
yon = "d"
is_mouth_open = True
baslangic_zamani = time.time()
score=0

SCORE_FONT=pygame.font.SysFont("Arial",30,True)
FINISH_FONT=pygame.font.SysFont("Arial",100,True)

def create_pacman(pacman_x, pacman_y):
    YELLOW = (255, 255, 0)
    BLACK = (0, 0, 0)
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
                (pacman_x, pacman_y),
                (pacman_x + PACMAN_RADIUS, pacman_y - PACMAN_RADIUS + PACMAN_RADIUS // 2),
                (pacman_x + PACMAN_RADIUS, pacman_y + PACMAN_RADIUS - PACMAN_RADIUS // 2)
            ]
            , 0)
    elif yon == "a":
        pygame.draw.polygon(
            screen,
            mouth_color,
            [
                (pacman_x, pacman_y),
                (pacman_x - PACMAN_RADIUS, pacman_y - PACMAN_RADIUS + PACMAN_RADIUS // 2),
                (pacman_x - PACMAN_RADIUS, pacman_y + PACMAN_RADIUS - PACMAN_RADIUS // 2)
            ]
            , 0)
    elif yon == "w":
        pygame.draw.polygon(
            screen,
            mouth_color,
            [
                (pacman_x, pacman_y),
                (pacman_x - PACMAN_RADIUS + PACMAN_RADIUS // 2, pacman_y - PACMAN_RADIUS),
                (pacman_x + PACMAN_RADIUS - PACMAN_RADIUS // 2, pacman_y - PACMAN_RADIUS)
            ]
            , 0)
    elif yon == "s":
        pygame.draw.polygon(
            screen,
            mouth_color,
            [
                (pacman_x, pacman_y),
                (pacman_x - PACMAN_RADIUS + PACMAN_RADIUS // 2, pacman_y + PACMAN_RADIUS),
                (pacman_x + PACMAN_RADIUS - PACMAN_RADIUS // 2, pacman_y + PACMAN_RADIUS)
            ]
            , 0)
        # pygame.draw.circle(screen, BLACK, (pacman_x, pacman_y-PACMAN_RADIUS//2), PACMAN_RADIUS//6)

def create_ghost(gx,gy):
    pygame.draw.circle(screen,(255, 192, 203),(gx,gy),20)

def create_food(food_x, food_y):
    RED = (255, 0, 0)
    pygame.draw.circle(screen, RED, (food_x, food_y), FOOD_RADIUS)

# pygame.mixer.music.load("nam2.mp3")
# pygame.mixer.music.play(-1)
eat_sound_effect=pygame.mixer.Sound("yem_sesi.mp3")
map = [
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
game_over=False
fps=5
hayalet_x=60
hayalet_y=60
while is_running:
    grid_x = int((x - PACMAN_RADIUS) / 40)
    grid_y = int((y - PACMAN_RADIUS) / 40)
    score_text=SCORE_FONT.render(f"Skor: {score}",True,(255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and grid_y % 1 == 0 and grid_x % 1 == 0 and map[grid_y+1][grid_x]!=1:
                    dx = 0
                    dy = SPEED
                    yon = "s"
                elif event.key == pygame.K_UP and grid_y % 1 == 0 and grid_x % 1 == 0 and map[grid_y-1][grid_x]!=1:
                    dx = 0
                    dy = -SPEED
                    yon = "w"
                elif event.key == pygame.K_RIGHT and grid_y % 1 == 0 and grid_x % 1 == 0 and map[grid_y][grid_x+1]!=1:
                    dx = SPEED
                    dy = 0
                    yon = "d"
                elif event.key == pygame.K_LEFT and grid_y % 1 == 0 and grid_x % 1 == 0 and map[grid_y][grid_x-1]!=1:
                    dx = -SPEED
                    dy = 0
                    yon = "a"

        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((0, 0, 0))
    nx=x+dx
    ny=y+dy
    next_col=int((nx - PACMAN_RADIUS) / 40)
    next_row = int((ny - PACMAN_RADIUS) / 40)

    if map[next_row][next_col]==1:
        dx=0
        dy=0
        eat_sound_effect.stop()
    if grid_x<len(map[0]) and grid_x>=0 and grid_y<len(map) and grid_y>=0:
        if map[grid_y][grid_x]==2:
            map[grid_y][grid_x]=0
            eat_sound_effect.play()
            score+=10
            if score==1100:
                game_over=True

    for satir in range(10):
        for sutun in range(20):
            val = map[satir][sutun]
            if val == 1:
                pygame.draw.rect(screen, (0, 0, 255), (
                sutun * PACMAN_RADIUS * 2, satir * PACMAN_RADIUS * 2, PACMAN_RADIUS * 2, PACMAN_RADIUS * 2), 0)
            elif val == 2:
                create_food((PACMAN_RADIUS - FOOD_RADIUS) + sutun * PACMAN_RADIUS * 2 + FOOD_RADIUS,
                            (PACMAN_RADIUS - FOOD_RADIUS) + satir * PACMAN_RADIUS * 2 + FOOD_RADIUS)

    x += dx
    y += dy
    create_pacman(x, y)

    ngx=hayalet_x
    ngy=hayalet_y
    if hayalet_x<x:
        ngx+=39
    elif hayalet_x > x:
        ngx -= 39
    if hayalet_y<y:
        ngy+=39
    elif hayalet_y > y:
        ngy -= 39


    g_row=int((ngy - 20) / 40)
    g_col=int((ngx - 20) / 40)
    if map[g_row][g_col] != 1:
        hayalet_x=ngx
        hayalet_y=ngy
    create_ghost(hayalet_x,hayalet_y)
    create_ghost(hayalet_x,hayalet_y)

    if grid_x==g_col and grid_y==g_row:
        game_over=True

    gecen_zaman = round((time.time() - baslangic_zamani), 2)
    if gecen_zaman > 0.2:
        is_mouth_open = not is_mouth_open
        baslangic_zamani = time.time()

    screen.blit(score_text,(20,HEIGHT-36))

    if game_over:
        screen.fill((0, 0, 0))
        finish_text = FINISH_FONT.render("KAZANDIN!", True, (255, 255, 0))
        screen.blit(finish_text, finish_text.get_rect(center=(WIDTH//2,HEIGHT//2)))
        fps = 0

    pygame.display.flip()

    clock.tick(fps)

pygame.quit()
