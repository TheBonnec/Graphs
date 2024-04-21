from Model.Graph import Graph
from InquirerPy import inquirer
from View.Tools import *
from Model.Helper import *
from View.Displays.displayGraph import displayGraph
from View.Displays.displayRanks import displayRanks
from View.Displays.displayCalendars import displayCalendars
from View.Displays.displayFloats import displayFloats
from View.Displays.displayCriticalPath import displayCriticalPath
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator



def graphMenu(graph: Graph):

    ''' ----- Init ----- '''

    # Is Menu Running
    isMenuRunning = True
    isGraphASchedulingGraph: bool = False
    if verifyCycle(graph = graph) == False and hasNegativeEdges(graph = graph) == False:
        isGraphASchedulingGraph = True

    # Menu Options
    optionGraph = Choice("Display the Graph")
    optionRanks = Choice("Display the Ranks")
    optionCalendars = Choice("Display the Calendars")
    optionFloats = Choice("Display the Floats")
    optionCriticalPaths = Choice("Display the Critical Path(s)")
    optionExit = Choice("Exit")

    options = [optionGraph]

    if isGraphASchedulingGraph:
        options.append(optionRanks)
        options.append(optionCalendars)
        options.append(optionFloats)
        options.append(optionCriticalPaths)
    
    options.append(Separator())
    options.append(optionExit)





    ''' ----- View ----- '''

    def body():
        nonlocal isMenuRunning, isGraphASchedulingGraph

        while isMenuRunning:
            clearConsole()
            title()

            print(f"\n   {graph.name}")

            if isGraphASchedulingGraph:
                print("🟢 This graph can be a scheduling graph.\n")
            else:
                print("🔴 This graph cannot be a scheduling graph.\n")

            menu = inquirer.select(
                message = "Select an option :",
                choices = options,
                default = None
            ).execute()

            if menu == optionExit.value:
                isMenuRunning = False
            elif menu == optionGraph.value:
                displayGraph(graph = graph)
            elif menu == optionRanks.value:
                displayRanks(graph = graph)
            elif menu == optionCalendars.value:
                displayCalendars(graph = graph)
            elif menu == optionFloats.value:
                displayFloats(graph = graph)
            elif menu == optionCriticalPaths.value:
                displayCriticalPath(graph = graph)


    

    ''' ----- Run ----- '''

    body()
        
