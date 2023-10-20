import pygame
import random
from boid import Boid

global screen_size

# setup
x_screen_size = 500
y_screen_size = 500
pygame.init()
screen = pygame.display.set_mode((x_screen_size, y_screen_size))
clock = pygame.time.Clock()
running = True
dt = 0
pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


# creates initial flock
flock = []
for i in range(30):
    flock.append(Boid())

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill screen to wipe last frame
    screen.fill("black")

    # draws the border
    y_up_lim = y_screen_size - 50
    x_up_lim = x_screen_size - 50
    x_low_lim = 50
    y_low_lim = 50
    pygame.draw.line(screen, "white", [x_low_lim, y_low_lim], [x_up_lim, y_low_lim], 5 )
    pygame.draw.line(screen, "white", [x_low_lim, y_low_lim], [x_low_lim, y_up_lim], 5)
    pygame.draw.line(screen, "white", [x_low_lim, y_up_lim], [x_up_lim, y_up_lim], 5)
    pygame.draw.line(screen, "white", [x_up_lim, y_low_lim], [x_up_lim, y_up_lim], 5)

    for i in flock:
        #draws boid
        pygame.draw.circle(screen, "red", i.position, 5)
        Boid.border(i)
        Boid.flock(i, flock)
        Boid.update(i)


    # displays everything
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(30) / 1000

pygame.quit()