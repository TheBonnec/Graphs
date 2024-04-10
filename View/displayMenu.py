from View.getListFiles import getListFiles
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from View.displayGraph import displayGraph
from Model.Graph import Graph

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
                #case 2:
                #    verifyCycle(graph)
                #    verifyNegativeEdge(graph)





















