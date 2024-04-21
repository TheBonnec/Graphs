from Model.Helper import *
from Model.Graph import Graph
from View.Tools import *


def displayCriticalPath(graph: Graph):
    clearConsole()
    title()

    ranks = computeRanks(graph)
    earliestDates = calculateEarliestDates(graph, ranks)                    
    latestDates = calculateLatestDates(graph, ranks, earliestDates)
    floats = calculateFloats(earliestDates, latestDates, graph)

    criticalPath = calculateCriticalPath(floats, graph)
    criticalPathList = list(criticalPath)

    print("The critical path is : ", criticalPathList)

    input("\nExit : ")