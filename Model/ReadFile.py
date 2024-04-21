from Model.Vertex import Vertex


def readFile(fileName : str):
    fileCutted = []
    listVertices = []
    file = open(fileName, "r")
    fileLines = file.readlines()
    for i in range(len(fileLines)):
        fileCutted.append(fileLines[i].split())
    for i in range(len(fileCutted)):
        listVertices.append(Vertex(fileCutted[i][0], int(fileCutted[i][1])))
    for i in range(len(fileCutted)):
        for j in range(2, len(fileCutted[i])):
            for k in range(len(listVertices)):
                if (fileCutted[i][j] == listVertices[k].value):
                    listVertices[i].addPreviousVertex(listVertices[k])
    listVertices = listVertices  
    file.close() 
    return listVertices