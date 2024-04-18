from Model.Graph import Graph
from Model.Vertex import Vertex
#import networkx as nx

def verifyCycle(graph: Graph) -> bool:
    # Rosalind Marimond Algorithm to verify if a graph contains a cycle
    print("\nDetecting the cycle, by using the elimination by predecessors method.")

    eliminateList = []
    while len(eliminateList) < len(graph.listVertices):
        sourceVertices = []
        remainingVertices = list(graph.listVertices)
        tempList = eliminateList.copy()
        for vertex in graph.listVertices:
            predecessors = list(vertex.previousVertices)

            """print("Vertex: ", vertex.value)
            for predecessor in predecessors:
                print("Predecessor: ", predecessor.value)"""
            
            if vertex not in eliminateList:
                resultPredecessors = [p for p in predecessors if p not in eliminateList]
                if resultPredecessors == []:
                    tempList.append(vertex)
                    sourceVertices.append(vertex.value)

        remainingVertices = [vertex for vertex in remainingVertices if vertex not in tempList]   
        eliminateList = tempList

        if sourceVertices == [] and len(eliminateList) < len(graph.listVertices):
            print("\n\nCycle detected.")
            return True

        print("\nSource vertices: ", sourceVertices)
        print("Eliminating source vertices...")
        print("Remaining vertices: ", end = "")
        if remainingVertices == []: print("None")
        for vertex in remainingVertices:
            print(vertex.value, end = " ")

    print("\nNo cycle detected.")
    return False


"""
def hasNegativeEdges(graph: Graph) -> bool:
    for vertex in graph.listVertices:
        for neighbor in vertex.previousVertices:
            if float(neighbor.duration) < 0:
                return True  # Negative edge detected
    return False  # No negative edge found

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