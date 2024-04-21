from View.getListFiles import getListFiles
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from View.displayGraph import displayGraph
from Model.Graph import Graph
from Model.Helper import*
from tabulate import tabulate as tb

def displayMenu(): 
    listTable = getListFiles()
    menuRunning = 1
    listTable.append("Exit")
    while(menuRunning):
        graphChoice = inquirer.select(
        message="Choose the table :",
        choices=listTable,
        default = None
        ).execute()
        if(graphChoice=="Exit"):
            break
        if(graphChoice):
            actionChoice = inquirer.rawlist(
                message ="Choose the action :",
                choices = [
                    Choice(value=1, name="Display the graph as a matrix"),
                    Choice(value=2, name="Check if there are cycles and/or negative edges"),
                    Choice(value=3, name="Compute and display the ranks of each vertices of the graph"),
                    Choice(value=4, name="Compute and display the earliest dates, the latest dates and the floats"),
                    Choice(value=5, name="Compute and display the critical path"),
                    Choice(value=None, name="Return")
                ],
                height=20
                
            ).execute()
            graph = Graph("Graph","GraphsFiles/"+graphChoice)
            match actionChoice:
                case 1:
                   displayGraph(graph)
                case 2:
                    if not verifyCycle(graph) and not hasNegativeEdges(graph):
                        print("This is a scheduling graph. It has no cycle and no negative edges")
                case 3:
                    if not verifyCycle(graph) and not hasNegativeEdges(graph):
                        print("This is a scheduling graph.")
                        print("\nComputing and displaying the ranks of each vertices of the graph...")
                        ranks = computeRanks(graph)
                        ranksValues = list(ranks.values())
                        Vertices = [vertex.value for vertex in list(ranks.keys())]
                        ranksValues.insert(0, "ranks")
                        Vertices.insert(0, "Vertices")
                        print(tb([Vertices, ranksValues], headers='firstrow'))
                    else: print("The properties necessary are not satisfied, this is not a scheduling graph.")
                case 4:
                    if not verifyCycle(graph) and not hasNegativeEdges(graph):
                        print("This is a scheduling graph.")
                        print("\nComputing and displaying the ranks of each vertices of the graph...")
                        ranks = computeRanks(graph)
                        ranksValues = list(ranks.values())
                        Vertices = [vertex.value for vertex in list(ranks.keys())]
                        ranksValues.insert(0, "ranks")
                        Vertices.insert(0, "Vertices")
                        earliestDates = calculateEarliestDates(graph, ranks)
                        earliestDatesValues = list(earliestDates.values())
                        earliestDatesValues.insert(0, "Earliest Dates")
                        latestDates = calculateLatestDates(graph, ranks, earliestDates)
                        latestDatesValues = list(latestDates.values())
                        latestDatesValues.insert(0,"Latest Dates")
                        floats = calculateFloats(earliestDates, latestDates, graph)
                        floatsValues = list(floats.values())
                        floatsValues.insert(0,"Floats")
                        print(tb([Vertices, ranksValues, earliestDatesValues, latestDatesValues, floatsValues], headers='firstrow'))
                case 5:
                    if not verifyCycle(graph) and not hasNegativeEdges(graph):
                        print("This is a scheduling graph.")
                        print("\nComputing and displaying the ranks of each vertices of the graph...")
                        ranks = computeRanks(graph)
                        ranksValues = list(ranks.values())
                        Vertices = [vertex.value for vertex in list(ranks.keys())]
                        ranksValues.insert(0, "ranks")
                        Vertices.insert(0, "Vertices")
                        earliestDates = calculateEarliestDates(graph, ranks)
                        earliestDatesValues = list(earliestDates.values())
                        earliestDatesValues.insert(0, "Earliest Dates")                       
                        latestDates = calculateLatestDates(graph, ranks, earliestDates)
                        latestDatesValues = list(latestDates.values())
                        latestDatesValues.insert(0,"Latest Dates")
                        floats = calculateFloats(earliestDates, latestDates, graph)
                        floatsValues = list(floats.values())
                        floatsValues.insert(0,"Floats")
                        print(tb([Vertices, ranksValues, earliestDatesValues, latestDatesValues, floatsValues], headers='firstrow'))
                        criticalPath = calculateCriticalPath(floats, graph)
                        criticalPathList = list(criticalPath)
                        print("The critical path is : ",criticalPathList)





















