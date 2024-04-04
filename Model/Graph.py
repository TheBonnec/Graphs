from Model.Vertex import Vertex
from Model.ReadFile import readingFile
from Model.addAlphaOmega import addVertexAlphaOmega

class Graph:
    def __init__(self, name : str, fileName : str) -> None:
        self.name : str = name
        listV = readingFile(fileName)
        listV = addVertexAlphaOmega(listV)
        self.listV : list[Vertex] = listV