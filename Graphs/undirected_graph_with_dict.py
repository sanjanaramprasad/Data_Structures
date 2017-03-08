class Graph(object):

    def __init__(self,object):
        self.vertexCount = int(object)
        self.vertices ={}
        for i in range(self.vertexCount):
            self.vertices[i]=[0]*self.vertexCount

    def addEdge(self,i,j):
        i=i-1
        j=j-1
        if(i>=0 and i<self.vertexCount and j>=0 and j< self.vertexCount):
            self.vertices[i][j]=1
            self.vertices[j][i]=1
    def removeEdge(self,i,j):
        i,j=i-1,j-1
        if(i>=0 and i< self.vertexCount and j>=0 and j<self.vertexCount):
            self.vertices[i][j] =0
            self.vertices[i][j]=0




if __name__=='__main__':
    graph_dict = Graph(3)
    print graph_dict.vertices
    graph_dict.addEdge(1,3)
    print graph_dict.vertices
