class Vertex(object):
    def __init__(self,object):
        self.visited = False
        self.label = object


class Queue():
    def __init__(self):
        self.queue = []

    def insert(self , ele):
        self.queue.append(ele)

    def remove(self):
        ele = self.queue[0]
        self.queue = self.queue[1:]
        return ele

class Graph():
    def __init__(self):
        self.vertexList = []
        self.adjacencyMatrix = []
        self.Queue = Queue()
        self. vertexCount = 0

    def addVertex(self , label):
        self.vertexCount+=1
        vertex = Vertex(label)
        self.vertexList.append(vertex)

    def addNewEdge(self,i,j):
        i,j = i-1,j-1
        if self.vertexCount == 0:
            print "Please add more vertices"
        if not self.adjacencyMatrix:
            self.adjacencyMatrix=[[0]*self.vertexCount for vertices in range(self.vertexCount)]
        if (i>=0 and i<self.vertexCount and j>=0 and j<self.vertexCount):
            self.adjacencyMatrix[i][j] = 1
            self.adjacencyMatrix[j][i] = 1

    def displayVertex(self,v):
        #print self.vertexList[v].label
        print ('Vertex : ' + str(self.vertexList[v].label))

    def getAdjUnvisitedVertex(self, vertex):
        for a in range(self.vertexCount):
                if(self.adjacencyMatrix[vertex][a] ==1 and self.vertexList[a].visited == False):
                    return a

        return -1


    def bfs(self):
        self.vertexList[0].visited = True
        self.displayVertex(0)
        self.Queue.insert(0)
        #v2 = 0
        while (self.Queue.queue):
            #print self.Queue.queue
            v2 = 0
            v1 = self.Queue.remove()
            #print v1
            while(v2!=-1):
                v2 = self.getAdjUnvisitedVertex(v1)
                if v2!=-1:
                    self.vertexList[v2].visited = True
                    self.displayVertex(v2)
                    self.Queue.insert(v2)






if __name__ == '__main__':
    graph = Graph()
    graph.addVertex(1)
    graph.addVertex(2)
    graph.addVertex(3)
    graph.addVertex(4)
    graph.addVertex(5)
    graph.addVertex(6)
    graph.addVertex(7)
    graph.addVertex(8)
    graph.addNewEdge(1, 2)
    graph.addNewEdge(2, 5)
    graph.addNewEdge(2, 3)
    graph.addNewEdge(3, 6)
    graph.addNewEdge(3, 4)
    graph.addNewEdge(5, 6)
    graph.addNewEdge(6, 7)
    graph.addNewEdge(6, 8)
    #print graph.adjacencyMatrix
    graph.bfs()
