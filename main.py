import pygame, draw, gameobject
from pygame.locals import *

pygame.init()
pygame.display.set_caption('dbd')
clock = pygame.time.Clock()
print(pygame.font.get_fonts())

bed = gameobject.GameObject('bed', 'assets/bed.png', 400, 200)
sleepy = gameobject.GameObject('sleepy', 'assets/wakingup.png', 400, 200)
textbox = gameobject.GameObject('textbox', 'assets/textbox.png', 64, 350, 128)

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
    draw.draw(textbox)
    draw.draw(bed)
    draw.draw(sleepy)
    draw.write('you are getting very sleepy right now because you are in such a comfy bed')
    draw.update()
