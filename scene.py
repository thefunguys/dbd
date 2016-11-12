import draw

class Scene:
    def __init__(self, rendertarget=draw.screen):
        self.gameobjects = []
        self.actor = None
        self.rendertarget = rendertarget
        self.bg_color = (20, 20, 20)

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
