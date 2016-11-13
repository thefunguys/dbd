import pygame, gameobject, scene, threading
from pygame.locals import *

enemies = []

def halfrect(rect):
    rect.x += 0.33 * rect.w
    rect.w /= 3
    rect.y += 0.25 * rect.h
    rect.h /= 2
    return rect

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

class PlatformPlayer(gameobject.GameObject):
    def __init__(self):
        super().__init__('player', 'assets/walkingd.png', -45, 133)
        self.velocity = [0, 0]
        self.orientation = -1
        self.crouch = pygame.image.load('assets/crouch.png').convert()
        self.crouch = pygame.transform.scale(self.crouch, (self.crouch.get_width() * self.scale, self.crouch.get_height() * self.scale))
        self.orig_sheet = self.sheet
        print(self.x)

    def update(self, dt):
        self.sheet = self.orig_sheet
        floor = 134
        if self.velocity[0] != 0:
            self.cycle_frame(dt)
        keys = pygame.key.get_pressed()
        if keys[K_DOWN]:
            self.velocity[0] = 0
            floor = 172
            self.sheet = self.crouch
            self.set_frame(0)
            self.set_image()
            self.y += 16
        elif keys[K_LEFT]:
            self.velocity[0] = -30
            self.orientation = 1
        elif keys[K_RIGHT]:
            self.velocity[0] = 30
            self.orientation = -1
        else:
            self.velocity[0] = 0
            self.set_frame(0)
        if keys[K_UP] and self.y >= floor:
            self.velocity[1] = -250

        if self.y < floor:
            self.velocity[1] += 10
        elif self.y > floor:
            self.y = floor
            self.velocity[1] = 0

        prect = pygame.Rect(self.x, self.y, self.width, self.height)
        prect = halfrect(prect)
        for enemy in enemies:
            enemyrect = enemy.draw_rect.move((enemy.x, enemy.y))
            enemyrect = halfrect(enemyrect)
            if prect.colliderect(enemyrect):
                self.x -= 50
                if self.x < -45:
                    self.x = -45

        self.x += self.velocity[0] * dt / 1000.0
        self.y += self.velocity[1] * dt / 1000.0


class PlatformEnemy(gameobject.GameObject):
    def __init__(self, name, x=300, y=220):
        super().__init__(name, 'assets/' + name + '.png', x, y, 16, 16, 2)
        self.velocity = [-100, 0]

    def update(self, dt):
        self.x += self.velocity[0] * dt / 1000.0


def angst(x=550):
    angsto = PlatformEnemy('angst', x)
    platformscene.add(angsto)
    enemies.append(angsto)


def fear(x=300):
    fearo = PlatformEnemy('fear', x, 152)
    platformscene.add(fearo)
    enemies.append(fearo)


platformscene = None
player = None

def start():
    global platformscene, player
    disp = pygame.Surface((320, 240))
    player = PlatformPlayer()

    platformscene = scene.Scene(disp)
    platformscene.add(player)
    del enemies[:]
    for i in range(20):
        angst(450 + 300 * i)
    for i in range(20):
        fear(300 + 300 * i)

    platformscene.bg_color = (200, 200, 200)
