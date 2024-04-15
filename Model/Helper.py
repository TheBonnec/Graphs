from asyncio import start_server
from networkx import topological_sort
from Model.Graph import Graph
from Model.Vertex import Vertex

def has_negative_edges(graph: Graph) -> bool:
    for vertex in graph.listVertices:
        for neighbor in vertex.previousVertices:
            if float(neighbor.duration) < 0:
                return True  # Negative edge detected
    return False  # No negative edge found

