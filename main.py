import pygame, draw, gameobject, scene, events, text, walker, platformer
from pygame.locals import *

pygame.init()
pygame.display.set_caption('dbd')
clock = pygame.time.Clock()

bed = gameobject.GameObject('bed', 'assets/bed.png', 400, 200)
sleepy = gameobject.GameObject('sleepy', 'assets/wakingup.png', 400, 200)
textbox = gameobject.GameObject('textbox', 'assets/textbox.png', 64, 350, 128)
walker = walker.Walker('walker', 'assets/walkingd.png', 570, 100)
lunch = gameobject.GameObject('lunch', 'assets/lunchlady.png', 320, 100)
essay = gameobject.GameObject('essay', 'assets/essay.png', 0, 0)

bedscene = scene.Scene()
bedscene.add(bed)
bedscene.add_actor(walker)
bedscene.add(lunch)
bedscene.add(sleepy)
bedscene.add(essay)
curscene = bedscene
text.add_text('you are getting very sleepy right now because you are in such a comfy bed', text.USER)
text.add_text('go to sleep')

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or pygame.key.get_pressed()[K_ESCAPE]:
            running = False
        if event.type == KEYDOWN:
            if pygame.key.get_pressed()[K_j]:
                curscene.advance()
            if pygame.key.get_pressed()[K_k]:
                curscene.devance()
            if pygame.key.get_pressed()[K_SPACE]:
                text.user_text()

        elif event.type == events.ADVANCETEXT:
            text.process_event(event.advtype)

    dt = clock.tick(60)

    curscene.update(dt)
    curscene.draw()
    platformer.platformscene.update(dt)
    platformer.platformscene.draw()
    draw.draw_surf(platformer.platformscene.rendertarget, (0, 64))
    draw.draw(textbox)
    text.draw_text()
    draw.update()
