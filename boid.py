import pygame
from numpy import sin, cos, tan, arctan, pi

class Boid:
    def __init__(self, pos, vel, maxspeed, size):
        self.pos = pos
        self.vel = vel
        self.acc = pygame.math.Vector2(0,0)

        self.size = size
        self.maxspeed = maxspeed

        self.perception = 80
        self.angle_perception = pi/6

        self.align_force = 0.25
        self.cohes_force = 0.15
        self.sep_force   = 0.15

    def get_angle(self, a, v):
        if (v.x < 0 and v.y > 0) or (v.x < 0 and v.y < 0):
            return (pi - a)
        return (2*pi - a)

    def in_range(self):
        a = self.get_angle(arctan(self.distance.y / self.distance.x), self.distance)
        return (self.distance.magnitude() <= self.perception
                and a >= self.angle_perception
                and a <= 2*pi-self.angle_perception)

    def get_locals(self, flock):
        self.locals = []
        for i in range(len(flock)):
            mate = flock[i]

            if self.pos != mate.pos:
                self.distance = mate.pos - self.pos

                if self.in_range():
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

            if steering.magnitude() >= self.align_force:
                steering.scale_to_length(self.align_force)

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

            if steering.magnitude() >= self.cohes_force:
                steering.scale_to_length(self.cohes_force)

        return steering

    def separation(self):
        steering = pygame.math.Vector2(0,0)
        count = 0

        for i in range(len(self.locals)):
            steering += ((self.pos - self.locals[i].pos) / self.distance.magnitude())
            count += 1

        if count > 0:
            steering /= count

            steering.scale_to_length(self.maxspeed)

            steering -= self.vel

            if steering.magnitude() >= self.sep_force:
                steering.scale_to_length(self.sep_force)

        return steering

    def move(self):
        self.acc = self.alignment() + self.cohesion() + self.separation()
        self.vel += self.acc
        self.pos += self.vel

    def borders(self, width, height):
        if self.pos.x <= 0 or self.pos.x >= width:
            self.pos.x = self.pos.x % width

        if self.pos.y <= 0 or self.pos.y >= height:
            self.pos.y = self.pos.y % height

    def draw_boid(self, screen):
        a = self.get_angle(arctan(self.vel.y/self.vel.x), self.vel)

        v1 = pygame.math.Vector2(self.pos.x + self.size*cos(a), self.pos.y - self.size*sin(a))
        v2 = pygame.math.Vector2(self.pos.x - self.size*sin(a)/3, self.pos.y - self.size*cos(a)/3)
        v3 = pygame.math.Vector2(self.pos.x + self.size*sin(a)/3, self.pos.y + self.size*cos(a)/3)

        pygame.draw.polygon(screen, (128,128,128), [v1, v2, v3])
