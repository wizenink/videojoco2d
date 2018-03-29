class Graph:
    def __init__(self):
        self.dict = {}
    def add_node(self,node):
        self.dict[node] = []
    def add_path(self,node1,node2):
        n1 = self.dict[node1]
        n2 = self.dict[node2]
        n1.append(node2)
        n2.append(node1)
        self.dict[node1] = n1
        self.dict[node2] = n2

def walkable(pos):
    print(pos)
    if pos == 0:
        return False
    else:
        return True

def toGraph(map):
    height = len(map)
    width = len(map[0])
    graph = Graph()
    for x in range(width):
        for y in range(height):
            graph.add_node((x,y))
    for x in range(width-1):
        for y in range(height-1):
            if not walkable(map[x][y]):
                continue
            if walkable(map[x+1][y]):
                graph.add_path((x,y),(x+1,y))
            if walkable(map[x][y+1]):
                graph.add_path((x,y),(x,y+1))
            if walkable(map[x+1][y+1]):
                graph.add_path((x,y),(x+1,y+1))
    return graph


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not (start in graph.dict):
        return None
    for node in graph.dict[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None
