import pygame
from numpy import sin, cos, tan, arctan, pi

class Boid:
    def __init__(self, pos, vel, size):
        self.pos = pos
        self.vel = vel

        self.a = 2*pi - arctan(self.vel.y/self.vel.x)
        self.size = size

    def move(self):
        self.pos += self.vel

    def draw_boid(self, screen):
        v1 = pygame.math.Vector2(self.pos.x + self.size*cos(self.a), self.pos.y - self.size*sin(self.a))
        v2 = pygame.math.Vector2(self.pos.x - self.size*sin(self.a)/3, self.pos.y - self.size*cos(self.a)/3)
        v3 = pygame.math.Vector2(self.pos.x + self.size*sin(self.a)/3, self.pos.y + self.size*cos(self.a)/3)

        pygame.draw.polygon(screen, (128,128,128), [v1, v2, v3])
