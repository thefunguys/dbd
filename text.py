import draw, pygame, events

USER = 1
EVENT = 2


class Text(object):
    def __init__(self, text, type=USER):
        self.text = text
        self.type = type

texts = [Text('', USER)]
curtext = 0

def add_text(text, type=USER):
    texts.append(Text(text, type))

def process_event(type):
    global curtext
    if texts[curtext].type == type and len(texts) > curtext + 1:
        curtext += 1

def draw_text():
    draw.write(texts[curtext].text)

def user_text():
    pygame.event.post(pygame.event.Event(events.ADVANCETEXT, advtype=USER))

def event_text():
    pygame.event.post(pygame.event.Event(events.ADVANCETEXT, advtype=EVENT))
