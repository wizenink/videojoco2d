from text import *

class Dialog:
    def  __init__(self,dialogName):
        self.dialogList = resourceManager.loadDialog(dialogName) # will be a 2d array [[]]. Each subarray an screen dialog.
        self.maxChars = 20
        self.font = None

    def queueScreen(self):
        if self.dialogList == []:
            return
        self.queue = []
        for t in self.dialogList[0]:
            self.queue.append(DynamicText(font,t,offset,autoreset=False))
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

    def draw(self,surface):
        drawBox(surface)
        for t in self.queue:
            t.drawText(surface)
