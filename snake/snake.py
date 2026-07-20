import time

import pygame

class Snake:
    def __init__(self):
        self.initial_length = 3
        self.body = [(60, 60),(40,60),(20,60)] 
        self.color = (5, 5, 5) 
        self.width = 20
        self.height = 20
        self.velocity_x = 1
        self.velocity_y = 0

    def move(self):
        current_head = self.body[0]

        new_head = [current_head[0] + self.velocity_x * self.width, current_head[1] + self.velocity_y * self.height]
        
        self.body.insert(0, new_head)

        if len(self.body) > self.initial_length:
            self.body.pop()

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, (segment[0],segment[1], self.width, self.height))

    def grow(self):
        self.initial_length += 1

    @property
    def head(self): 
        return pygame.rect.Rect(self.body[0][0], self.body[0][1], self.width, self.height)
    
        
        
            

