class Graph:
    def __init__(self):
        self.dict = {}
    def add_node(self,node):
        self.dict[node] = []
    def add_path(self,node1,node2,cost):
        #print(node1)
        n1 = self.dict[node1]
        n1.append((node2,cost))
        self.dict[node1] = n1
    def move_cost(self,a,b):
        if a == (47,18):
            print(self.dict[a])
        for x in self.dict[a]:
            x1,x2 = x
            x11,x12 = x1
            if (x11,x12) == b:
                return x2
        return None
    def get_vertex_neighbours(self, pos):
        x = []
        for n in self.dict[pos]:
            x.append(n[0])
        return x
    def heuristic(self, start, goal):
        #Heurística de Chebyshev
        D = 1
        D2 = 1
        dx = abs(start[0] - goal[0])
        dy = abs(start[1] - goal[1])
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)


def walkable(pos):
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
    #print(map[47][18])
    #print(walkable((47,18)))
    #print(walkable((48,18)))
    #print(walkable((47,19)))
    """for x in range(width-1):
        for y in range(height-1):
            if not walkable(map[x][y]):
                continue
            for i in range(-1,2):
                for j in range(-1,2):
                    if (i == 0) and (j == 0):
                        continue
                    if(walkable(map[x+i][y+j])):
                        graph.add_path((x,y),(x+i,y+j),1)
                    else:
                        graph.add_path((x,y),(x+i,y+j),100)"""
    for x in range(1,width-1):
        for y in range(1,height-1):
            if not walkable(map[x][y]):
                continue
            if(walkable(map[x+1][y])):
                graph.add_path((x,y),(x+1,y),1)
            else:
                graph.add_path((x,y),(x+1,y),100)
            if(walkable(map[x-1][y])):
                graph.add_path((x,y),(x-1,y),1)
            else:
                graph.add_path((x,y),(x-1,y),100)
            if(walkable(map[x][y+1])):
                graph.add_path((x,y),(x,y+1),1)
            else:
                graph.add_path((x,y),(x,y+1),100)
            if(walkable(map[x][y-1])):
                graph.add_path((x,y),(x,y-1),1)
            else:
                graph.add_path((x,y),(x,y-1),100)
    return graph


def AStarSearch(start, end, graph):

	G = {}
	F = {}


	G[start] = 0
	F[start] = graph.heuristic(start, end)

	closedVertices = set()
	openVertices = set([start])
	cameFrom = {}

	while len(openVertices) > 0:

		current = None
		currentFscore = None
		for pos in openVertices:
			if current is None or F[pos] < currentFscore:
				currentFscore = F[pos]
				current = pos

		if current == end:

			path = [current]
			while current in cameFrom:
				current = cameFrom[current]
				path.append(current)
			path.reverse()
			return path, F[end] #Done!


		openVertices.remove(current)
		closedVertices.add(current)


		for neighbour in graph.get_vertex_neighbours(current):
			if neighbour in closedVertices:
				continue
			candidateG = G[current] + graph.move_cost(current, neighbour)

			if neighbour not in openVertices:
				openVertices.add(neighbour)
			elif candidateG >= G[neighbour]:
				continue


			cameFrom[neighbour] = current
			G[neighbour] = candidateG
			H = graph.heuristic(neighbour, end)
			F[neighbour] = G[neighbour] + H

	raise RuntimeError("A* failed to find a solution")

def find_path(graph,start,end,path = []):
    return AStarSearch(start,end,graph)
"""def find_path(graph, start, end,path = []):
    path = path + [start]
    if start == end:
        return path
    if not (start in graph.dict):
        return None
    for node in graph.dict[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None"""
