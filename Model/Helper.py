from Model.Graph import Graph
from Model.Vertex import Vertex
import networkx as nx

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