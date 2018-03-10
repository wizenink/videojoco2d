import pygame
pygame.time.set_timer(pygame.USEREVENT, 200)
def text_generator(text):
    tmp = ''
    for letter in text:
        tmp += letter
        if letter != ' ':
            yield tmp

class DynamicText(object):
    def __init__(self, font, text,offset=0,autoreset=False):
        self.done = False
        self.font = font
        self.text = text
        self._gen = text_generator(self.text)
        self.autoreset = autoreset
        self.offset = offset
        self.update()

    def reset(self):
        self._gen = text_generator(self.text)
        self.done = False
        self.update()

    def update(self):
        if not self.done:
            try: self.rendered = self.font.render(next(self._gen), True, (230,230,230))
            except StopIteration:
                self.done = True
                if self.autoreset: self.reset()

    def drawText(self, screen):
        pos = self.box2.topleft
        screen.blit(self.rendered,(pos[0]+10,pos[1]+10+self.offset))


def drawBox(screen):
    self.box = pygame.Rect(
               (screen.get_width() * 0.05),
                (screen.get_height() * 0.65),
                screen.get_width() * 0.9 ,screen.get_height() * 0.2)
    self.box = self.box.inflate(-50,-10)
    self.box2 = pygame.Rect(
               (screen.get_width() * 0.05),
                (screen.get_height() * 0.65),
                screen.get_width() * 0.9 ,screen.get_height() * 0.2)
    self.box2 = self.box2.inflate(-50,-10)
    pygame.draw.rect(screen,(0,0,0),self.box,0)
    pygame.draw.rect(screen,(255,255,255),self.box2,10)
