import pygame

pygame.init()

HEIGHT = 600
WIDTH = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

RAKET_WIDTH = 20
RAKET_HEIGHT = 100

raket1_x = 28
raket1_y = HEIGHT/2 - RAKET_HEIGHT/2

raket2_x = WIDTH - 48
raket2_y = HEIGHT/2 - RAKET_HEIGHT/2

top_x = WIDTH/2
top_y = HEIGHT/2

dx = 5
dy = 5

clock = pygame.time.Clock()

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    #saha kodlari
    pygame.draw.rect(screen, (255, 0, 0), (20, 20, 760, 560),3)
    pygame.draw.line(screen, (0,0,255), (WIDTH/2, 23), (WIDTH/2, HEIGHT-23), 8)

    #raket kodlari
    pygame.draw.rect(screen, (255, 255, 255), (raket1_x, raket1_y, RAKET_WIDTH, RAKET_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (raket2_x, raket2_y, RAKET_WIDTH, RAKET_HEIGHT))

    # top

    pygame.draw.circle(screen, (255,255,0), (top_x, top_y), 10)

    if top_y <= 23 or top_y >= HEIGHT - 23:
        dy *= -1
    
    if top_x <= 23 or top_x >= WIDTH - 23:
        dx *= -1

    if top_x <=raket1_x+RAKET_WIDTH and (top_y >= raket1_y and top_y <= raket1_y + RAKET_HEIGHT):
        dx *= -1
    if top_x >=raket2_x and (top_y >= raket2_y and top_y <= raket2_y + RAKET_HEIGHT):
        dx *= -1

    top_x += dx
    top_y += dy

    #hareket kodu 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and raket2_y > 23:
        raket2_y -= 10

    if keys[pygame.K_DOWN] and raket2_y < HEIGHT - RAKET_HEIGHT - 23:
        raket2_y += 10

    if keys[pygame.K_w] and raket1_y > 23:
        raket1_y -= 10

    if keys[pygame.K_s] and raket1_y < HEIGHT - RAKET_HEIGHT - 23:
        raket1_y += 10

    
    pygame.display.flip() 
    screen.fill((0, 0, 0))
    clock.tick(60)

    """
    * oyundaki bugları cözme
    * makinenin seninle otomatik oynaması: singe and multiplayer modları
    * topun her zaman ortaadan baslaması (sayı kazandığında)
    * skor tutma
    * fizik kuralları
   
    """
    


pygame.quit()
