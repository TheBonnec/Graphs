from Model.Graph import Graph
from View.displayGraph import DisplayGraph


def main():
    graph = Graph("graph1","GraphsFiles/table2.txt")
    DisplayGraph(graph)
    return
    

if __name__ == "__main__":
    main()