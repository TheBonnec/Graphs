from tabulate import tabulate as tb
from Model.Graph import Graph
from Model.Helper import *
from View.Tools import *


def displayCalendars(graph: Graph):
    clearConsole()
    title()

    ranks = computeRanks(graph)
    ranksValues = list(ranks.values())
    vertices = [vertex.value for vertex in list(ranks.keys())]
    ranksValues.insert(0, "Ranks")
    vertices.insert(0, "Vertices")

    earliestDates = calculateEarliestDates(graph, ranks)
    earliestDatesValues = list(earliestDates.values())
    earliestDatesValues.insert(0, "Earliest Dates")    

    latestDates = calculateLatestDates(graph, ranks, earliestDates)
    latestDatesValues = list(latestDates.values())
    latestDatesValues.insert(0, "Latest Dates")
    print(tb([vertices, ranksValues, earliestDatesValues, latestDatesValues], headers='firstrow'))

    input("\nExit : ")