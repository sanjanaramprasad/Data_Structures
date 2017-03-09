from heapq import *


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, priority, ele):
        heappush(self.heap , (priority,ele))
        heapify(self.heap)

    def deleteMin(self):
        priority,ele = heappop(self.heap)
        return priority,ele
    def update(self,s,new_priority):
        heapreplace(self.heap(new_priority,s))



class Graph:

    def __init__(self):
        self.vertices=[]
        self.vertexCount = 0
        self.adjacency = {}

    def addVertex(self,label):
        if label not in self.vertices:
            self.vertices.append(label)
        else:
            print "Choose a new name for vertex"
        self.vertexCount+=1

    def addNewEdge(self,i,j,weight):
        if self.vertexCount:
            if (i>=0 and i<self.vertexCount and j>=0 and j<self.vertexCount):
                if i not in self.adjacency:
                    self.adjacency[i]={}
                self.adjacency[i][j]=weight


class ShortestPath:
    def __init__(self,graph, source):
        self.s = source
        self.pq = PriorityQueue()
        self.graph = graph
        self.distance=[]
        self.path={}
        self.pq.insert(0,self.s)
        self.blacklist = {}

    def dijkstra(self):
        self.distance=[0]*self.graph.vertexCount
        for i in range(self.graph.vertexCount):
            self.distance[i] = -1
        self.distance[self.s] = 0

        while(self.pq.heap):
            priority,ele = self.pq.deleteMin()
            if ele not in self.blacklist or priority not in self.blacklist[ele]:
                if ele in self.graph.adjacency:
                    for adj in self.graph.adjacency[ele]:
                        new_distance = self.distance[ele] + self.graph.adjacency[ele][adj]
                        if self.distance[adj] == -1 :
                            self.distance[adj] = new_distance
                            self.pq.insert(new_distance,adj)
                            self.path[adj] = ele

                        if new_distance < self.distance[adj]:
                            if adj in self.blacklist:
                                self.blacklist[adj].append(self.distance[adj])
                            else:
                                self.blacklist[adj]=[]
                                self.blacklist[adj].append(self.distance[adj])
                            self.distance[adj] = new_distance
                            self.pq.insert(new_distance,adj)
                            self.path[adj]=ele
        print self.path
        print self.distance

if __name__ == '__main__':
    graph = Graph()
    graph.addVertex(0)
    graph.addVertex(1)
    graph.addVertex(2)
    graph.addVertex(3)
    graph.addVertex(4)
    graph.addNewEdge(0, 1,4)
    graph.addNewEdge(0, 2,1)
    graph.addNewEdge(1, 4, 4)
    graph.addNewEdge(2, 3, 4)
    graph.addNewEdge(2, 1, 2)
    graph.addNewEdge(3, 4, 4)
    uw = ShortestPath(graph , 0)
    uw.dijkstra()




