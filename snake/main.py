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

fps = 8

game_over=False
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake1.velocity_y != 1: #-1 sol, 0 sabit, 1 sağ
                snake1.velocity_y = -1
                snake1.velocity_x = 0
            elif event.key == pygame.K_DOWN and snake1.velocity_y != -1:
                snake1.velocity_y = 1
                snake1.velocity_x = 0
            elif event.key == pygame.K_LEFT and snake1.velocity_x != 1:
                snake1.velocity_x = -1
                snake1.velocity_y = 0
            elif event.key == pygame.K_RIGHT and snake1.velocity_x != -1:
                snake1.velocity_x = 1
                snake1.velocity_y = 0
        if event.type == pygame.QUIT:
            is_running = False

    for segment in snake1.body[1:]:
        if snake1.head.colliderect(pygame.rect.Rect(segment[0],segment[1],snake1.width,snake1.height)):
            game_over=True
    if (snake1.get_position()[0]<20 or snake1.get_position()[0]>WIDTH-50
            or snake1.get_position()[1]<40 or snake1.get_position()[1]>HEIGHT-60):
        game_over=True
    if game_over:
        fps=0


    screen.fill((0, 255, 0))
    pygame.draw.rect(screen, (5,5,5), (20,40,WIDTH-50,HEIGHT-60),5)
    for x in range(WIDTH//20-3):
        for y in range(HEIGHT//20-3):
            if (x+y)%2==0:
                pygame.draw.rect(screen,(100,255,100),(x*20+25,y*20+45,20,20))
            else:
                pygame.draw.rect(screen,(0,190,0),(x*20+25,y*20+45,20,20))
    
    snake1.move()
    snake1.draw(screen)

    if(snake1.head.colliderect(food1.head)):
        snake1.grow()
        food1.set_position(randint(20+5, WIDTH - 55), randint(45, HEIGHT - 65))
        text_surface = font.render("Score: " + str(snake1.initial_length-3), True, (0, 0, 0))
    
    food1.draw(screen)

    #skor
    text_rect = text_surface.get_rect()
    text_rect.topleft = (20, 0)  
    screen.blit(text_surface, text_rect)

    pygame.display.flip()
    clock.tick(fps)
    fps += fps*0.001


pygame.quit()