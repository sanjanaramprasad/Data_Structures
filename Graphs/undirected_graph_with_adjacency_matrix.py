class Graph(object):

    def __init__(self,object):
        self.vertexCount = int(object)
        self.adjMatrix = []
        for i in range(self.vertexCount):
            self.adjMatrix.append([0]*self.vertexCount)

    def addEdge(self, i , j):
        if (i>=0 and i<self.vertexCount and j>=0 and j<self.vertexCount):
            self.adjMatrix[i][j]=1
            self.adjMatrix[j][i]=1

    def removeEdge(self, i ,j):
        if(i>=0 and i<self.vertexCount and j>=0 and j<self.vertexCount):
            self.adjMatrix[i][j]= 0
            self.adjMatrix[j][i] = 0

    def isEdge(self,i,j):
        if(i>=0 and i<self.vertexCount and j>=0 and j<self.vertexCount):
            return self.adjMatrix[i][j]
        return False





if __name__=='__main__':

    graph_tester = Graph(4)
    graph_tester.addEdge(1,3)
    print graph_tester.adjMatrix
    print graph_tester.isEdge(1,3)

