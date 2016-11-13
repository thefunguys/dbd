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
essay = gameobject.GameObject('essay', 'assets/essay.png', 340, 100, 32, 32, 8)

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
text.add_text('Oh no! Looks like you\'re having some trouble there. That\'s okay. It\'s hard to get out of bed sometimes.')
text.add_text("Especially if you're feeling down. Sometimes we have to battle our own brains to get through the day.")
text.add_text("Looks like you're a little low on dopamine. Collect 20 dopamine points to get out of bed and start your day!", text.EVENT)
text.add_text("Good job, Dylan! You made a really important step in your day!")
text.add_text("Oh! Look at the time! You're late for lunch with your friend Heather! You better hurry!")
text.add_text("")

prog = 0.0

def next_scene():
    global curscene
    curscene += 1
    state(1)
    print(state(), curscene)
    if curscene >= len(scenes):
        curscene = 0
    if scenes[curscene] == lunchscene:
        text.texts = []
        text.curtext = 0
        text.add_text("Look! Heather already got a table! You should sit with her", text.USER)
        text.add_text("It's okay. Take your time. Social interactions can be scary. But if you overcome some of your own fears and anxieties, you'll have a great time!", text.EVENT)
        text.add_text("Great job Dylan! You are really making progress. Heather is happy to see you, and you have a great lunch!")
        text.add_text("But don't forget! You have an essay due in a few hours!")
        text.add_text("Your essay is a one-page report on the importance of traffic lights. Good luck!")
        text.add_text('')
    if scenes[curscene] == essayscene:
        text.texts = []
        text.curtext = 0
        text.add_text("Oh no! Looks like you're having a hard time there. Don't worry. Take your time. Breathe. Just take it one word at a time.", text.EVENT)
        text.add_text("You did it! You did a great job. I bet you'll get an A+")
        text.add_text('')
    if scenes[curscene] == bedscene:
        text.add_text("Wow! You made it through the day. You are amazing!")
        text.add_text("I know today was hard, but don't worry. Tomorrow will be easier. Just remember to take it one day, one step, one word at a time.")
        text.add_text("You are going to be okay")
        


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
        if event.type == QUIT or pressed[K_ESCAPE]:
            running = False
        if event.type == KEYDOWN:
            pressed[event.key] = True
            if event.key == K_SPACE:
                text.user_text()

        elif event.type == events.ADVANCETEXT:
            processed = text.process_event(event.advtype)
            if processed:
                print(state(), processed.text)
                if state() == 1 and current_scene() == bedscene:
                    print('waiting')
                    prog = 0.6
                    threading.Timer(3.0, zero_prog).start()
                elif state() == 6 and current_scene() == bedscene:
                    next_scene()
                    prog = 0.0
                elif state() == 1 and current_scene() == lunchscene:
                    platformer.start()
                elif state() == 6 and current_scene() == lunchscene:
                    prog = 0.0
                    next_scene()
                next_state()


    dt = clock.tick(60)

    current_scene().update(dt)
    current_scene().draw()
    if state() == 3 and current_scene() == lunchscene:
        if not platformer.player:
            platformer.start()
        prog = (platformer.player.x + 45) / 280.0
        if prog > 1.0 or pressed[K_d]:
            text.event_text()
        platformer.platformscene.update(dt)
        platformer.platformscene.draw()
        draw.draw_surf(platformer.platformscene.rendertarget, (10, 64))
    if state() == 5 and current_scene() == bedscene:
        snake.update(dt, pressed)
        draw.draw_surf(snake.screen, (10, 64))
        prog = snake.score.score / 20.0
        if prog >= 1.0 or pressed[K_d]:
            text.event_text()
    current_scene().set_progress(prog)
    draw.draw(textbox)
    text.draw_text(text.texts)
    draw.update()
