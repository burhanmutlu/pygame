import pygame
from random import randint 

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Physical Movement")

class RigidBody:
    def __init__(self, x,y):
        self.rect_size = 40
        self.rect = pygame.Rect(x,y, self.rect_size, self.rect_size)
        self.velocity_x = 0
        self.velocity_y = 0
        self.g_value = 1
        #self.velocity = (0, 0)
        self.jump_power = -15
        self.sekme_gucu = 0.6
        self.air_friction = 0.9
        self.is_jumping = True

    def update(self):
        self.velocity_y += self.g_value
        self.velocity_x *= self.air_friction

        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        if self.rect.bottom >= HEIGHT-50: #yere degerse ne olacak
            self.rect.bottom = HEIGHT-50

            if abs(self.velocity_y) > 2:
                self.velocity_y = self.sekme_gucu * (-self.velocity_y)
            else:
                self.velocity_y = 0
                self.is_jumping = False

        else: 
            self.is_jumping = True

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = self.jump_power
            self.is_jumping = True

    def apply_push(self, kuvvet_x, kuvvet_y):
        self.velocity_x += kuvvet_x
        self.velocity_y += kuvvet_y


su = RigidBody(WIDTH // 2-20, HEIGHT // 2-20)
ates = RigidBody(WIDTH // 2-80, HEIGHT // 2-80)

objects = []
for i in range (0,50): 
    objects.append(RigidBody(randint(0,WIDTH-20), randint(0, HEIGHT-20)))

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_f:
                su.apply_push(2*su.velocity_x, -10)
            if event.key==pygame.K_g:
                ates.apply_push(2*ates.velocity_x, -10)
    key = pygame.key.get_pressed()

    if key[pygame.K_UP]:
        su.jump()
    if key[pygame.K_LEFT]:
         su.velocity_x += -1
    elif key[pygame.K_RIGHT]:
        su.velocity_x += 1
    
    if key[pygame.K_w]:
        ates.jump()
    if key[pygame.K_a]:
        ates.velocity_x += -1

    elif key[pygame.K_d]:
        ates.velocity_x += 1
         
    su.update()
    ates.update()

    screen.fill((30, 30, 140))

    """ for o in objects:
        o.update()
        pygame.draw.rect(screen, (255, 50, 10), o.rect) """

    pygame.draw.rect(screen, (150,50,0), (0, HEIGHT-50, WIDTH, 20)) #zemın cizimi

    pygame.draw.rect(screen, (255, 0, 0), su.rect) #nesne cizimi- ates
    pygame.draw.rect(screen, (0, 0, 255), ates.rect) #nesne cizimi- su

    if su.rect.colliderect(ates.rect):
        su.apply_push(100, -100)
        ates.apply_push(-100, -100)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
