from Model.Graph import Graph
from Model.Vertex import Vertex
from Model.InvertedVertex import InvertedVertex

#import networkx as nx

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


def invertGraph(graph: Graph) -> Graph:
    invertedVertices = {}

    # Création des InvertedVertex correspondants
    for vertex in graph.listVertices:
        invertedVertices[vertex.id] = InvertedVertex(vertex.value, vertex.duration)

    # Ajout des successeurs
    for vertex in graph.listVertices:
        for previousVertex in vertex.previousVertices:
            invertedVertices[previousVertex.id].addNextVertex(invertedVertices[vertex.id])

    newInvertedGraph = Graph(graph.name, graph.fileName)
    newInvertedGraph.listVertices = list(invertedVertices.values())

    return newInvertedGraph


def pifPafPoufRemettreLeGrapheAlEndroit(graph: Graph) -> Graph:
    normalVertices = {}

    # Création des Vertex correspondants
    for vertex in graph.listVertices:
        normalVertices[vertex.id] = Vertex(vertex.value, vertex.duration)

    # Ajout des prédécesseurs
    for vertex in graph.listVertices:
        for nextVertex in vertex.previousVertices:
            normalVertices[nextVertex.id].addPreviousVertex(normalVertices[vertex.id])

    newInvertedGraph = Graph(graph.name, graph.fileName)
    newInvertedGraph.listVertices = list(normalVertices.values())

    return newInvertedGraph


# Dijkstra's algorithm but trying with working by successors
def DijkstraAlgorithm(graph: Graph) -> dict:




# Dijkstra's algorithm but trying with working by predecessors
def DijkstraAlgorithm(graph: Graph) -> dict:
    # use of a dictionnary to store the distances 
    distances = {vertex: float('inf') for vertex in graph.listVertices}
    orderVertices = {vertex: None for vertex in graph.listVertices}

    CC = [source for source in graph.listVertices if source.previousVertices == []]
    distances[CC[0]] = 0
    M = [vertex for vertex in graph.listVertices if vertex not in CC]
    
    while(len(CC) < len(graph.listVertices)):
        tempList = CC.copy()
        for vertex in M:
            predecessors = list(vertex.previousVertices)
            predecessorsCC = [p for p in predecessors if p in CC]
            
        
        minV = min([distances[vertex] for vertex in M])
        for vertex in M:
            if distances[vertex] == minV:
                tempList.append(vertex)
        
        M = [vertex for vertex in M if vertex not in tempList]

        CC = tempList
        print("CC: ", [vertex.value for vertex in CC])

    

"""
def calculateLatestDates(graph: Graph, project_end_date: int) -> dict:
    # Create a directed graph in NetworkX from the Graph object
    G = nx.DiGraph()
    for vertex in graph.listVertices:
        vertex_duration = int(vertex.duration)
        G.add_node(vertex.value, duration=vertex_duration) 
        for predecessor in vertex.previousVertices:
            G.add_edge(predecessor.value, vertex.value)

    if not nx.is_directed_acyclic_graph(G):
        raise ValueError("The graph contains a cycle, it's impossible to calculate the latest dates.")

    # Initialize the latest start times with the project end date
    latest_finish_times = {vertex: project_end_date for vertex in G.nodes}
    latest_start_times = {vertex: project_end_date for vertex in G.nodes}

    G_reverse = G.reverse()

    for vertex in nx.topological_sort(G_reverse):
        if G_reverse.out_degree(vertex) == 0:
            latest_finish_times[vertex] = project_end_date
        else:
            min_latest_finish = project_end_date
            for successor in G_reverse.successors(vertex):
                successor_duration = G.nodes[successor]['duration']
                min_latest_finish = min(min_latest_finish, latest_finish_times[successor] - successor_duration)
            latest_finish_times[vertex] = min_latest_finish
            latest_start_times[vertex] = latest_finish_times[vertex] - G.nodes[vertex]['duration']

    return latest_start_times

"""