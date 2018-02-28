class Scene:
    map = [[]]
    tilemap = []
    name = ""
    width = 0
    height = 0
    def __init__(self,name,width,height,map):
        self.name = name
        self.height = height
        self.width = width
        self.map = map
