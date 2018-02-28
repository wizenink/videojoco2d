import os

class resourceManager(object):

    __instance = None

    resources = {}

    @staticmethod
    def getInstance():
        if resourceManager.__instance == None:
            resourceManager()
        return __instance

    def __init__(self):
        if resourceManager.__instance != None:
            raise Exception("This class is a singleton")
        else:
            resourceManager.__instance = self

    @classmethod
    def loadImage(cls, name, colorkey = None):
        if name in cls.resources:
            return cls.resources[name]
        else:
            fullname = os.path.join('image',name)
            cls.resources[name] = imagen
            return image

s = resourceManager()
s1 = resourceManager.getInstance()
print(s)
print(s1)
