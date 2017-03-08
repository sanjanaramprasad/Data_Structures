#Start with indices that have an indegree of 0 and add them to queue, go to their adjacent nodes and decrease their indegree by one.
# Once it becomes 0 for a node. Add to queue and repeat same


class Queue:
    def __init__(self):
        self.queue =[]
    def insert(self, ele):
        self.queue.append(ele)
    def remove(self):
        ele = self.queue[0]
        self.queue= self.queue[1:]
        return ele
    def delete(self):
        self.queue[:] = []
        print self.queue
class Vertex(object):
    def __init__(self,object):
        self.label = object
        self.inDegree = 0


class Graph:

    def __init__(self):
        self.counter = 0
        self.vertices =[]
        self.vertexCount =0
        self.adjacencyMatrix = []
        self.Queue = Queue()

    def addVertex(self, v):
        self.vertexCount+=1
        vertex = Vertex(v)
        self.vertices.append(vertex)

    def addNewEdge(self,i,j):
        if self.vertexCount == 0:
            print("Please add vertex first")
        if not self.adjacencyMatrix:
            self.adjacencyMatrix = [[0]*self.vertexCount for count in range(self.vertexCount)]
        if(i>=0 and i<self.vertexCount and j>=0 and j<self.vertexCount):
            self.adjacencyMatrix[i][j] = 1
            self.vertices[j].inDegree +=1

    def topologicalSort(self):
        for each in self.vertices:
            if each.inDegree == 0:
                self.Queue.insert(each)
        while(self.Queue.queue):
            string = ",".join([str(each.label) for each in self.Queue.queue])
            print string
            v1 = self.Queue.remove()
            index = self.vertices.index(v1)
            self.counter += 1
            for adj in range(self.vertexCount):
                if self.adjacencyMatrix[index][adj] == 1:
                    self.vertices[adj].inDegree -=1
                    if(self.vertices[adj].inDegree == 0):
                        self.Queue.insert(self.vertices[adj])
        if(self.counter != self.vertexCount):
            print "Graph has cycles"

        self.Queue.delete()




if __name__ == '__main__':
    graph = Graph()
    graph.addVertex(0)
    graph.addVertex(1)
    graph.addVertex(2)
    graph.addVertex(3)
    graph.addVertex(4)
    graph.addVertex(5)
    graph.addVertex(6)
    graph.addVertex(7)
    graph.addNewEdge(0, 3)
    graph.addNewEdge(0, 4)
    graph.addNewEdge(1, 3)
    graph.addNewEdge(2, 4)
    graph.addNewEdge(2, 7)
    graph.addNewEdge(3, 5)
    graph.addNewEdge(3, 6)
    graph.addNewEdge(3, 7)
    graph.addNewEdge(4, 6)
    #graph.addNewEdge(3, 7)
    graph.topologicalSort()





