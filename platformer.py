import pygame, gameobject, scene
from pygame.locals import *


class PlatformPlayer(gameobject.GameObject):
    def __init__(self):
        super().__init__('player', 'assets/walkingd.png', 100, 100)
        self.velocity = [0, 0]
        self.orientation = 1
        print(self.x)

    def update(self, dt):
        floor = 134
        if self.velocity[0] != 0:
            self.cycle_frame(dt)
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.velocity[0] = -30
            self.orientation = 1
        elif keys[K_RIGHT]:
            self.velocity[0] = 30
            self.orientation = -1
        else:
            self.velocity[0] = 0
            self.set_frame(0)
        if keys[K_UP] and self.y >= floor:
            self.velocity[1] = -200

        if self.y < floor:
            self.velocity[1] += 10
        elif self.y > floor:
            self.y = floor
            self.velocity[1] = 0

        self.x += self.velocity[0] * dt / 1000.0
        self.y += self.velocity[1] * dt / 1000.0


def block(x, y, w, h):
    block_surf = pygame.Surface((w, h)).convert()
    block_surf.fill((20, 20, 20))
    blocky = gameobject.GameObject('block', 'assets/bed.png', x, y, w, h, block_surf)
    return blocky

disp = pygame.Surface((320, 240))
player = PlatformPlayer()

platformscene = scene.Scene(disp)
platformscene.add(player)
platformscene.add(block(10, 10, 32, 32))
platformscene.bg_color = (100, 120, 200)