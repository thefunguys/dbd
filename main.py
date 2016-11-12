import pygame, draw, gameobject
from pygame.locals import *

pygame.init()
pygame.display.set_caption('dbd')
clock = pygame.time.Clock()

bed = gameobject.GameObject('bed', 'assets/bed.png', 400, 200)
sleepy = gameobject.GameObject('sleepy', 'assets/wakingup.png', 400, 200)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or pygame.key.get_pressed()[K_ESCAPE]:
            running = False
        if event.type == KEYDOWN and pygame.key.get_pressed()[K_j]:
            sleepy.inc_frame()
        if event.type == KEYDOWN and pygame.key.get_pressed()[K_k]:
            sleepy.dec_frame()

    dt = clock.tick(60)

    draw.draw_bg()
    draw.draw(bed)
    draw.draw(sleepy)
    draw.update()
