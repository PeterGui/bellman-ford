import graph
import queue


class BellmanFord():

    def __init__(self, directed_graph):
        self.graph = directed_graph
        self.dist_to = [float('inf') for vertex in range(
            directed_graph.vCount())]
        self.edge_to = [None for vertex in range(directed_graph.vCount())]
        self.on_queue = [False for vertex in range(directed_graph.vCount())]
        self.queue = queue.Queue()
        self.find_shortest_paths(0)

    def find_shortest_paths(self, source):
        self.dist_to[source] = 0.0
        self.queue.enqueue(source)
        self.on_queue[source] = True
        while not self.queue.isEmpty():
            popped_vertex = self.queue.dequeue()
            self.on_queue[popped_vertex] = False
            self.chill(popped_vertex)

    def chill(self, popped_vertex):
        vertexLetter = self.get_letter(popped_vertex)
        for vertex in self.graph.adjacent[vertexLetter]:
            to_vertex = self.graph.vertexIndexMap[vertex]
            for edge in self.graph.edgeArray:
                if (edge[0] == popped_vertex and edge[1] == to_vertex):
                    toWeight = edge[2]
                    desiredEdge = edge
                    if (self.dist_to[to_vertex] > self.dist_to[popped_vertex] + toWeight):
                        self.edge_to[to_vertex] = desiredEdge
                        self.dist_to[to_vertex] = self.dist_to[popped_vertex] + toWeight
                        if(not self.on_queue[to_vertex]):
                            self.queue.enqueue(to_vertex)
                            self.on_queue[to_vertex] = True

    def get_letter(self, vertex):
        return self.graph.vertexIndexMap.keys()[
            self.graph.vertexIndexMap.values().index(vertex)]
