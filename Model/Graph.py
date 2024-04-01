from Vertex import Vertex

class Graph:
    def __init__(self, name : str, fileName : str) -> None:
        self.name = name
        fileCutted = 0
        ListV = 0
        file = open(fileName, "r")
        for i in range(len(file)):
            fileCutted[i] = file.readlines[i].split()
        for i in range(len(fileCutted)):
            ListV[i]=Vertex(fileCutted[i][0], fileCutted[i][1])

        for i in range(len(ListV)):
            for j in range(1, len(fileCutted[i])):
                for k in range(len(ListV)):
                    if (fileCutted[i][j] == ListV[k].value):
                        ListV[i].addNextVertex(ListV[k])
        self.ListV = ListV  
        file.close()  