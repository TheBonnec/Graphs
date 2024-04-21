from Model.Graph import Graph
from View.Displays.displayGraph import displayGraph

from Model.Helper import *

    
def maintrace():
    
    graph = Graph("graph2", "GraphsFiles/table2.txt")

    ecrire(f"\n   {graph.name} \n\n\n")
    displayGraph(graph)
    if verifyCycle(graph = graph) == False and hasNegativeEdges(graph = graph) == False:
        ecrire("\n\n ==> This graph can be a scheduling graph.\n")
        
        ranks = computeRanks(graph)
        earliestdates = calculateEarliestDates(graph, ranks)
        latestdates = calculateLatestDates(graph, ranks, earliestdates)
        floats = calculateFloats(earliestdates, latestdates, graph)
    
    else:
        ecrire("\n\n ==> This graph cannot be a scheduling graph.\n\n")


if __name__ == "__main__":
    maintrace()