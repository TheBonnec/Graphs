from Model.Helper import computeRanks
from tabulate import tabulate as tb
from Model.Graph import Graph
from View.Tools import *



def displayRanks(graph: Graph):
    clearConsole()
    title()

    ranks = computeRanks(graph)
    ranksValues = list(ranks.values())
    Vertices = [vertex.value for vertex in list(ranks.keys())]
    ranksValues.insert(0, "Ranks")
    Vertices.insert(0, "Vertices")
    print(tb([Vertices, ranksValues], headers='firstrow'))

    input("\nExit : ")