import draw

class Scene:
    def __init__(self, rendertarget=draw.screen):
        self.gameobjects = []
        self.actor = None
        self.rendertarget = rendertarget
        self.bg_color = draw.bg_color

    def add(self, gameobject):
        self.gameobjects.append(gameobject)

    def add_actor(self, go):
        self.actor = go

    def draw(self, surface=None):
        draw.draw_bg(self.rendertarget, self.bg_color)
        if surface is None:
            surface = self.rendertarget
        for go in self.gameobjects:
            draw.draw(go, surface)
        if self.actor:
            draw.draw(self.actor, surface)

    def update(self, dt):
        for go in self.gameobjects:
            go.update(dt)

    def advance(self):
        if self.actor:
            self.actor.inc_frame()

    def devance(self):
        if self.actor:
            self.actor.dec_frame()

    def set_progress(self, progress):
        if progress >= 1.0:
            progress = 0.99
        if self.actor:
            pframe = int(progress * (self.actor.sheet.get_width() / self.actor.width))
            self.actor.set_frame(pframe)
            if self.actor.name == 'walker':
                self.actor.x = 570 - 200 * progress
