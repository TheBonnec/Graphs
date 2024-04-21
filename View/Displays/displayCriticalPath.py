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

    criticalPaths = calculateCriticalPath(floats, graph, ranks)

    if len(criticalPaths) < 2:
        print("The critical path is :\n")
    else:
        print("The critical paths are :\n")

    for criticalPath in criticalPaths:
        display = ""
        for index in range(len(criticalPath) - 1):
            display += criticalPath[index] + " -> "
        display += criticalPath[-1]
        print(display)


    input("\nExit : ")