from random import randint

import pygame
pygame.init()
WIDTH=1500
HEIGHT=1000
screen=pygame.display.set_mode((WIDTH,HEIGHT))
sayilar = [25]
for i in range(0,randint(5,15)):
    rand_sayi=randint(10,99)
    if not rand_sayi in sayilar:
        sayilar.append(rand_sayi)
pygame.display.set_caption("Bubble Sort Programı")
eski_sayilar=sayilar
baslangic=100
NORMAL=(0,0,255)
BELİRTME=(255,0,0)
pixel_boyut=8
is_running=True
is_finish_the_bubble_sort=False
while is_running:
    for i in range(0,len(sayilar)-1):
        temp_sayilar = sayilar
        finish = True
        for j in range(0,len(sayilar)-1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
            if not  is_running:
                continue
            konum = baslangic
            if not is_finish_the_bubble_sort:
                screen.fill((0, 0, 0))
            for sayi in sayilar:
                if sayi==sayilar[j] or sayilar[j+1]==sayi:
                    if sayilar[j] > sayilar[j+1]:
                        finish=False
                        pygame.draw.rect(screen,BELİRTME,(konum,HEIGHT-sayi*pixel_boyut,25,sayi*pixel_boyut))
                    else :
                        if finish:
                            finish=True
                        pygame.draw.rect(screen,(255,255,0),(konum,HEIGHT-sayi*pixel_boyut,25,sayi*pixel_boyut))
                        if is_finish_the_bubble_sort:
                            pygame.display.update()
                            pygame.time.wait(500)
                else:
                     pygame.draw.rect(screen,NORMAL,(konum,HEIGHT-sayi*pixel_boyut,25,sayi*pixel_boyut))
                konum+=35
            if sayilar[j]>sayilar[j+1]:
                temp=sayilar[j]
                sayilar[j]=sayilar[j+1]
                sayilar[j+1]=temp
            pygame.display.update()
            pygame.time.wait(500)
        if finish:
            is_finish_the_bubble_sort=True
            NORMAL=(255,255,0)
            BELİRTME=(255,255,0)
        elif finish and NORMAL==(255,255,0):
            break

pygame.quit()