from .text import *
import pygame
class Dialog:
    def  __init__(self,dialogName):
        self.dialogList = [["this is","A dialog page","with dialog offsets"],["This is","the second page","cool,right?"]] # will be a 2d array [[]]. Each subarray an screen dialog.
        self.maxChars = 20
        self.font = pygame.font.Font(None,25)

    def queueScreen(self):
        if self.dialogList == []:
            return
        offset = 0
        self.queue = []
        for t in self.dialogList[0]:
            self.queue.append(DynamicText(self.font,t,offset,autoreset=False))
            offset +=15
        offset = 0
        self.dialogList.pop(0)

    def alldone(self):
        return all(x.done for x in self.queue)

    def clear(self):
        self.queue = []

    def update(self):
        if self.queue == []:
            return
        for dialog in self.queue:
            if not dialog.done:
                dialog.update()
                break
            else:
                continue

    def qUpdate(self):
        if self.alldone():
            self.queueScreen()
        else:
            self.update()
    def draw(self,surface):
        drawBox(surface)
        for t in self.queue:
            t.drawText(surface)
