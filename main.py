# OPTIMIZATION: quadtree / spatial subdivision

import pygame, sys
from random import random, uniform

import boid


pygame.init()
clock = pygame.time.Clock()

X, Y = 1200, 1000

screen = pygame.display.set_mode([X,Y])
pygame.display.set_caption("Flocking simulation")

N = 100

flock = []
for i in range(N):
    pos = pygame.math.Vector2(random() * X, random() * Y)

    maxspeed = 6
    vel = pygame.math.Vector2(uniform(-1.0,1.0) * maxspeed, uniform(-1.0,1.0) * maxspeed)

    size = 20

    current = boid.Boid(pos, vel, maxspeed, size)
    flock.append(current)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    for i in range(N):
        flock[i].get_locals(flock)

        flock[i].borders(X, Y)
        flock[i].move()
        flock[i].draw_boid(screen)

    pygame.display.flip()
    clock.tick(30)
    pygame.display.update()

pygame.quit()
