import draw

class Scene:
    def __init__(self):
        self.gameobjects = []
        self.actor = None

    def add(self, gameobject):
        self.gameobjects.append(gameobject)

    def add_actor(self, go):
        self.actor = go

    def draw(self):
        for go in self.gameobjects:
            draw.draw(go)
        draw.draw(self.actor)

    def update(self, dt):
        for go in self.gameobjects:
            go.update(dt)

    def advance(self):
        if self.actor:
            self.actor.inc_frame()

    def devance(self):
        if self.actor:
            self.actor.dec_frame()
