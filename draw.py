import pygame

pygame.init()
update_rects = []
screen = pygame.display.set_mode((640, 480), pygame.DOUBLEBUF | pygame.HWSURFACE)

border = pygame.Surface(screen.get_size()).convert()
bgrect = screen.get_size()
background = pygame.Surface((bgrect[0] - 6, bgrect[1] - 6)).convert()
bg_color = (80, 100, 150)
background.fill(bg_color)
screen.blit(background, (0, 0))
pygame.display.update()

font = pygame.font.Font('assets/dejavu.ttf', 18)
print(font.size('hello'))


def draw(go, surface=screen):
    update_rects.append(pygame.Rect(go.x, go.y, go.width, go.height))
    surface.blit(go.image, (go.x, go.y))

def draw_surf(surface, loc, target=screen):
    update_rects.append(surface.get_rect(topleft=loc))
    target.blit(surface, loc)

def update():
    pygame.display.update()
    del update_rects[:]

def draw_bg(surface=screen, bg_color=bg_color):
    if bg_color != background.get_at((0, 0)):
        background.fill(bg_color)
    surface.blit(border, (0, 0))
    surface.blit(background, (3, 3))

def write(text, surface=screen):
    drawText(surface, text, (0, 0, 0), pygame.Rect(80, 370, 480, 100), font)

def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2
 
    # get the height of the font
    fontHeight = font.size("Tg")[1]
 
    while text:
        i = 1
 
        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break
 
        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1
 
        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1
 
        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)
 
        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing
 
        # remove the text we just blitted
        text = text[i:]
 
    return text
