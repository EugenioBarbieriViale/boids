import pygame, sys
from random import random
# from numpy import sin, cos, tan, atan, pi
from numpy import pi

import boid


pygame.init()
clock = pygame.time.Clock()

X, Y = 1000, 800

screen = pygame.display.set_mode([X,Y])
pygame.display.set_caption("Flocking simulation")

N = 10

flock = []
for i in range(N):
    pos = pygame.math.Vector2(random() * X, random() * Y)
    vel = pygame.math.Vector2(random() * 3, random() * 3)
    size = 30

    current = boid.Boid(pos, vel, size)
    flock.append(current)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    for i in range(N):
        flock[i].move()
        flock[i].draw_boid(screen)

    pygame.display.flip()
    clock.tick(30)
    pygame.display.update()

pygame.quit()
