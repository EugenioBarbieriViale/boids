import pygame
from numpy import sin, cos, tan, arctan, pi

class Boid:
    def __init__(self, pos, vel, maxspeed, size):
        self.pos = pos
        self.vel = vel
        self.acc = pygame.math.Vector2(0,0)

        self.size = size

        self.perception = 80
        self.maxspeed = maxspeed
        self.maxforce = 0.2

    def get_locals(self, flock):
        self.locals = []
        for i in range(len(flock)):
            mate = flock[i]

            if self.pos != mate.pos:
                d = pygame.math.Vector2.distance_to(self.pos, mate.pos)

                if d <= self.perception:
                    self.locals.append(mate)

    def alignment(self):
        steering = pygame.math.Vector2(0,0)
        count = 0

        for i in range(len(self.locals)):
            steering += self.locals[i].vel
            count += 1

        if count > 0:
            steering /= count

            steering.scale_to_length(self.maxspeed)
            steering -= self.vel
            steering *= self.maxforce

        return steering

    def cohesion(self):
        steering = pygame.math.Vector2(0,0)
        count = 0

        for i in range(len(self.locals)):
            steering += self.locals[i].pos
            count += 1

        if count > 0:
            steering /= count

            steering -= self.pos
            steering.scale_to_length(self.maxspeed)

            steering -= self.vel
            steering *= self.maxforce

        return steering

    def separation(self):
        steering = pygame.math.Vector2(0,0)
        count = 0

        for i in range(len(self.locals)):
            steering += self.locals[i].pos
            count += 1

        if count > 0:
            steering /= count
            steering -= self.pos
            steering *= -1

            steering.scale_to_length(self.maxspeed)

            steering -= self.vel
            steering *= self.maxforce

        return steering

    def move(self):
        self.acc = self.alignment() + self.cohesion() + self.separation()
        self.vel += self.acc
        self.pos += self.vel

    def get_angle(self):
        if self.vel.x < 0 and self.vel.y > 0:
            angle = pi - arctan(self.vel.y/self.vel.x)

        elif self.vel.x < 0 and self.vel.y < 0:
            angle = pi - arctan(self.vel.y/self.vel.x)

        else:
            angle = 2*pi - arctan(self.vel.y/self.vel.x)

        return angle

    def borders(self, width, height):
        if self.pos.x <= 0 or self.pos.x >= width:
            self.pos.x = self.pos.x % width

        if self.pos.y <= 0 or self.pos.y >= height:
            self.pos.y = self.pos.y % height

    def draw_boid(self, screen):
        a = self.get_angle()

        v1 = pygame.math.Vector2(self.pos.x + self.size*cos(a), self.pos.y - self.size*sin(a))
        v2 = pygame.math.Vector2(self.pos.x - self.size*sin(a)/3, self.pos.y - self.size*cos(a)/3)
        v3 = pygame.math.Vector2(self.pos.x + self.size*sin(a)/3, self.pos.y + self.size*cos(a)/3)

        pygame.draw.polygon(screen, (128,128,128), [v1, v2, v3])
