from Model.ReadFile import readFile
from Model.Vertex import Vertex


class Graph:
    def __init__(self, name : str, fileName : str) -> None:
        self.name : str = name
        self.fileName = fileName
        self.listVertices : list[Vertex] = self.getVertices(fileName = fileName)


    
    def getVertices(self, fileName: str) -> list[Vertex]:
        listVertices = readFile(fileName = fileName)
        self.addVertexAlphaOmega(listVertices = listVertices)
        return listVertices



    def addVertexAlphaOmega(self, listVertices : list[Vertex]):
        nbVertex = len(listVertices)
        alpha = Vertex("0", 0)
        omega = Vertex(str(nbVertex+1),0)
        for i in range(len(listVertices)):
            if (listVertices[i].previousVertices == []):
                listVertices[i].previousVertices.append(alpha)
        for i in range(len(listVertices)):
            notSuccessor = 1
            for j in range(len(listVertices)):
                for k in range(len(listVertices[j].previousVertices)):
                    if (listVertices[i].value == listVertices[j].previousVertices[k].value):
                        notSuccessor = 0
            if (notSuccessor == 1):
                omega.addPreviousVertex(listVertices[i])
        listVertices.insert(0, alpha)
        listVertices.append(omega)