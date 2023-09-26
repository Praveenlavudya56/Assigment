
class Garaps:
    def __init__(self,numOfNodes):
        self.noOfNodes=numOfNodes
        self.adjMatrix=[]
        for i in range(numOfNodes):
            row=[0]*(numOfNodes)
            self.adjMatrix.append(row)
        # print(self.adjMatrix)
    def addEdge(self,val1,val2):
        self.adjMatrix[val1][val2]=1
        # self.adjMatrix[val2][val1]=1
    def display(self):
        for i in self.adjMatrix:
            print(i)

g=Garaps(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(2,3)
g.addEdge(1,2)
g.addEdge(1,2)
g.display()


