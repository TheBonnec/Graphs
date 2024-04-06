from Model.Graph import Graph
from View.displayGraph import displayGraph


def main():
    graph = Graph("graph1","GraphsFiles/table2.txt")
    displayGraph(graph)
    return
    

if __name__ == "__main__":
    main()