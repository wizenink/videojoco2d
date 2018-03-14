import pygame
pygame.time.set_timer(pygame.USEREVENT, 200)
from game.constants import *
def text_generator(text):
    tmp = ''
    pos = 0
    if pos == 0:
        yield tmp
    for letter in text:
        pos = pos +1
        tmp += letter
        if letter != ' ':
            yield tmp


box = pygame.Rect(
           (WIN_WIDTH * 0.05),
            (WIN_HEIGHT * 0.65),
            WIN_WIDTH * 0.9 ,WIN_HEIGHT * 0.2)
box = box.inflate(-50,-10)
box2 = pygame.Rect(
           (WIN_WIDTH * 0.05),
            (WIN_HEIGHT * 0.65),
            WIN_WIDTH * 0.9 ,WIN_HEIGHT * 0.2)
box2 = box2.inflate(-50,-10)


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
        pos = box2.topleft
        screen.blit(self.rendered,(pos[0]+10,pos[1]+10+self.offset))


def drawBox(screen):
        pygame.draw.rect(screen,(0,0,0),box,0)
        pygame.draw.rect(screen,(255,255,255),box2,10)
