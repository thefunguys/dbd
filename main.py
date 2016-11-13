import pygame, draw, gameobject, scene, events, text, walker, platformer
from pygame.locals import *

pygame.init()
pygame.display.set_caption('dbd')
clock = pygame.time.Clock()

bed = gameobject.GameObject('bed', 'assets/bed.png', 400, 200)
sleepy = gameobject.GameObject('sleepy', 'assets/wakingup.png', 400, 200)
textbox = gameobject.GameObject('textbox', 'assets/textbox.png', 64, 350, 128)
walker = walker.Walker('walker', 'assets/walkingd.png', 570, 200)
lunch = gameobject.GameObject('lunch', 'assets/lunchlady.png', 320, 200)
essay = gameobject.GameObject('essay', 'assets/essay.png', 400, 200)

bedscene = scene.Scene()
bedscene.add(bed)
bedscene.add_actor(sleepy)
lunchscene = scene.Scene()
lunchscene.add_actor(walker)
lunchscene.add(lunch)
essayscene = scene.Scene()
essayscene.add_actor(essay)
scenes = [bedscene, lunchscene, essayscene]
curscene = 0
gamevars = {'state': 'begin'}
def state(s=None):
    if s:
        gamevars['state'] = s
    return gamevars['state']
text.add_text('you are getting very sleepy right now because you are in such a comfy bed', text.USER)
text.add_text('go to sleep')
prog = 0.0

def next_scene():
    global curscene
    curscene += 1
    if curscene >= len(scenes):
        curscene = 0
    if scenes[curscene] == lunchscene:
        state('begin lunch')
        text.texts = []
        text.curtext = 0
        text.add_text('Heather calls you to join for lunch', text.USER)
        text.add_text('get pass anxiety and fear to make it to the table', text.EVENT)

def current_scene():
    return scenes[curscene]

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or pygame.key.get_pressed()[K_ESCAPE]:
            running = False
        if event.type == KEYDOWN:
            if pygame.key.get_pressed()[K_j]:
                next_scene()
                draw.draw_bg()
                pygame.display.update()
            if pygame.key.get_pressed()[K_k]:
                curscene.devance()
            if pygame.key.get_pressed()[K_SPACE]:
                text.user_text()
                if state() == 'begin lunch':
                    platformer.start()
                    state('lunching')

        elif event.type == events.ADVANCETEXT:
            text.process_event(event.advtype)

    dt = clock.tick(60)
    prog += dt / 10000.0
    if prog > 1.1:
        prog = 0

    current_scene().update(dt)
    current_scene().draw()
    if state() == 'lunching':
        prog = platformer.player.x / 280.0
        platformer.platformscene.update(dt)
        platformer.platformscene.draw()
        draw.draw_surf(platformer.platformscene.rendertarget, (0, 64))
    current_scene().set_progress(prog)
    draw.draw(textbox)
    text.draw_text(text.texts)
    draw.update()
