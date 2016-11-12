import pygame

update_rects = []
screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)

background = pygame.Surface(screen.get_size()).convert()
background.fill((220, 220, 220))
screen.blit(background, (0, 0))
pygame.display.update()

def draw(go):
    update_rects.append(pygame.Rect(go.x, go.y, go.width, go.height))
    screen.blit(go.image, (go.x, go.y))

def update():
    global update_rects
    pygame.display.update(update_rects)
    update_rects = []

def draw_bg():
    screen.blit(background, (0, 0))
