import pygame, draw, gameobject, scene, events, text, walker, platformer, snake, threading
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
gamevars = {'state': 1}


def state(s=None):
    if s:
        gamevars['state'] = s
    return gamevars['state']


def next_state():
    state(state() + 1)

text.add_text('Good morning, Dylan!', text.USER)
text.add_text('The sun is shining, birds are singing, and it\'s time to get out of bed!', text.EVENT)
text.add_text('Oh no! Looks like you\'re having some trouble there.  That\'s okay.  It\'s hard to get out of bed sometimes.')
text.add_text("Especially if you're feeling down.  Sometimes we have to battle our own brains to get through the day.")
text.add_text("Looks like you're a little low on dopamine.  Collect 20 dopamine points to get out of bed and start your day!", text.EVENT)

prog = 0.0

def next_scene():
    global curscene
    curscene += 1
    state(1)
    if curscene >= len(scenes):
        curscene = 0
    if scenes[curscene] == lunchscene:
        text.texts = []
        text.curtext = 0
        text.add_text('Heather calls you to join for lunch', text.USER)
        text.add_text('get pass anxiety and fear to make it to the table', text.EVENT)


def current_scene():
    return scenes[curscene]

prog = 0.0
def zero_prog():
    global prog
    prog = 0.0
    text.event_text()

running = True
while running:
    pressed = list(pygame.key.get_pressed())
    for event in pygame.event.get():
        if event.type == QUIT or pygame.key.get_pressed()[K_ESCAPE]:
            running = False
        if event.type == KEYDOWN:
            pressed[event.key] = True
            if event.key == K_SPACE:
                text.user_text()

        elif event.type == events.ADVANCETEXT:
            processed = text.process_event(event.advtype)
            if processed:
                print(state())
                if state() == 1 and current_scene() == bedscene:
                    print('waiting')
                    prog = 0.6
                    threading.Timer(3.0, zero_prog).start()
                elif state() == 1 and current_scene() == lunchscene:
                    platformer.start()
                next_state()


    if pressed[K_j]:
        next_scene()
        draw.draw_bg()
        pygame.display.update()
    if pressed[K_k]:
        curscene.devance()
    dt = clock.tick(60)

    current_scene().update(dt)
    current_scene().draw()
    if state() == 2 and current_scene() == lunchscene:
        prog = (platformer.player.x + 45) / 280.0
        if prog > 1.0:
            next_scene()
        platformer.platformscene.update(dt)
        platformer.platformscene.draw()
        draw.draw_surf(platformer.platformscene.rendertarget, (10, 64))
    if state() == 5 and current_scene() == bedscene:
        snake.update(dt, pressed)
        draw.draw_surf(snake.screen, (10, 64))
        prog = snake.score.score / 20.0
        if prog >= 1.0 or pressed[K_d]:
            next_scene()
    current_scene().set_progress(prog)
    draw.draw(textbox)
    text.draw_text(text.texts)
    draw.update()
