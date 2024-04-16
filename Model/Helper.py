from Model.Graph import Graph
from Model.Vertex import Vertex
import networkx as nx

def has_negative_edges(graph: Graph) -> bool:
    for vertex in graph.listVertices:
        for neighbor in vertex.previousVertices:
            if float(neighbor.duration) < 0:
                return True  # Negative edge detected
    return False  # No negative edge found

def calculate_latest_dates(graph: Graph):
    G = nx.DiGraph()
    for vertex in graph.listVertices:
        for prev_vertex in vertex.previousVertices:
            G.add_edge(prev_vertex.value, vertex.value, weight=int(vertex.duration))

    # Vérifier s'il y a des cycles dans le graphe
    if not nx.is_directed_acyclic_graph(G):
        raise ValueError("Le graphe contient un cycle, impossible de calculer les dates les plus tardives.")
    # --> tri topologique
    topo_sorted_vertices = list(nx.topological_sort(G))
    latest_start_times = {vertex: 0 for vertex in topo_sorted_vertices}

    # Initialiser le dernier noeud
    latest_start_times[topo_sorted_vertices[-1]] = int(graph.listVertices[-1].duration)

    # Calculer les dates les plus tardives en remontant dans le tri topologique
    for vertex in reversed(topo_sorted_vertices):
        current_duration = int(next((v.duration for v in graph.listVertices if v.value == vertex), None))
        for pred in G.predecessors(vertex):
            latest_start_times[pred] = min(latest_start_times[pred], latest_start_times[vertex] - current_duration)
    for vertex in topo_sorted_vertices:
        print(f"Latest start time for task {vertex}: {latest_start_times[vertex]}")

    return latest_start_times