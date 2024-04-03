from Model.Graph import Graph


def main():
    graph = Graph("graph1","GraphsFiles/table7.txt")
    print(graph.listV[0].value)
    print(graph.listV[0].previousVertices[1].value)
    return
    

if __name__ == "__main__":
    main()