import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, name, imgname, x, y, w=32, h=32):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.scale = 4
        self.x = x
        self.y = y
        self.width = w * self.scale
        self.height = h * self.scale
        self.draw_rect = pygame.rect.Rect(0, 0, self.width, self.height)
        self.sheet = pygame.image.load(imgname)
        self.sheet = pygame.transform.scale(self.sheet, (self.sheet.get_width() * self.scale, self.sheet.get_height() * self.scale))
        print(self.name)
        print(self.sheet.get_width())
        self.set_image()
        self.frame_elapsed = 0.0

    def set_image(self):
        self.image = pygame.Surface(self.draw_rect.size).convert()
        self.image.blit(self.sheet, (0, 0), self.draw_rect)
        self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)

    def inc_frame(self):
        self.draw_rect = self.draw_rect.move(self.width, 0)
        if self.draw_rect.x >= self.sheet.get_width():
            self.draw_rect.x -= self.width
        self.set_image()

    def dec_frame(self):
        self.draw_rect = self.draw_rect.move(-self.width, 0)
        if self.draw_rect.x < 0:
            self.draw_rect = self.draw_rect.move(self.width, 0)
        self.set_image()

    def update(self, dt):
        self.frame_elapsed += dt
        if self.frame_elapsed < 300:
            return
        self.frame_elapsed = 0.0
        self.draw_rect = self.draw_rect.move(self.width, 0)
        if self.draw_rect.x >= self.sheet.get_width():
            self.draw_rect.x = 0
        self.set_image()
        
