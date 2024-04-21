from Model.Graph import Graph
from View.displayGraph import displayGraph
from View.displayMenu import displayMenu
from Model.Helper import verifyCycle, hasNegativeEdges, computeRanks, DijkstraAlgorithm # calculateLatestDates

def main():
    graph = Graph("graph1", "GraphsFiles/table1.txt")
    displayGraph(graph)
    DijkstraAlgorithm(graph)


    """
    if not verifyCycle(graph) and not hasNegativeEdges(graph):
        print("This is a scheduling graph.")
        print("\nComputing and displaying the ranks of each vertices of the graph...")
        ranks = computeRanks(graph)
        for vertex, rank in ranks.items():
            print(f"Rank of task {vertex.value}: {rank}")

    else: print("The properties necessary are not satisfied, this is not a scheduling graph.") """


    """project_end_date = 50
        try:
            latest_dates = calculateLatestDates(graph, project_end_date)
            for vertex_value, start_date in latest_dates.items():
                print(f"Latest start time for task {vertex_value}: {start_date}")
            print("Les dates les plus tardives ont été calculées.")
        except ValueError as e:
            print(e)"""

if __name__ == "__main__":
    main()