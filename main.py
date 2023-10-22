import pygame
import random
from boid import Boid
from quadtree import *

global screen_size

# setup
x_screen_size = 1000
y_screen_size = 1000
pygame.init()
screen = pygame.display.set_mode((x_screen_size, y_screen_size))
clock = pygame.time.Clock()
running = True
dt = 0
pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


# creates initial flock
flock = []
for i in range(75):
    flock.append(Boid())

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill screen to wipe last frame
    screen.fill("lightblue")

    # draws the border
    y_up_lim = y_screen_size - 50
    x_up_lim = x_screen_size - 50
    x_low_lim = 50
    y_low_lim = 50
    pygame.draw.line(screen, "white", [x_low_lim, y_low_lim], [x_up_lim, y_low_lim], 5 )
    pygame.draw.line(screen, "white", [x_low_lim, y_low_lim], [x_low_lim, y_up_lim], 5)
    pygame.draw.line(screen, "white", [x_low_lim, y_up_lim], [x_up_lim, y_up_lim], 5)
    pygame.draw.line(screen, "white", [x_up_lim, y_low_lim], [x_up_lim, y_up_lim], 5)



    # boundary = rectangle(screen.get_width() / 2,screen.get_height() / 2, screen.get_width(), screen.get_height())
    # qt = quadTree(boundary, 4)

    # for i in flock:
    #     #draws boid
    #     pygame.draw.circle(screen, "black", i.position, 5)
    #     Boid.border(i)
    #     i_point = point(i.position[0], i.position[1], i)
    #     qt.insert(i_point)
    #     range = rectangle(i.position[0], i.position[1], i.vision, i.vision)
    #     points = qt.query(range, [])
    #     Boid.flock(i, points)
    #     Boid.update(i)


    for i in flock:
        #draws boid
        pygame.draw.circle(screen, "black", i.position, 5)
        Boid.border(i)
        Boid.flock(i, flock)
        Boid.update(i)


    # displays everything
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(30) / 1000

pygame.quit()