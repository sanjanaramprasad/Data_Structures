class Vertex(object):
    def __init__(self,object):
        self.label = object
        self.visited = False



class Graph():
    def __init__(self):
        self.vertex=[]
        self.adjMatrix=[]
        self.vertexCount=0
        self.stack = []

    def addVertex(self,label):
        new_vertex = Vertex(label)
        self.vertex.append(new_vertex)
        self.vertexCount+=1

    def addNewEdge(self,i,j):
        i,j = i-1, j-1
        if self.vertexCount<1:
            print("Please add more vertices")

        if not self.adjMatrix:
            self.adjMatrix = [[0] * self.vertexCount for k in range(self.vertexCount)]

        if(i>=0 and i<self.vertexCount and j>=0 and j<self.vertexCount):
            self.adjMatrix[i][j]=1
            self.adjMatrix[j][i] =1

    def displayVertex(self,index):
        print("Vertex :" + str(self.vertex[index-1].label))

    def getAdjUnvisitedVertex(self,v):
        for adj in range(self.vertexCount):
            #print adj, v
            if(self.adjMatrix[v][adj] == 1 and self.vertex[adj].visited == False):
                #print "here"
                return adj
        return -1
    def dfs(self):
        self.vertex[0].visited = True
        self.displayVertex(1)
        self.stack.append(0)
        while(self.stack):
            #print self.stack
            #print "here"
            v = self.getAdjUnvisitedVertex(self.stack[-1])

            if v == -1:
                self.stack.pop()
            else:
                self.vertex[v].visited = True
                self.displayVertex(v+1)
                self.stack.append(v)
        #resetting flags
        for q in range(self.vertexCount):
            self.vertex[q].visited= False








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
    graph.addNewEdge(1,2)
    graph.addNewEdge(2,5)
    graph.addNewEdge(2,3)
    graph.addNewEdge(3,6)
    graph.addNewEdge(3,4)
    graph.addNewEdge(5,6)
    graph.addNewEdge(6,7)
    graph.addNewEdge(6,8)
    #print graph.adjMatrix
    #graph.displayVertex(2)
    graph.dfs()


