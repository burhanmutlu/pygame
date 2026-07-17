import snake 
import food

import pygame

from random import randint

clock = pygame.time.Clock()

pygame.init()

HEIGHT = 450
WIDTH = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


snake1 = snake.Snake()
food1= food.Food(randint(30, WIDTH - 60), randint(50, HEIGHT - 80))

timer = 10

font = pygame.font.SysFont("Arial", 36)

text_surface = font.render("Score: 0", True, (0, 0, 0)) 

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False


    screen.fill((0, 255, 0))

    pygame.draw.rect(screen, (5,5,5), (20,40,WIDTH-50,HEIGHT-60),5)
    
    snake1.draw(screen)
    food1.draw(screen)

    key = pygame.key.get_pressed()
    if key [pygame.K_UP]:
        snake1.velocity_y= -1

    if key [pygame.K_DOWN]:
        snake1.velocity_y= 1
    
    if key [pygame.K_LEFT]:
        snake1.velocity_x = -1   #-1 sol, 0 sabit, 1 sağ
    
    if key [pygame.K_RIGHT]:
        snake1.velocity_x = 1





    text_rect = text_surface.get_rect()
    text_rect.topleft = (20, 0)  
    screen.blit(text_surface, text_rect)

    pygame.display.flip() 

    clock.tick(60)


pygame.quit()