from Model.Graph import Graph
from Model.Vertex import Vertex
import copy

def verifyCycle(graph: Graph) -> bool:
    # Rosalind Marimond Algorithm to verify if a graph contains a cycle
    print("\nDetecting the cycle, by using the elimination by predecessors method.")

    eliminateList = []
    # we iterate while the eliminate vertices is not equal to the number of vertices in the graph
    while len(eliminateList) < len(graph.listVertices):
        sourceVertices = []
        remainingVertices = list(graph.listVertices)
        tempList = eliminateList.copy()

        # we iterate through the vertices in the graph
        for vertex in graph.listVertices:
            predecessors = list(vertex.previousVertices)

            """print("Vertex: ", vertex.value)
            for predecessor in predecessors:
                print("Predecessor: ", predecessor.value)"""
            # if the vertex is not in the eliminate list and it has no more predecessors, we add it to the source vertices
            if vertex not in eliminateList: 
                resultPredecessors = [p for p in predecessors if p not in eliminateList]
                if resultPredecessors == []:
                    tempList.append(vertex)
                    sourceVertices.append(vertex.value)

        remainingVertices = [vertex for vertex in remainingVertices if vertex not in tempList]   
        eliminateList = tempList

        # if the source vertices list is empty after running through all vertices, there is a cycle in the graph
        if sourceVertices == [] and len(eliminateList) < len(graph.listVertices):
            print("\n\nCycle detected.")
            return True # Cycle detected

        # we print the source and the remaining vertices step by step for the traces
        print("\nSource vertices: ", sourceVertices)
        print("Eliminating source vertices...")
        print("Remaining vertices: ", end = "")
        if remainingVertices == []: print("None")
        for vertex in remainingVertices:
            print(vertex.value, end = " ")

    print("\nNo cycle detected.")
    return False # No cycle detected


def hasNegativeEdges(graph: Graph) -> bool:
    for vertex in graph.listVertices:
        for neighbor in vertex.previousVertices:
            if float(neighbor.duration) < 0:
                print("Negative-weight edge detected.")
                return True  # Negative edge detected
    print("No negative-weight edge detected.")
    return False  # No negative edge detected


def computeRanks(graph: Graph) -> dict:
    # use of a dictionnary to store the ranks
    ranks = {vertex: 0 for vertex in graph.listVertices}
    eliminateList = []
    k = 0
    # same algorithm as verifyCycle, but simplified that handle the ranks of the vertices
    while len(eliminateList) < len(graph.listVertices):
        tempList = eliminateList.copy()
        for vertex in graph.listVertices:
            predecessors = list(vertex.previousVertices)
            if vertex not in eliminateList: 
                resultPredecessors = [p for p in predecessors if p not in eliminateList]
                if resultPredecessors == []:
                    tempList.append(vertex)
                    # assign the rank to the vertex
                    ranks[vertex] = k

        eliminateList = tempList
        # increment the rank at each iteration
        k += 1
    return ranks


def calculateEarliestDates (graph : Graph, ranks : dict) -> dict:
    earliestDates = {vertex: 0 for vertex in graph.listVertices}
    omega = graph.listVertices[-1]
    for i in range(ranks[omega]+1):
        listVerticesOfRankI = [k for k, v in ranks.items() if v==i]
        for vertex in listVerticesOfRankI:
            if vertex.previousVertices != []:
                earliestFinishDate = earliestDates[vertex.previousVertices[0]] + int(vertex.previousVertices[0].duration)
                for i in range(len(vertex.previousVertices)):
                    earliestFinishDate = max(earliestFinishDate, earliestDates[vertex.previousVertices[i]] + int(vertex.previousVertices[i].duration))
                earliestDates[vertex] =  earliestFinishDate
    return earliestDates


def calculateLatestDates(graph : Graph, ranks: dict, earliestDates: dict)-> dict:
    omega = graph.listVertices[-1]
    latestDates = {vertex: earliestDates[omega] for vertex in graph.listVertices}
    for i in range(ranks[omega]+1, 0, -1):
        listVerticesOfRankI = [k for k, v in ranks.items() if v==i]
        for vertex in listVerticesOfRankI:
            for previousVertex in vertex.previousVertices:
                latestDates[previousVertex] = min(latestDates[previousVertex], latestDates[vertex] - int(previousVertex.duration))
    return latestDates

def calculateFloats(earliestDates: dict, latestDates: dict, graph : Graph) -> dict:
    float = {vertex: 0 for vertex in graph.listVertices}
    for vertex in graph.listVertices:
        float[vertex] = latestDates[vertex] - earliestDates[vertex]
    return float


def calculateCriticalPath(float : dict, graph : Graph, ranks: dict):
    oneCriticalPath = []
    oneCriticalPath.append(graph.listVertices[0].value)
    listCriticalPath = []
    listCriticalPath.append(oneCriticalPath)
    previousVertex = graph.listVertices[0]
    for vertex in graph.listVertices:
        if float[vertex] == 0:
            if ranks[vertex] != 0 :
                if ranks[vertex] == ranks[previousVertex]:
                    anotherListCriticalPath = copy.deepcopy(listCriticalPath)
                    for criticalPath in anotherListCriticalPath:
                        criticalPath.pop()
                        criticalPath.append(vertex.value)
                    listCriticalPath = listCriticalPath + anotherListCriticalPath
                else :
                    for criticalPath in listCriticalPath:
                        criticalPath.append(vertex.value)
        previousVertex = vertex
    return listCriticalPath