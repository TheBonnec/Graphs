from Model.Vertex import Vertex

def addVertexAlphaOmega(listVertices : list[Vertex]):  
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
    listVertices.append(alpha)
    listVertices.append(omega)
    return listVertices