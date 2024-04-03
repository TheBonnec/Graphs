from Model.Vertex import Vertex

def readingFile(fileName : str):
    fileCutted = []
    listV = []
    file = open(fileName, "r")
    fileLines = file.readlines()
    for i in range(len(fileLines)):
        fileCutted.append(fileLines[i].split())
    for i in range(len(fileCutted)-1):
        listV.append(Vertex(fileCutted[i][0], fileCutted[i][1]))

    for i in range(len(listV)):
        for j in range(1, len(fileCutted[i])):
            for k in range(2, len(listV)):
                if (fileCutted[i][j] == listV[k].value):
                    listV[i].addPreviousVertex(listV[k])
    listV = listV  
    file.close() 
    return listV