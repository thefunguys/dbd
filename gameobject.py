import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, name, imgname, x, y, w=32, h=32, scale=4, surface=None):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.scale = scale
        self.x = x
        self.y = y
        self.width = w * self.scale
        self.height = h * self.scale
        self.orientation = 1
        self.draw_rect = pygame.rect.Rect(0, 0, self.width, self.height)
        if surface:
            self.sheet = surface
        else:
            self.sheet = pygame.image.load(imgname).convert()
        self.sheet = pygame.transform.scale(self.sheet, (self.sheet.get_width() * self.scale, self.sheet.get_height() * self.scale))
        print(self.name + ' loaded')
        self.set_image()
        self.frame_elapsed = 0.0

    def set_image(self):
        self.image = pygame.Surface(self.draw_rect.size).convert()
        self.image.blit(self.sheet, (0, 0), self.draw_rect)
        self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)
        if self.orientation == -1:
            self.image = pygame.transform.flip(self.image, True, False)

    def set_frame(self, frameno):
        self.draw_rect = pygame.Rect(frameno * self.width, 0, self.width, self.height)
        self.set_image()

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

    def cycle_frame(self, dt):
        self.frame_elapsed += dt
        if self.frame_elapsed < 300:
            return
        self.frame_elapsed = 0.0
        self.draw_rect = self.draw_rect.move(self.width, 0)
        if self.draw_rect.x >= self.sheet.get_width():
            self.draw_rect.x = 0
        self.set_image()

    def update(self, dt):
        self.cycle_frame(dt)
        
