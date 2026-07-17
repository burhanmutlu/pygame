import time

import pygame

class Snake:
    def __init__(self):
        self.initial_length = 3
        #self.body = [(0, 0)] * self.initial_length  
        #self.direction = (1, 0)   
        self.color = (5, 5, 5) 
        self.x = 60
        self.y = 60
        self.width = 20
        self.height = 20
        self.velocity_x = 0
        self.velocity_y = 1

    def draw(self, screen):
        for _ in range(self.initial_length):
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            self.x += (self.width+5)//2
            #time.sleep(0.1)

    def grow(self):
        self.initial_length += 1

   
        
        
            

