from Model.Graph import Graph
from View.displayGraph import displayGraph
from View.displayMenu import displayMenu
from Model.Helper import has_negative_edges


def main():
    graph = Graph("graph1","GraphsFiles/table11.txt")
    if has_negative_edges(graph):
        print("Le graphe a des arêtes négatives.")
    else:
        print("Le graphe n'a pas d'arêtes négatives.")

if __name__ == "__main__":
    main()