from Model.Graph import Graph
from tabulate import tabulate as tb
from Model.Helper import *
from View.Tools import *


def displayFloats(graph: Graph):
    clearConsole()
    title()

    ranks = computeRanks(graph)
    earliestDates = calculateEarliestDates(graph, ranks)
    latestDates = calculateLatestDates(graph, ranks, earliestDates)
    floats = calculateFloats(earliestDates = earliestDates, latestDates = latestDates, graph = graph)

    floatsValues = list(floats.values())
    floatsValues.insert(0, "Floats")

    ranksValues = list(ranks.values())
    vertices = [vertex.value for vertex in list(ranks.keys())]
    ranksValues.insert(0, "Ranks")
    vertices.insert(0, "Vertices")

    print(tb([vertices, ranksValues, floatsValues], headers='firstrow'))

    input("\nExit : ")