from Model.Vertex import Vertex
from Model.ReadFile import readingFile

class Graph:
    def __init__(self, name : str, fileName : str) -> None:
        self.name = name
        self.listV = readingFile(fileName)
 

    def addVertexAlphaOmega(self, listVertexNoPredecessor : list[Vertex], listVertexNoSuccessor : list[Vertex]):  
        nbVertex = len(self.ListV)
        alpha = Vertex("0", 0)
        omega = Vertex(str(nbVertex+1),0)
        for i in range(len(listVertexNoPredecessor)):
            listVertexNoPredecessor[i].addPreviousVertex(alpha)
        for i in range(len(listVertexNoSuccessor)):
            omega.addPreviousVertex(listVertexNoSuccessor[i])
