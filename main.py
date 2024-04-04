from Model.Graph import Graph


def main():
    graph = Graph("graph1","GraphsFiles/table1.txt")
    for i in range(len(graph.listV)):
        print("Vertex is :")
        graph.listV[i].print()
        print("Previous vertices : ")
        for j in range(len(graph.listV[i].previousVertices)):
            graph.listV[i].previousVertices[j].print()
    return
    

if __name__ == "__main__":
    main()