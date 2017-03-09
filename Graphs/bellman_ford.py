from heapq import *
from numpy import inf

class Queue:
    def __init__(self):
        self.queue =[]

    def insert(self,ele):
        self.queue.append(ele)

    def delete(self):
        ele = self.queue[0]
        self.queue = self.queue[1:]
        return ele


class Graph:

    def __init__(self):
        self.vertexCount=0
        self.vertices=[]
        self.adjacency={}

    def addVertex(self,label):
        self.vertexCount +=1
        self.vertices.append(label)

    def addNewEdge(self,i,j,weight):
        if self.vertexCount != 0:
            if(i>=0 and i<self.vertexCount and j>=0 and j<self.vertexCount):
                if i in self.adjacency:
                    self.adjacency[i][j] = weight
                else:
                    self.adjacency[i]={}
                    self.adjacency[i][j] = weight


class ShortestPath:
    def __init__(self,graph,source):
        self.queue = Queue()
        self.distance=[]
        self.graph = graph
        self.s = source
        self.path={}
    def bellman_ford(self):
        self.distance=[inf]*self.graph.vertexCount
        self.distance[self.s] = 0
        for i in range(self.graph.vertexCount):
            for each in self.graph.vertices:
                for adj in self.graph.adjacency[each]:
                    new_distance = self.distance[each] + self.graph.adjacency[each][adj]

                    if new_distance < self.distance[adj]:
                        self.distance[adj] = new_distance
                        self.path[adj] = each
        print self.distance
        print self.path



if __name__ == '__main__':
    graph = Graph()
    graph.addVertex(0)
    graph.addVertex(1)
    graph.addVertex(2)
    graph.addVertex(3)
    graph.addVertex(4)
    graph.addVertex(5)
    graph.addNewEdge(0, 1, 10)
    graph.addNewEdge(0, 5 , 8)
    graph.addNewEdge(1, 3 , 2)
    graph.addNewEdge(2, 1, 1)
    graph.addNewEdge(3, 2, -2)
    graph.addNewEdge(4, 3, -1)
    graph.addNewEdge(4, 1, -4)
    graph.addNewEdge(5, 4, 1)
    uw = ShortestPath(graph , 0)
    uw.bellman_ford()




