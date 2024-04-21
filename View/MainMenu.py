from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from Model.GraphsList import getAllGraphs
from View.GraphMenu import graphMenu
from InquirerPy import inquirer
from Model.Graph import Graph
from View.Tools import *


def mainMenu():

    ''' ----- Init ----- '''

    graphs: list[Graph] = getAllGraphs()
    isMenuRunning = True

    options: list[str] = []

    optionExit = Choice("Exit")

    for graph in graphs:
        options.append(Choice(graph.name))
    options.append(Separator())
    options.append(optionExit)




    ''' ----- View ----- '''

    def body():
        nonlocal isMenuRunning

        while isMenuRunning:
            clearConsole()
            title()

            menu = inquirer.select(
                message = "Select a table :",
                choices = options,
                default = None
            ).execute()


            if menu == optionExit.value:
                isMenuRunning = False
            elif menu:
                selectedGraph = getGraphFromName(graphName = menu)
                graphMenu(graph = selectedGraph)



    
    ''' ----- Methods ----- '''

    def getGraphFromName(graphName: str) -> Graph:
        for graph in graphs:
            if graph.name == graphName:
                return graph
    



    ''' ----- Run ----- '''

    body()

    