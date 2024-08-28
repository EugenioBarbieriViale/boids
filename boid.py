import pygame
from numpy import sin, cos, tan, arctan, pi

class Boid:
    def __init__(self, pos, vel, size):
        self.pos = pos
        self.vel = vel

        self.acc = pygame.math.Vector2(0,0)
        self.steering = pygame.math.Vector2(0,0)

        self.size = size

        self.threshold = 70
        self.maxspeed = 3
        self.maxforce = 0.3

    def get_locals(self, flock):
        self.locals = []
        for i in range(len(flock)):
            mate = flock[i]

            if self.pos != mate.pos:
                d = pygame.math.Vector2.distance_to(self.pos, mate.pos)

                if d <= self.threshold:
                    self.locals.append(mate)

    def alignment(self):
        count = 0

        for i in range(len(self.locals)):
            self.steering += self.locals[i].vel
            count += 1

        if count > 0:
            self.steering /= count
            self.steering.scale_to_length(self.maxspeed)
            self.steering -= self.vel

        if self.steering.magnitude() >= self.maxforce:
            # self.steering *= self.maxforce
            self.steering.scale_to_length(self.maxforce)

    def move(self):
        if self.vel.x < 0 and self.vel.y > 0:
            self.a = pi - arctan(self.vel.y/self.vel.x)

        elif self.vel.x < 0 and self.vel.y < 0:
            self.a = pi - arctan(self.vel.y/self.vel.x)

        else:
            self.a = 2*pi - arctan(self.vel.y/self.vel.x)

        self.acc = self.steering
        self.vel += self.acc
        self.pos += self.vel

    def borders(self, width, height):
        if self.pos.x <= 0:
            self.pos.x = width

        if self.pos.x >= width:
            self.pos.x = 0

        if self.pos.y <= 0:
            self.pos.y = height

        if self.pos.y >= height:
            self.pos.y = 0

    def draw_boid(self, screen):
        v1 = pygame.math.Vector2(self.pos.x + self.size*cos(self.a), self.pos.y - self.size*sin(self.a))
        v2 = pygame.math.Vector2(self.pos.x - self.size*sin(self.a)/3, self.pos.y - self.size*cos(self.a)/3)
        v3 = pygame.math.Vector2(self.pos.x + self.size*sin(self.a)/3, self.pos.y + self.size*cos(self.a)/3)

        pygame.draw.polygon(screen, (128,128,128), [v1, v2, v3])
