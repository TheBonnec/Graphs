from Model.Graph import Graph


def main():
    graph = Graph("graph1","GraphsFiles/table2.txt")
    print(graph.listV[0].value)
    print(graph.listV[0].previousVertices)
    return
    

if __name__ == "__main__":
    main()