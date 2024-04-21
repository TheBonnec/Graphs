from Model.Graph import Graph
from View.Displays.displayGraph import displayGraph

from Model.Helper import *

    
def maintrace():
    
    graph = Graph("GRAPH 12", "GraphsFiles/table12.txt")

    ecrire(f"\n   {graph.name} \n\n\n")
    displayGraph(graph)
    if verifyCycle(graph = graph) == False and hasNegativeEdges(graph = graph) == False:
        ecrire("\n\n ==> This graph can be a scheduling graph.\n")
        
        ranks = computeRanks(graph)
        earliestdates = calculateEarliestDates(graph, ranks)
        latestdates = calculateLatestDates(graph, ranks, earliestdates)
        floats = calculateFloats(earliestdates, latestdates, graph)
        criticalpath = calculateCriticalPath(floats, graph, ranks)

        ecrire("\n\n ==> The critical path of this graph is : ")
        for i in range(len(criticalpath)):
            for j in range(len(criticalpath[i])-1):
                    ecrire(str(criticalpath[i][j])+ " --> ")
            ecrire(str(criticalpath[i][-1])+ "\n")
    
    else:
        ecrire("\n\n ==> This graph cannot be a scheduling graph.\n\n")


if __name__ == "__main__":
    maintrace()