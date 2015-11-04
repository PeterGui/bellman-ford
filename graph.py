from collections import OrderedDict


class graph:

    def __init__(self):
        self.vertexNameArray = []
        self.vertexIndexMap = {}
        self.vertexPositionArray = []
        self.edgeArray = []
        self.adjacent = OrderedDict()

    def addVertex(self, name, x, y):
        self.vertexIndexMap[name] = self.vCount()
        self.vertexNameArray.append(name)
        self.vertexPositionArray.append((x, y))
        if name not in self.adjacent:
            self.adjacent[name] = []

    def addEdge(self, vName1, vName2, weight):
        self.edgeArray.append((self.vertexIndexMap[vName1],
                               self.vertexIndexMap[vName2], weight))
        self.adjacent[vName1].append(vName2)
        self.adjacent[vName2].append(vName1)

    def vCount(self): return len(self.vertexNameArray)

    def eCount(self): return len(self.edgeArray)

    def reverse(self):
        reversedGraph = graph()
        reversedGraph.adjacent = self.adjacent
        reversedGraph.edgeArray = [(edge[1], edge[0], edge[2]) for
                                   edge in self.edgeArray]
        reversedGraph.vertexIndexMap = self.vertexIndexMap
        reversedGraph.vertexNameArray = self.vertexNameArray
        reversedGraph.vertexPositionArray = self.vertexPositionArray
        return reversedGraph

    # Access functions for vertex information
    def vX(self, i):
        return self.vertexPositionArray[i][0]

    def vY(self, i):
        return self.vertexPositionArray[i][1]

    def vName(self, i):
        return self.vertexNameArray[i]

    # Access functions for edge information
    def eV0X(self, i):
        return self.vertexPositionArray[self.edgeArray[i][0]][0]

    def eV0Y(self, i):
        return self.vertexPositionArray[self.edgeArray[i][0]][1]

    def eV1X(self, i):
        return self.vertexPositionArray[self.edgeArray[i][1]][0]

    def eV1Y(self, i):
        return self.vertexPositionArray[self.edgeArray[i][1]][1]

    def eVX(self, i):
        return self.vertexPositionArray[i][0]

    def eVY(self, i):
        return self.vertexPositionArray[i][1]

    def eWght(self, i):
        return self.edgeArray[i][2]
