import pygame, gameobject

class Walker(gameobject.GameObject):
    def inc_frame(self):
        self.x -= 10
        self.draw_rect = self.draw_rect.move(self.width, 0)
        if self.draw_rect.x >= self.sheet.get_width():
            self.draw_rect.x = 0
        self.set_image()

    def dec_frame(self):
        self.x += 10
        gameobject.GameObject.dec_frame(self)
        if self.draw_rect.x <= 0:
            self.draw_rect.x = self.sheet.get_width() - self.width
