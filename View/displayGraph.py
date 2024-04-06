from Model.Graph import Graph
from tabulate import tabulate as tb

def DisplayGraph(graph : Graph) -> None:
    listVertices = graph.listV
    displayMatrix = []

    # Filling the matrix with zeros
    for i in range(len(listVertices)):
        displayMatrix.append([])
        for j in range(len(listVertices)):
            displayMatrix[i].append(0)
    
    # Replacing the 0 representing existing edges by 1
    for i in range(len(listVertices)):
        for j in range(len(listVertices[i].previousVertices)):
            displayMatrix[int(listVertices[i].previousVertices[j].value)][int(listVertices[i].value)] = 1

        # Multiplying the 1 and 0 in each row by the duration of the task
    for i in range(len(listVertices)):
        for k in range(len(displayMatrix[i])):
            displayMatrix[i][k] = displayMatrix[i][k] * int(listVertices[i].duration)

    # Displaying the Matrix in the terminal
    print(tb(displayMatrix, headers=list(range(len(listVertices))), showindex="always"))







