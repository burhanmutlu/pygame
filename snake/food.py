import pygame

class Food:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._color = (255, 0, 0)
        self._radius = 10
        self._points = 10

    def draw(self, screen):
        pygame.draw.circle(screen, self._color, (self._x, self._y), self._radius)

    def set_radius(self, radius):
        self._radius = radius
    
    def get_points(self):
        return self._points




